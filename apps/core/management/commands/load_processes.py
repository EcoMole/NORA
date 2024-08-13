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
    help = "Command that loads production processes from csv." 

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def add_process_step(self, row):
        print("Adding process step for nf:", row["nf name"])

        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        r_food_form = row["food form"]
        if pd.isna(r_food_form) == True:  # Should only have one variant then
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food)
        else:
            nf_variant = NovelFoodVariant.objects.get(
                novel_food=novel_food, food_form__title=r_food_form
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

        if not pd.isna(row["red flag"]):
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

        for index, row in df.iterrows():
            self.add_process_step(row)
