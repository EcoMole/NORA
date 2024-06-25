from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from taxonomies.models import Taxonomy, TaxonomyNode
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution
from composition.models import NovelFoodVariant, ProductionNovelFoodVariant, RiskAssessmentRedFlags, RiskAssessmentRedFlagsNFVariant


class Command(BaseCommand):
    help = "TODO" #TODO

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def add_process_step(self, row):
        print('Adding process step for nf:', row['nf name'])
        result_msg = 'Process steps:'
        
        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        r_food_form = row["food form"]
        if pd.isna(r_food_form) == True: #Should only have one variant then
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food)
        else:
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food, food_form__title=r_food_form)

        if not pd.isna(row['process step']):
            try: 
                process_obj = TaxonomyNode.objects.get(extended_name=row["process step"], taxonomy__code="MTX")
                print(f'Found process {row["process step"]}')
            except TaxonomyNode.DoesNotExist:
                print(f"Did not find process {row['process step']}, creating.")
                process_obj = TaxonomyNode.objects.create(extended_name=row["process step"], code = 'NORA', taxonomy=Taxonomy.objects.get(code='MTX'))

            ProductionNovelFoodVariant.objects.create(id_novel_food_variant=nf_variant, process=process_obj)

        if not pd.isna(row['red flag']):
            red_flag = RiskAssessmentRedFlags.objects.get_or_create(title=row["red flag"])
            RiskAssessmentRedFlagsNFVariant.objects.create(nf_variant=nf_variant, risk_assessment=red_flag[0])

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        
        ProductionNovelFoodVariant.objects.all().delete()
        RiskAssessmentRedFlagsNFVariant.objects.all().delete()

        for index, row in df.iterrows():
            self.add_process_step(row)