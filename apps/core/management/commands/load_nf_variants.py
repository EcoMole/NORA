from django.core.management.base import BaseCommand
import pandas as pd
from taxonomies.models import Taxonomy, TaxonomyNode, Subgroup, Population
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion
from core.models import Contribution
from composition.models import NovelFoodVariant, FoodForm, ProposedUse

class Command(BaseCommand):
    help = "Command to load NF variants."

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
        return qualifier_obj
    
    def get_duration(self, word):
        unit_vocab = Taxonomy.objects.get(code='UNIT')
        if 'days' in word:
            search_term = 'Day'
            amount = int(word.split('days')[0].strip())
        elif 'weeks' in word:
            search_term = 'Week'
            amount = int(word.split('weeks')[0].strip())
        elif 'months' in word:
            search_term = 'Month'
            amount = int(word.split('months')[0].strip())
        elif 'years' in word:
            search_term = 'Year'
            amount = int(word.split('years')[0].strip())
        else:
            print(word)

        unit = TaxonomyNode.objects.get(taxonomy=unit_vocab, extended_name=search_term)
        return amount, unit


    def add_use(self, row):
        print('Adding use for NF name', row['nf name'])
        result_msg = 'Uses:'
        
        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        if row['food forms'] == '?':
            r_food_forms = 'powder'
            result_msg += 'Food form missing, assuming powder - check and correct.'

        r_proposed_use = row["proposed use"]
        r_food_forms = row["food forms"]
        r_target_subgroup = row["target population"]
        r_age = row["age"]
        r_age_qualifier = row["age qualifier"]

        subgroup_obj = Subgroup.objects.get(title=r_target_subgroup)

        if not pd.isna(r_age):
            qualifier_obj = self.get_qualifier(r_age_qualifier)
            age, unit = self.get_duration(r_age)
            population_obj = Population.objects.get_or_create(subgroup=subgroup_obj, value=age, qualifier=qualifier_obj, unit=unit)
        else:
            population_obj = Population.objects.get_or_create(subgroup=subgroup_obj, value=None, qualifier=None, unit=None)

        food_forms = r_food_forms.split(',')
        for food_form in food_forms:
            food_form_obj = FoodForm.objects.get_or_create(title=food_form.strip())
            nf_variant_obj = NovelFoodVariant.objects.get_or_create(novel_food=novel_food, food_form=food_form_obj[0])
            ProposedUse.objects.create(nf_variant = nf_variant_obj[0], use_type=r_proposed_use, population=population_obj[0])

    def create_empty_nf_variants(self):
        # For each novel food that doesnt have any NF variant, create 1:
        nf_list = NovelFood.objects.all()
        for nf in nf_list:
            nf_variants = NovelFoodVariant.objects.filter(novel_food=nf)
            if not nf_variants:
                NovelFoodVariant.objects.create(novel_food=nf)
                print(f'Creating empty NF variant for {nf.title}')
    
    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])

        NovelFoodVariant.objects.all().delete()
        Population.objects.all().delete()

        for index, row in df.iterrows():
            self.add_use(row)

        # For each NF without any variant, create one
        self.create_empty_nf_variants()