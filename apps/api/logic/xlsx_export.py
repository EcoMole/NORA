from io import BytesIO

import pandas as pd
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
        genotox_study.pop("djangoAdminGenotox", "")
        genotox_rows.append(genotox_study)
    return genotox_rows


def serialize_endpoint(endpoint):
    reference_point = endpoint.get("referencePoint", "")
    qualifier = endpoint.get("qualifier", "")
    lovalue = endpoint.get("lovalue", "")
    subpopulation = endpoint.get("subpopulation", "")
    id = endpoint.get("endpointId", "")

    id_str = f"(Id: {id})"

    # Filter the empty strings out
    return " - ".join(
        filter(bool, [str(id_str), reference_point, qualifier, lovalue, subpopulation])
    )


def serialize_population(population):
    subgroup = population.get("subgroup", "")
    qualifier = population.get("qualifier", "")
    value = population.get("value", "")

    # Filter the empty strings out
    return " ".join(filter(bool, [subgroup, qualifier, value]))


def create_final_outcome_rows(endpoint, nf_id, study_id):
    final_outcomes = endpoint.get("finalOutcomes", "")
    endpoint_id = endpoint.get("endpointId", "")
    final_outcome_rows = []
    for final_outcome in final_outcomes:
        final_outcome["endpointId"] = endpoint_id
        final_outcome["endpointstudyId"] = study_id
        final_outcome.pop("djangoAdminFinalOutcome", "")
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
        endpoint_study.pop("djangoAdminEndpointstudy", "")
        study_id = endpoint_study.get("endpointstudyId", "")
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
            final_outcomes = create_final_outcome_rows(endpoint, nf_id, study_id)
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
        adme_study.pop("djangoAdminAdme", "")
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


def serialize_species(species):
    name = species.get("name", "")
    scientific_name = species.get("scientificName", "")
    genus = species.get("genus", "")
    family = species.get("family")
    organism_type = species.get("orgType")

    return " < ".join(
        filter(bool, [name, scientific_name, genus, family, organism_type])
    )


def serialize_synonyms(synonyms):
    names = []
    for synonym in synonyms:
        names.append(synonym.get("title", ""))

    return " ; ".join(names)


def process_organism_identity(organisms, nf_id):
    organism_rows = []
    for organism in organisms:
        organism["novelFoodId"] = nf_id
        species_list = organism.get("species", [])
        if len(species_list) > 0:
            serialized_species = [
                serialize_species(species) for species in species_list
            ]
            organism["species"] = " ; ".join(serialized_species)

        organism_synonyms = organism.get("orgSynonyms", [])
        if len(organism_synonyms) > 0:
            organism_common_names = [
                synonym
                for synonym in organism_synonyms
                if synonym["typeTitle"] == "common name"
            ]
            organism_trade_names = [
                synonym
                for synonym in organism_synonyms
                if synonym["typeTitle"] == "trade name"
            ]
            organism["common names"] = serialize_synonyms(organism_common_names)
            organism["trade names"] = serialize_synonyms(organism_trade_names)

        if len(organism_synonyms) > 0:
            if organism_synonyms[0].get("typeTitle", "") != "":
                organism_common_names = [
                    synonym
                    for synonym in organism_synonyms
                    if synonym["typeTitle"] == "common name"
                ]
                organism_trade_names = [
                    synonym
                    for synonym in organism_synonyms
                    if synonym["typeTitle"] == "trade name"
                ]
                organism["common names"] = serialize_synonyms(organism_common_names)
                organism["trade names"] = serialize_synonyms(organism_trade_names)
            else:
                organism["synonyms"] = serialize_synonyms(organism_synonyms)

        organism.pop("orgSynonyms", "")
        organism.pop("__typename", "")

        organism_rows.append(organism)
    return organism_rows


def serialize_production_processes(processes):
    procs = []
    for process in processes:
        procs.append(process["process"])
    return " , ".join(procs)


def process_compositions(compositions, nf_id, food_form):
    composition_rows = []  # radek s nf id, nf food form, slozenim
    for composition in compositions:
        composition["novelFoodId"] = nf_id
        composition["foodForm"] = food_form
        composition_rows.append(composition)
        composition.pop("__typename", "")
    return composition_rows


def process_nf_variants(variants, nf_id):
    nf_variants_rows = []
    composition_rows = []
    for variant in variants:
        var = {}
        var["novelFoodId"] = nf_id
        var["foodForm"] = variant.get("foodForm", "not selected for export")
        # var["proposedUses"] =
        uses = []
        for proposed_use in variant.get("proposedUses", []):
            use = proposed_use.get("useType", "")
            population = proposed_use.get("population", None)
            if population:
                proposed_population = serialize_population(population)
            remarks = proposed_use.get("remarks", "")
            prop_use = f"{use}"
            if population:
                prop_use += f"( {proposed_population} )"
            if remarks != "":
                prop_use += f" - {remarks}"
            uses.append(prop_use)
        if len(uses) > 0:
            var["proposedUses"] = " ; ".join(uses)
        risk_flags = variant.get("riskAssessRedFlags", [])
        if len(risk_flags) > 0:
            var["riskAssessRedFlags"] = serialize_synonyms(risk_flags)
        processes = variant.get("productionProcesses", [])
        if len(processes) > 0:
            var["productionProcesses"] = serialize_production_processes(processes)

        compositions = variant.get("compositions", [])
        if len(compositions) > 0:
            composition_rows += process_compositions(
                compositions, nf_id, var["foodForm"]
            )
        nf_variants_rows.append(var)

    return nf_variants_rows, composition_rows


def process_chemicals(chemicals, nf_id):
    chemicals_rows = []

    for chemical in chemicals:
        chemical["novelFoodId"] = nf_id
        chem_synonyms = chemical.get("chemSynonyms", [])
        if len(chem_synonyms) > 0:
            if chem_synonyms[0].get("typeTitle", "") != "":
                chemical_common_names = [
                    synonym
                    for synonym in chem_synonyms
                    if synonym["typeTitle"] == "common name"
                ]
                chemical_trade_names = [
                    synonym
                    for synonym in chem_synonyms
                    if synonym["typeTitle"] == "trade name"
                ]
                chemical["common names"] = serialize_synonyms(chemical_common_names)
                chemical["trade names"] = serialize_synonyms(chemical_trade_names)
            else:
                chemical["synonyms"] = serialize_synonyms(chem_synonyms)

        chemical.pop("chemSynonyms", "")
        chemical.pop("__typename", "")

        descriptors = chemical.get("chemDescriptors", [])

        if len(descriptors) > 0:
            for descriptor in descriptors:
                if "type" in descriptor:
                    chemical[descriptor["type"]] = f"{descriptor.get('value', '')} "

        chemical.pop("chemDescriptors", "")

        chemicals_rows.append(chemical)

    return chemicals_rows


def process_synonyms(synonyms):
    serialized_common_names = ""
    serialized_trade_names = ""
    serialized_synonyms = None
    if len(synonyms) > 0:
        if synonyms[0].get("typeTitle", "") != "":
            common_names = [
                synonym for synonym in synonyms if synonym["typeTitle"] == "common name"
            ]
            trade_names = [
                synonym for synonym in synonyms if synonym["typeTitle"] == "trade name"
            ]
            serialized_common_names = serialize_synonyms(common_names)
            serialized_trade_names = serialize_synonyms(trade_names)
        else:
            serialized_synonyms = serialize_synonyms(synonyms)
    else:
        serialized_synonyms = serialize_synonyms(synonyms)
    return serialized_common_names, serialized_trade_names, serialized_synonyms


def process_hbgvs(hbgvs):
    hbgvs_result = []
    for hbgv in hbgvs:
        substance = hbgv.get("substance", "")
        exceeded = hbgv.get("exceeded", "")
        type = hbgv.get("type", "")
        hbgv_repr = " - ".join(filter(bool, [substance, exceeded, type]))
        hbgvs_result.append(hbgv_repr)

    return " ; ".join(hbgvs_result)


def flatten_json(
    data,
    genotox_rows,
    endpoint_rows,
    adme_rows,
    final_outcome_rows,
    organism_rows,
    nf_variants_rows,
    composition_rows,
    chemicals_rows,
    parent_key="",
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
            if key == "organisms":  # process_organism_identity
                organism_rows += process_organism_identity(value, nf_id)
                continue
            if key == "chemicals":
                chemicals_rows += process_chemicals(value, nf_id)
                continue
            if key == "novelFoodVariants":
                new_nf_variant_rows, new_composition_rows = process_nf_variants(
                    value, nf_id
                )
                nf_variants_rows += new_nf_variant_rows
                composition_rows += new_composition_rows
                continue
            if key == "synonyms":
                (
                    serialized_common_names,
                    serialized_trade_names,
                    serialized_synonyms,
                ) = process_synonyms(value)
                if serialized_synonyms is not None:
                    if serialized_synonyms != "":
                        items.append(("synonyms", serialized_synonyms))
                else:
                    items.append(("common names", serialized_common_names))
                    items.append(("trade names", serialized_trade_names))
                continue
            if key == "hbgvs":
                hbgvs = process_hbgvs(value)
                items.append(("hbvgs", hbgvs))
                continue

            if (
                key.startswith("__") or key == "id" or "djangoAdmin" in key
            ):  # Skip all the inner keys from graphql + djangoAdmin keys
                continue
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):  # Dict was found -> recurse
                (
                    item,
                    genotox_rows,
                    endpoint_rows,
                    adme_rows,
                    final_outcome_rows,
                    organism_rows,
                    nf_variants_rows,
                    composition_rows,
                    chemicals_rows,
                ) = flatten_json(
                    value,
                    genotox_rows,
                    endpoint_rows,
                    adme_rows,
                    final_outcome_rows,
                    organism_rows,
                    nf_variants_rows,
                    composition_rows,
                    chemicals_rows,
                    new_key,
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
                            organism_rows,
                            nf_variants_rows,
                            composition_rows,
                            chemicals_rows,
                        ) = flatten_json(
                            item,
                            genotox_rows,
                            endpoint_rows,
                            adme_rows,
                            final_outcome_rows,
                            organism_rows,
                            nf_variants_rows,
                            composition_rows,
                            chemicals_rows,
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

    return (
        dict(items),
        genotox_rows,
        endpoint_rows,
        adme_rows,
        final_outcome_rows,
        organism_rows,
        nf_variants_rows,
        composition_rows,
        chemicals_rows,
    )


def create_export(novel_food_data):
    filters = novel_food_data[1]

    novel_food_data = novel_food_data[0]

    novel_food_df_data = []
    genotox_rows = []
    endpoint_rows = []
    adme_rows = []
    final_outcome_rows = []
    organism_rows = []
    nf_variants_rows = []
    composition_rows = []
    chemicals_rows = []
    for item in novel_food_data:
        (
            nf,
            genotox_rows,
            endpoint_rows,
            adme_rows,
            final_outcome_rows,
            organism_rows,
            nf_variants_rows,
            composition_rows,
            chemicals_rows,
        ) = flatten_json(
            item,
            genotox_rows,
            endpoint_rows,
            adme_rows,
            final_outcome_rows,
            organism_rows,
            nf_variants_rows,
            composition_rows,
            chemicals_rows,
        )
        novel_food_df_data.append(nf)

    novel_food_df = pd.DataFrame(novel_food_df_data)
    genotox_df = pd.DataFrame(genotox_rows)
    endpoint_df = pd.DataFrame(endpoint_rows)
    adme_df = pd.DataFrame(adme_rows)
    final_outcomes_df = pd.DataFrame(final_outcome_rows)
    organisms_df = pd.DataFrame(organism_rows)
    nf_variants_df = pd.DataFrame(nf_variants_rows)
    composition_df = pd.DataFrame(composition_rows)
    chemicals_df = pd.DataFrame(chemicals_rows)

    filters_df = pd.DataFrame(filters, columns=["Applied Export Filters"])

    dataframes = {
        "Novel foods": novel_food_df,
        "Organism identity of NF": organisms_df,
        "Chemical identity of NF": chemicals_df,
        "Novel Food variants": nf_variants_df,
        "Composition": composition_df,
        "Genotox studies": genotox_df,
        "Endpoint studies": endpoint_df,
        "ADME studies": adme_df,
        "Final outcomes": final_outcomes_df,
    }

    for sheet_name, df in dataframes.items():
        if "novelFoodId" in df.columns:
            dataframes[sheet_name] = df[
                ["novelFoodId"] + [col for col in df.columns if col != "novelFoodId"]
            ]

    # Filter out empty DataFrames
    non_empty_dataframes = {name: df for name, df in dataframes.items() if not df.empty}

    output = BytesIO()

    # Write non-empty DataFrames to Excel
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        filters_df.to_excel(writer, sheet_name="APPLIED FILTERS", index=False)
        for sheet_name, df in non_empty_dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Autofit column width for each sheet
        for sheet in writer.sheets.values():
            sheet.autofit()

    output.seek(0)

    # Return the Excel file as an HTTP response
    response = HttpResponse(
        output,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=exported_data.xlsx"

    return response
