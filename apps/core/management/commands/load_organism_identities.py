import pandas as pd
from administrative.models import OpinionQuestion, Question
from django.core.management.base import BaseCommand
from novel_food.models import (
    Family,
    Genus,
    NovelFood,
    NovelFoodOrganism,
    Organism,
    OrganismSyn,
    OrgType,
    Species,
    SynonymType,
)
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "Command that loads organism identities of NFs from csv."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def add_organism_identity(self, row):
        print("Adding organism identity for nf:", row["nf name"])

        try:
            question = Question.objects.get(number=row["question"])
        except Question.DoesNotExist:
            print("Question not found - returning")
            return
        opinion_question = OpinionQuestion.objects.get(question=question)
        try:
            novel_food_obj = NovelFood.objects.get(opinion=opinion_question.opinion)
        except NovelFood.DoesNotExist:
            print("Novel food not found - returning")
            return

        if not pd.isna(row["vocab"]):  # We know its in vocabulary
            organism_vocab = TaxonomyNode.objects.get(
                extended_name=row["vocab"].strip(), taxonomy__code="MTX"
            )
        else: # We need to create a dummy node, that user can manage later
            organism_vocab = TaxonomyNode.objects.get(
                extended_name="Dummy node", taxonomy__code="MTX", code="NORA"
            )

        # Create the organism
        organism_obj = Organism.objects.create(vocab_id=organism_vocab)

        org_type_obj, _ = OrgType.objects.get_or_create(title=row["type"])
        if not pd.isna(row["family"]):
            family_obj = Family.objects.get_or_create(
                title=row["family"], org_type=org_type_obj
            )
            genus_obj = Genus.objects.get_or_create(
                title=row["genus"], family=family_obj[0]
            )

        else:
            print("Family missing, created dummy node -> rename it.")
            genus_obj = Genus.objects.get_or_create(title=row["genus"])

        if "," in row["species"]:
            #Multiple species for one organism, fill in manually
            print("Multiple species for one organism, fill in manually")
            return
        else:
            Species.objects.get_or_create(
                name=row["species"], genus=genus_obj[0], organism=organism_obj
            )

        # Connect Organism to Novel Food

        nf_organism = NovelFoodOrganism.objects.create(
            organism=organism_obj, novel_food=novel_food_obj
        )

        if not pd.isna(row["variant"]):
            nf_organism.variant = row["variant"]

        if not pd.isna(row["gmo"]):
            nf_organism.is_gmo = TaxonomyNode.objects.get(code=row["gmo"], taxonomy__code="YESNO")

        if not pd.isna(row["qps"]):
            nf_organism.has_qps = TaxonomyNode.objects.get(code=row["qps"], taxonomy__code="YESNO")

        if not pd.isna(row["part"]):
            # Try to find the part in MTX
            try:
                part_obj = TaxonomyNode.objects.get(
                    extended_name=row["part"], taxonomy__code="MTX"
                )
                nf_organism.org_part = part_obj
            except TaxonomyNode.DoesNotExist:
                print("Part used not found in vocabulary -> add it.")

        if not pd.isna(row["cell culture"]):
            nf_organism.cell_culture = row["cell culture"]

        if not pd.isna(row["cell culture modified"]):
            nf_organism.cells_modified = TaxonomyNode.objects.get(
                code=row["cell culture modified"], taxonomy__code="YESNO"
            )

        nf_organism.save()

        common_name_synonym_type = SynonymType.objects.get(title="common name")

        r_common_names = row["common names"]
        if not pd.isna(r_common_names):
            common_names = r_common_names.split(",")
            for common_name in common_names:
                OrganismSyn.objects.create(
                    organism=organism_obj,
                    title=common_name,
                    syn_type=common_name_synonym_type,
                )

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])

        # Create dummy node in MTX:
        TaxonomyNode.objects.get_or_create(
            extended_name="Dummy node",
            taxonomy=Taxonomy.objects.get(code="MTX"),
            code="NORA",
        )

        for _, row in df.iterrows():
            self.add_organism_identity(row)
