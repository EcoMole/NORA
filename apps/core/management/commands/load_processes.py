import pandas as pd
from administrative.models import OpinionQuestion, Question
from composition.models import (
    NovelFoodVariant,
    ProductionNovelFoodVariant,
    RiskAssessRedFlag,
    RiskAssessRedFlagNFVariant,
)
from django.core.management.base import BaseCommand
from novel_food.models import NovelFood
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "Command to load production processes from csv."  

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def add_process_step(self, row):
        print("Adding process step for nf:", row["nf name"])

        try:
            question = Question.objects.get(number=row["question"])
        except Question.DoesNotExist:
            print("Question not found - returning")
            return
        opinion_question = OpinionQuestion.objects.get(question=question)
        try:
            novel_food = NovelFood.objects.get(opinion=opinion_question.opinion)
        except NovelFood.DoesNotExist:
            print("Novel food not found - returning")
            return

        if pd.isna(row["food form"]):  # Should only have one variant then
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food)
        else:
            nf_variant = NovelFoodVariant.objects.get(
                novel_food=novel_food, food_form__title=row["food form"]
            )

        if not pd.isna(row["process step"]):
            try:
                process_obj = TaxonomyNode.objects.get(
                    extended_name=row["process step"], taxonomy__code="MTX"
                )
                print(f'Found process {row["process step"]}')
            except TaxonomyNode.DoesNotExist:
                print(f"Did not find process {row['process step']}, creating.")
                process_obj = TaxonomyNode.objects.create(
                    extended_name=row["process step"],
                    code="NORA",
                    taxonomy=Taxonomy.objects.get(code="MTX"),
                )

            ProductionNovelFoodVariant.objects.create(
                nf_variant=nf_variant, process=process_obj
            )

        if not pd.isna(row["red flag"]): # Add risk assessment red flags
            red_flag = RiskAssessRedFlag.objects.get_or_create(
                title=row["red flag"]
            )
            RiskAssessRedFlagNFVariant.objects.create(
                nf_variant=nf_variant, risk_assess_red_flag=red_flag[0]
            )

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])

        ProductionNovelFoodVariant.objects.all().delete()
        RiskAssessRedFlagNFVariant.objects.all().delete()

        for _, row in df.iterrows():
            self.add_process_step(row)
