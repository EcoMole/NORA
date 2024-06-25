import pandas as pd
from administrative.models import Opinion, OpinionQuestion, Question
from core.models import Contribution
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
    help = "Script to load organism identities of Novel Foods."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def annotate(self, opinion, text):
        contribution = Contribution.objects.get(opinion=opinion)
        contribution.remarks = contribution.remarks + text
        contribution.save()

    def add_organism_identity(self, row):
        final_msg = "\n"
        print("Adding organism identity for nf:", row["nf name"])

        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food_obj = NovelFood.objects.get(opinion=opinion)

        if not pd.isna(row["vocab"]):  # We know its in vocabulary
            organism_vocab = TaxonomyNode.objects.get(
                extended_name=row["vocab"].strip(), taxonomy__code="MTX"
            )
        else:
            final_msg += (
                "Organism not found in vocabulary, created dummy node -> add it.\n"
            )
            organism_vocab = TaxonomyNode.objects.get(
                extended_name="Dummy node", taxonomy__code="MTX", code="NORA"
            )

        organism_obj = Organism.objects.create(vocab_id=organism_vocab)

        org_type_obj = OrgType.objects.get(title=row["type"])
        if not pd.isna(row["family"]):
            family_obj = Family.objects.get_or_create(
                title=row["family"], org_type=org_type_obj
            )
            genus_obj = Genus.objects.get_or_create(
                title=row["genus"], family=family_obj[0]
            )

        else:
            final_msg += "Family missing, created dummy node -> rename it.\n"
            # family_obj = Family.objects.create(title='Dummy family', org_type=org_type_obj)
            genus_obj = Genus.objects.get_or_create(title=row["genus"])

        if "," in row["species"]:
            final_msg += "Multiple species for one organism, fill in manually.\n"
            self.annotate(opinion, final_msg)
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
            yes_no = TaxonomyNode.objects.get(code=row["gmo"], taxonomy__code="YESNO")
            nf_organism.is_gmo = yes_no
        else:
            final_msg += "GMO status for organism missing."

        if not pd.isna(row["qps"]):
            yes_no = TaxonomyNode.objects.get(code=row["qps"], taxonomy__code="YESNO")
            nf_organism.has_qps = yes_no

        if not pd.isna(row["part"]):
            # Try to find the part in MTX
            try:
                part_obj = TaxonomyNode.objects.get(
                    extended_name=row["part"], taxonomy__code="MTX"
                )
                nf_organism.org_part = part_obj
            except TaxonomyNode.DoesNotExist:
                final_msg += "Part used not found in vocabulary -> add it."

        if not pd.isna(row["cell culture"]):
            nf_organism.cell_culture = row["cell culture"]

        if not pd.isna(row["cell culture modified"]):
            nf_organism.are_the_cells_modified = TaxonomyNode.objects.get(
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

        self.annotate(opinion, final_msg)

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])

        # Create dummy node in MTX:
        TaxonomyNode.objects.get_or_create(
            extended_name="Dummy node",
            taxonomy=Taxonomy.objects.get(code="MTX"),
            code="NORA",
        )

        NovelFoodOrganism.objects.all().delete()
        Organism.objects.all().delete()

        for index, row in df.iterrows():
            self.add_organism_identity(row)
