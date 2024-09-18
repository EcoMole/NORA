import pandas as pd
from io import BytesIO
from django.http import HttpResponse


def process_genotox_studies(genotoxes, nf_id):
    genotox_rows = []
    for genotox_study in genotoxes:
        genotox_study = {
            key: value
            for key, value in genotox_study.items()
            if not key.startswith("__") and key != "id"
        }  # ignore GraphQl metadata
        genotox_study["novelFoodId"] = nf_id  # Add NF id
        genotox_rows.append(genotox_study)
    return genotox_rows


def serialize_endpoint(endpoint):
    reference_point = endpoint.get("referencePoint", "")
    qualifier = endpoint.get("qualifier", "")
    lovalue = endpoint.get("lovalue", "")
    subpopulation = endpoint.get("subpopulation", "")

    # Filter the empty strings out
    return " - ".join(
        filter(bool, [reference_point, qualifier, lovalue, subpopulation])
    )


def serialize_population(population):
    subgroup = population.get("subgroup", "")
    qualifier = population.get("qualifier", "")
    value = population.get("value", "")

    # Filter the empty strings out
    return " ".join(filter(bool, [subgroup, qualifier, value]))


def create_final_outcome_rows(endpoint, nf_id):
    final_outcomes = endpoint.get("finalOutcomes", "")
    final_outcome_rows = []
    for final_outcome in final_outcomes:
        final_outcome = {
            key: value
            for key, value in final_outcome.items()
            if not key.startswith("__") and key != "id"
        }
        serialized_populations = []
        for population in final_outcome.get(
            "populations", []
        ):  # serialize populations into strings
            serialized_population = serialize_population(population)
            serialized_populations.append(serialized_population)
        final_outcome["populations"] = "; ".join(
            serialized_populations
        )  # make all populations into one column
        final_outcome["novelFoodId"] = nf_id  # Add NF id
        final_outcome_rows.append(final_outcome)
    return final_outcome_rows


def process_endpoint_studies(endpointstudies, nf_id):
    endpoint_rows = []
    final_outcome_rows = []
    for endpoint_study in endpointstudies:
        endpoint_study = {
            key: value
            for key, value in endpoint_study.items()
            if not key.startswith("__") and key != "id"
        }

        # endpoint-lovalue, subpopulation, qualifier, referencePoint into one column
        serialized_endpoints = [
            serialize_endpoint(endpoint)
            for endpoint in endpoint_study.get("endpoints", [])
        ]
        for endpoint in endpoint_study.get(
            "endpoints", []
        ):  # process the final outcomes for given endpoint
            final_outcomes = create_final_outcome_rows(endpoint, nf_id)
            final_outcome_rows += final_outcomes
        endpoint_study["endpoints"] = "; ".join(
            serialized_endpoints
        )  # make all endpoints into one column
        endpoint_study["novelFoodId"] = nf_id  # Add NF id
        endpoint_rows.append(endpoint_study)
    return endpoint_rows, final_outcome_rows


def process_adme_studies(admes, nf_id):
    adme_rows = []
    for adme_study in admes:
        investig_types = [
            investigation_type["title"]
            for investigation_type in adme_study["investigationTypes"]
        ]
        adme_study["investigationTypes"] = "; ".join(
            investig_types
        )  # flatten the investigation types into one column
        adme_study = {
            key: value
            for key, value in adme_study.items()
            if not key.startswith("__") and key != "id"
        }  # ignore GraphQl metadata
        adme_study["novelFoodId"] = nf_id  # Add NF id
        adme_rows.append(adme_study)
    return adme_rows


def flatten_json(
    data, genotox_rows, endpoint_rows, adme_rows, final_outcome_rows, parent_key=""
):
    items = []

    nf_id = data.get("novelFoodId", "")
    items.append(("novelFoodId", nf_id))

    if isinstance(data, dict):

        for key, value in data.items():
            if key == "genotoxes":  # Delegate into genotox studies sheet
                genotox_rows += process_genotox_studies(value, nf_id)
                continue
            if key == "endpointstudies":  # Delegate into endpoint studies sheets
                new_endpoint_rows, new_final_outcome_rows = process_endpoint_studies(
                    value, nf_id
                )
                endpoint_rows += new_endpoint_rows
                final_outcome_rows += new_final_outcome_rows
                continue
            if key == "admes":  # Delegate into adme studies sheet
                adme_rows += process_adme_studies(value, nf_id)
                continue
            if (
                key.startswith("__") or key == "id"
            ):  # Skip all the inner keys from graphql
                continue
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):  # Dict was found -> recurse
                item, genotox_rows, endpoint_rows, adme_rows, final_outcome_rows = (
                    flatten_json(
                        value,
                        genotox_rows,
                        endpoint_rows,
                        adme_rows,
                        final_outcome_rows,
                        new_key,
                    )
                )
                items.extend(item.items())
            elif isinstance(value, list):
                # Flatten the list
                flattened_list = []
                for item in value:
                    if isinstance(item, dict):  # Dict was found -> recurse
                        (
                            item,
                            genotox_rows,
                            endpoint_rows,
                            adme_rows,
                            final_outcome_rows,
                        ) = flatten_json(
                            item,
                            genotox_rows,
                            endpoint_rows,
                            adme_rows,
                            final_outcome_rows,
                            "",
                        )
                        flattened_list.append(item)
                    else:
                        flattened_list.append(repr(item))
                # Concatenate the list into one column
                elements = []
                for i in flattened_list:
                    representation = " ".join(
                        x for x in i.values()
                    )  # concatenate all values into one string
                    elements.append(representation)
                concatenated_value = ", ".join(
                    elements
                )  # divide different values by ','
                items.append((new_key, concatenated_value))
            else:
                if value is None:
                    value = ""
                items.append((new_key, value))
    else:
        items.append((parent_key, data))

    return dict(items), genotox_rows, endpoint_rows, adme_rows, final_outcome_rows


def create_export(novel_food_data):
    print("Creating export...")
    novel_food_df_data = []
    genotox_rows = []
    endpoint_rows = []
    adme_rows = []
    final_outcome_rows = []
    for item in novel_food_data:
        nf, genotox_rows, endpoint_rows, adme_rows, final_outcome_rows = flatten_json(
            item["node"], genotox_rows, endpoint_rows, adme_rows, final_outcome_rows
        )
        novel_food_df_data.append(nf)

    novel_food_df = pd.DataFrame(novel_food_df_data)
    genotox_df = pd.DataFrame(genotox_rows)
    endpoint_df = pd.DataFrame(endpoint_rows)
    adme_df = pd.DataFrame(adme_rows)
    final_outcomes_df = pd.DataFrame(final_outcome_rows)

    dataframes = [novel_food_df, genotox_df, endpoint_df, adme_df, final_outcomes_df]

    for df in dataframes:  # Reorder the columns so that novelFoodId is first in each df
        if "novelFoodId" in df.columns:
            df = df[
                ["novelFoodId"] + [col for col in df.columns if col != "novelFoodId"]
            ]

    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        novel_food_df.to_excel(writer, sheet_name="novel_food", index=False)
        genotox_df.to_excel(writer, sheet_name="genotox", index=False)
        endpoint_df.to_excel(writer, sheet_name="endpointstudies", index=False)
        adme_df.to_excel(writer, sheet_name="adme", index=False)
        final_outcomes_df.to_excel(writer, sheet_name="final_outcomes", index=False)

        # Get the worksheets
        for sheet in writer.sheets.values():
            sheet.autofit()  # Make the columns more wide

    output.seek(0)

    # Return the Excel file as an HTTP response
    response = HttpResponse(
        output,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=exported_data.xlsx"

    return response
