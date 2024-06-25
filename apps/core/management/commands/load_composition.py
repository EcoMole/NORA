from django.core.management.base import BaseCommand
import pandas as pd
from taxonomies.models import Taxonomy, TaxonomyNode
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution
from composition.models import NovelFoodVariant, Parameter, Composition, ParameterType

class Command(BaseCommand):
    help = "Script to load organism identities of Novel Foods."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def annotate(self, opinion, text):
        contribution = Contribution.objects.get(opinion=opinion)
        contribution.remarks = contribution.remarks + text
        contribution.save()

    def initialize_characterisations(self):
        # Take all novel food variants:
        novel_food_variants = NovelFoodVariant.objects.all()

        parameters = ['Carbohydrates', 'Fat', 'Protein', 'Minerals', 'Moisture', 'Vitamins']

        # create all 6 parameters
        carbs = Parameter.objects.create(title='Carbohydrates')
        fat = Parameter.objects.create(title='Fat')
        protein = Parameter.objects.create(title='Protein')
        minerals = Parameter.objects.create(title='Minerals')
        moisture = Parameter.objects.create(title='Moisture')
        vitamins = Parameter.objects.create(title='Vitamins')

        parameters_objs = [carbs, fat, protein, minerals, moisture, vitamins]

        percent_unit_obj = TaxonomyNode.objects.get(extended_name='Percent', taxonomy__code='UNIT')

        # For each novel food variant and for each parameter, create a composition
        for novel_food_variant in novel_food_variants:
            for parameter in parameters_objs:
                Composition.objects.create(novel_food_variant=novel_food_variant, parameter=parameter, unit=percent_unit_obj, type='characterisation')


    def interpret_value(self, value):
        qualifiers = ['<=', '>=', '<', '>']
        print(f'value: {value}')

        qualifier_vocab_map = { 
            '<' : 'Less than',
            '<=' : 'Less than or equal',
            '>' : 'Greater than',
            '>=' : 'Greater than or equal',
            '=' : 'Equal to',
        }

        if '-' in value: # We know its range, we want to get lower value and upper value
            print('range')
            lower, upper = value.split('-')
            return float(lower.strip()), float(upper.strip()), TaxonomyNode.objects.get(extended_name='Equal to', taxonomy__code='QUALIFIER')
        
        elif any(qualifier in value for qualifier in qualifiers):
            print('qualifier found')
            for qualifier in qualifiers:
                if qualifier in value:
                    print(f'matched qualifier {qualifier}')
                    return float(value.split(qualifier)[1].strip()), None, TaxonomyNode.objects.get(extended_name=qualifier_vocab_map[qualifier], taxonomy__code='QUALIFIER')
                
        else:
            return float(value), None, TaxonomyNode.objects.get(extended_name='Equal to', taxonomy__code='QUALIFIER')

    def add_composition(self, row):
        print(f'Adding composition for nf: {row["nf name"]}')

        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food_obj = NovelFood.objects.get(opinion=opinion)

        if pd.isna(row['value']):
            return
        # Get the proper variant
        r_food_form = row["food form"]
        if pd.isna(r_food_form) == True: #Should only have one variant then
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food_obj)
        else:
            nf_variant = NovelFoodVariant.objects.get(novel_food=novel_food_obj, food_form__title=r_food_form)

        #get the composition object
        parameter = Parameter.objects.get(title=row['parameter'])
        composition_obj = Composition.objects.get(novel_food_variant=nf_variant, parameter=parameter)
        value, upper_value, qualifier = self.interpret_value(row['value'])
        composition_obj.value = value
        if upper_value:
            composition_obj.upper_range_value = upper_value
        composition_obj.qualifier = qualifier
        if row['footnote']:
            composition_obj.footnote = row['footnote']
        composition_obj.save()


    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        Composition.objects.all().delete()
        Parameter.objects.all().delete()

        self.initialize_characterisations()

        for index, row in df.iterrows():
            self.add_composition(row)
