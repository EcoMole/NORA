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
        }
        genotox_study["novelFoodId"] = nf_id
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


def process_endpoint_studies(endpointstudies, nf_id):
    endpoint_rows = []
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
        endpoint_study["endpoints"] = "; ".join(serialized_endpoints)
        endpoint_study["novelFoodId"] = nf_id
        endpoint_rows.append(endpoint_study)
    return endpoint_rows

def process_adme_studies(admes, nf_id):
    adme_rows = []
    for adme_study in admes:
        investig_types = [investigation_type['title'] for investigation_type in adme_study['investigationTypes']]
        adme_study['investigationTypes'] = "; ".join(investig_types)
        adme_study = {
            key: value
            for key, value in adme_study.items()
            if not key.startswith("__") and key != "id"
        }
        adme_study["novelFoodId"] = nf_id
        adme_rows.append(adme_study)
    return adme_rows

def flatten_json(data, genotox_rows, endpoint_rows, adme_rows, parent_key="", sep="."):
    items = []
    list_sep = ", "

    nf_id = data.get("novelFoodId", '')
    items.append(("novelFoodId", nf_id))

    if isinstance(data, dict):

        for key, value in data.items():
            if key == "genotoxes":
                genotox_rows += process_genotox_studies(value, nf_id)
                continue
            if key == "endpointstudies":
                endpoint_rows += process_endpoint_studies(value, nf_id)
                continue
            if key == "admes":
                adme_rows += process_adme_studies(value, nf_id)
                continue
            if (
                key.startswith("__") or key == "id"
            ):  # Skip all the inner keys from graphql
                continue
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):  # Dict was found -> recurse
                item, genotox_rows, endpoint_rows, adme_rows = flatten_json(
                    value, genotox_rows, endpoint_rows, adme_rows, new_key, sep=sep
                )
                items.extend(item.items())
                # items.extend(flatten_json(value, genotox_df, endpointstudies_df, new_key, sep=sep).items())
            elif isinstance(value, list):
                # Flattent the list
                flattened_list = []
                for item in value:
                    if isinstance(item, dict):  # Dict was found -> recurse
                        item, genotox_rows, endpoint_rows, adme_rows = flatten_json(
                            item, genotox_rows, endpoint_rows, adme_rows, "", sep=sep
                        )
                        flattened_list.append(item)
                    else:
                        flattened_list.append(repr(item))
                # Concatenate the list into one column
                elements = []
                for i in flattened_list:
                    if isinstance(i, list):  # can this happen?
                        elements.append(i)
                    if isinstance(i, dict):
                        representation = " ".join(x for x in i.values())
                        elements.append(representation)
                concatenated_value = list_sep.join(elements)
                items.append((new_key, concatenated_value))
            else:
                if value is None:
                    value = ""
                items.append((new_key, value))
    else:
        items.append((parent_key, data))

    return dict(items), genotox_rows, endpoint_rows, adme_rows


def create_export(novel_food_data):
    print("Creating export...")
    novel_food_df_data = []
    genotox_rows = []
    endpoint_rows = []
    adme_rows = []
    for item in novel_food_data:
        nf, genotox_rows, endpoint_rows, adme_rows = flatten_json(
            item["node"], genotox_rows, endpoint_rows, adme_rows
        )
        novel_food_df_data.append(nf)

    novel_food_df = pd.DataFrame(novel_food_df_data)
    genotox_df = pd.DataFrame(genotox_rows)
    endpoint_df = pd.DataFrame(endpoint_rows)
    adme_df = pd.DataFrame(adme_rows)

    # Reorder the columns so that novelFoodId is first
    if "novelFoodId" in genotox_df.columns:
        genotox_df = genotox_df[
            ["novelFoodId"]
            + [col for col in genotox_df.columns if col != "novelFoodId"]
        ]

    if "novelFoodId" in endpoint_df.columns:
        endpoint_df = endpoint_df[
            ["novelFoodId"]
            + [col for col in endpoint_df.columns if col != "novelFoodId"]
        ]

    if "novelFoodId" in adme_df.columns:
        adme_df = adme_df[
            ["novelFoodId"]
            + [col for col in adme_df.columns if col != "novelFoodId"]
        ]

    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        novel_food_df.to_excel(writer, sheet_name="novel_food", index=False)
        genotox_df.to_excel(writer, sheet_name="genotox", index=False)
        endpoint_df.to_excel(writer, sheet_name="endpointstudies", index=False)
        adme_df.to_excel(writer, sheet_name="adme", index=False)

        # Get the worksheets
        novel_food_ws = writer.sheets["novel_food"]
        genotox_ws = writer.sheets["genotox"]
        endpoint_ws = writer.sheets["endpointstudies"]
        adme_ws = writer.sheets["adme"]

        # Autofit columns for each worksheet
        novel_food_ws.autofit()
        genotox_ws.autofit()
        endpoint_ws.autofit()
        adme_ws.autofit()

    output.seek(0)

    # Return the Excel file as an HTTP response
    response = HttpResponse(
        output,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=exported_data.xlsx"

    return response
