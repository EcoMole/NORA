from typing import Any
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from studies.models import StudySource, Endpoint, Endpointstudy
from taxonomies.models import Taxonomy, TaxonomyNode, Subgroup, Population
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution
from composition.models import NovelFoodVariant, ProposedUseType

class Command(BaseCommand):
    help = "TODO" #TODO

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def get_qualifier(self, word):
        qualifier_taxonomy = Taxonomy.objects.get(code='QUALIFIER')
        map = {
            '<' : 'Less than',
            '<=' : 'Less than or equal',
            '>' : 'Greater than',
            '>=' : 'Greater than or equal',
            '=' : 'Equal to',
        }
        qualifier_obj = TaxonomyNode.objects.get(taxonomy=qualifier_taxonomy, extended_name=map[word])


    def add_use(self, row):
        result_msg = 'Uses:'
        
        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        r_proposed_use = row["proposed use"]
        r_food_forms = row["food forms"]
        r_target_subgroup = row["target population"]
        r_age = row["age"]
        r_age_qualifier = row["age qualifier"]

        proposed_use_obj = ProposedUseType.objects.get(title=r_proposed_use) 
        subgroup_obj = Subgroup.objects.get(title=r_target_subgroup)

        if not pd.isna(r_age):
            qualifier_obj = self.get_qualifier(r_age_qualifier)
            population_obj = Population.objects.get_or_create(subgroup=subgroup_obj, value=r_age, qualifier=qualifier_obj)
        else:
            population_obj = Population.objects.get_or_create(subgroup=subgroup_obj)

        food_forms = r_food_forms.split(',')


    
    def handle(self, *args: Any, **options: Any):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])