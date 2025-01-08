from io import BytesIO

import pandas as pd
from django.http import HttpResponse


def filter_metadata(data, exclude_keys=None):
    """Filter out unwanted keys from a dictionary."""
    exclude_keys = exclude_keys or {"id"}
    return {
        k: v
        for k, v in data.items()
        if not k.startswith("__") and k not in exclude_keys
    }


def process_genotox_studies(genotoxes, nf_id):
    genotox_rows = []
    for genotox_study in genotoxes:
        genotox_study = filter_metadata(
            genotox_study, exclude_keys={"djangoAdminGenotox", "id"}
        )
        additional = {"novelFoodId": nf_id}
        genotox_rows.append({**additional, **genotox_study})
    return genotox_rows


def process_adme_studies(admes, nf_id):
    adme_rows = []
    for adme_study in admes:
        adme_study = filter_metadata(adme_study, exclude_keys={"djangoAdminAdme", "id"})

        investig_types = [
            investigation_type["title"]
            for investigation_type in adme_study.get("investigationTypes", [])
        ]
        if len(investig_types) > 0:
            adme_study["investigationTypes"] = "; ".join(
                investig_types
            )  # flatten the investigation types into one column

        additional = {"novelFoodId": nf_id}
        adme_rows.append({**additional, **adme_study})
    return adme_rows


def serialize_endpoint(endpoint):
    print(f"Serializing endpoint {endpoint}")
    parts = [
        f"(Id: {endpoint.get('endpointId', '')})",
        endpoint.get("referencePoint", ""),
        endpoint.get("qualifier", ""),
        endpoint.get("lovalue", ""),
        endpoint.get("unit", ""),
        endpoint.get("subpopulation", ""),
    ]
    print(f"Serialization result: {' - '.join(filter(bool, parts))}")
    return " - ".join(filter(bool, parts))


def process_endpoint_studies(endpointstudies, nf_id):
    endpoint_rows = []
    final_outcome_rows = []
    for endpoint_study in endpointstudies:        
        study_id = endpoint_study.get("endpointstudyId", "")

        serialized_endpoints = [
            serialize_endpoint(endpoint)
            for endpoint in endpoint_study.get("endpoints", [])
        ]
        if len(serialized_endpoints) > 0:
            endpoint_study["endpoints"] = "; ".join(serialized_endpoints)
        # process the final outcomes for given endpoint
        for endpoint in endpoint_study.get("endpoints", []):
            final_outcomes = create_final_outcome_rows(endpoint, nf_id, study_id)
            final_outcome_rows += final_outcomes

        endpoint_study = filter_metadata(
            endpoint_study, exclude_keys={"id", "djangoAdminEndpointstudy", "endpoints"}
        )

        additional_id = {
            "novelFoodId": nf_id,
        }

        endpoint_rows.append({**additional_id, **endpoint_study})

    return endpoint_rows, final_outcome_rows


def serialize_population(population):
    return " ".join(
        filter(
            bool,
            [
                population.get("subgroup", ""),
                population.get("qualifier", ""),
                population.get("value", ""),
            ],
        )
    )


def create_final_outcome_rows(endpoint, nf_id, study_id):
    final_outcomes = endpoint.get("finalOutcomes", "")
    endpoint_id = endpoint.get("endpointId", "")
    final_outcome_rows = []
    for final_outcome in final_outcomes:

        final_outcome = filter_metadata(
            final_outcome, exclude_keys={"id", "djangoAdminFinalOutcome"}
        )
        serialized_populations = []
        # serialize populations into strings
        for population in final_outcome.get("populations", []):
            serialized_population = serialize_population(population)
            serialized_populations.append(serialized_population)
        final_outcome["populations"] = "; ".join(serialized_populations)
        additional = {
            "novelFoodId": nf_id,
            "endpointId": endpoint_id,
            "endpointstudyId": study_id,
        }
        final_outcome_rows.append({**additional, **final_outcome})
    return final_outcome_rows


def serialize_species(species):
    return " < ".join(
        filter(
            bool,
            [
                species.get("name", ""),
                species.get("scientificName", ""),
                species.get("genus", ""),
                species.get("family", ""),
                species.get("orgType", ""),
            ],
        )
    )


def serialize_synonyms(synonyms):
    return " ; ".join(synonym.get("title", "") for synonym in synonyms)


def process_organism_identity(organisms, nf_id):
    organism_rows = []
    for organism in organisms:

        organism["novelFoodId"] = nf_id
        species_list = organism.get("species", [])
        serialized_species = [serialize_species(species) for species in species_list]
        if len(serialized_species) > 0:
            organism["species"] = " ; ".join(serialized_species)

        organism_synonyms = organism.get("orgSynonyms", [])

        organism_common_names = [
            synonym
            for synonym in organism_synonyms
            if synonym.get("typeTitle", "") == "common name"
        ]
        organism_trade_names = [
            synonym
            for synonym in organism_synonyms
            if synonym.get("typeTitle", "") == "trade name"
        ]
        if len(organism_common_names) > 0:
            organism["common names"] = serialize_synonyms(organism_common_names)
        if len(organism_trade_names) > 0:
            organism["trade names"] = serialize_synonyms(organism_trade_names)
        organism_general_synonyms = [
            synonym
            for synonym in organism_synonyms
            if synonym.get("typeTitle", "") == "synonym"
        ]
        if len(organism_general_synonyms) > 0:
            organism["synonyms"] = serialize_synonyms(organism_general_synonyms)

        organism = filter_metadata(
            organism, exclude_keys={"id", "djangoAdminOrganism", "orgSynonyms"}
        )

        organism_rows.append(organism)
    return organism_rows

def serialize_production_processes(processes):
    return " , ".join([proc["process"] for proc in processes])

def process_compositions(compositions, nf_id, nf_variant_id, food_form):
    composition_rows = []  # radek s nf id, nf food form, slozenim
    for composition in compositions:
        composition = filter_metadata(composition, exclude_keys={"id"})
        additional = {
            "novelFoodId": nf_id,
            "novelFoodVariantId": nf_variant_id,
            "foodForm": food_form,
        }
        composition_rows.append({**additional, **composition})
    return composition_rows


def process_nf_variants(variants, nf_id):
    nf_variants_rows = []
    composition_rows = []
    for variant in variants:
        var = {}
        var["novelFoodId"] = nf_id
        nf_variant_id = variant.get("novelfoodvariantId", "")
        var["novelFoodVariantId"] = nf_variant_id
        var["foodForm"] = variant.get("foodForm", "not selected for export")
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
                compositions, nf_id, nf_variant_id, var["foodForm"]
            )
        nf_variants_rows.append(var)

    return nf_variants_rows, composition_rows


def process_chemicals(chemicals, nf_id):
    chemicals_rows = []

    for chemical in chemicals:
        chemical["novelFoodId"] = nf_id
        chem_synonyms = chemical.get("chemSynonyms", [])
        if len(chem_synonyms) > 0:
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
            chemical_synonym_names = [
                synonym
                for synonym in chem_synonyms
                if synonym["typeTitle"] == "synonym"
            ]
            if len(chemical_common_names) > 0:
                chemical["common names"] = serialize_synonyms(chemical_common_names)
            if len(chemical_trade_names) > 0:
                chemical["trade names"] = serialize_synonyms(chemical_trade_names)
            if len(chemical_synonym_names) > 0:
                chemical["synonyms"] = serialize_synonyms(chemical_synonym_names)


        descriptors = chemical.get("chemDescriptors", [])

        if len(descriptors) > 0:
            for descriptor in descriptors:
                if "type" in descriptor:
                    chemical[descriptor["type"]] = f"{descriptor.get('value', '')} "

        chemical = filter_metadata(chemical, exclude_keys={"id", "djangoAdminChemical", "chemSynonyms", "chemDescriptors"})

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
                items.append(("HBGV", hbgvs))
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


def create_export(data):
    filters = data[1]

    novel_food_data = data[0]
    
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
        if "allergenicities" in item.keys():
            item["allergenicity"] = item.pop("allergenicities")
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
