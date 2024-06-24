from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from studies.models import Genotox, StudySource
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution

class Command(BaseCommand):
    help = "TODO" #TODO

    outcomes = ['negative', 'positive', 'inconclusive']

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def get_pos_neg(self, word):
        posneg = Taxonomy.objects.get(code='POSNEG') #FINAL delete create
        pos = TaxonomyNode.objects.get(taxonomy=posneg, code='POS') #FINAL delete create
        neg = TaxonomyNode.objects.get(taxonomy=posneg, code='NEG') #FINAL delete create
        inconclusive = TaxonomyNode.objects.get(taxonomy=posneg, code='INC') #FINAL delete create

        if word == 'negative':
            return neg
        elif word == 'positive':
            return pos
        elif word == 'inconclusive':
            return inconclusive
        
        return None
    
    def get_guideline(self, word):
        print('getting guideline for', word)
        studyguideline = Taxonomy.objects.get(code='STUDYGUIDELINE')
        guideline = Taxonomy.objects.get(code='GUIDELINE')
        if 'OECD TG' in word:
            number = word.split('OECD TG')[1].strip()
            #get the guideline node:
            try:
                guideline_node = TaxonomyNode.objects.exclude(taxonomy=guideline).get(extended_name__icontains=f'OECD Guideline {number}')
                print('found guideline node')
                return guideline_node
            # CHeck if it exists
            except TaxonomyNode.DoesNotExist:
                guideline_node = TaxonomyNode.objects.create(taxonomy=studyguideline, extended_name=f'OECD Guideline {number}', code='NORA')
                print(f'did not find guideline node {word}, creating')
                return guideline_node
        
            except TaxonomyNode.MultipleObjectsReturned:
                print(f'multiple OECD guideline nodes {word}, returning first')
                guideline_node = TaxonomyNode.objects.filter(taxonomy=guideline, extended_name__icontains=f'OECD Guideline {number}').first()
                return guideline_node

        else:
            try:
                guideline_node = TaxonomyNode.objects.get(taxonomy=studyguideline, extended_name=word)
            except:
                guideline_node = TaxonomyNode.objects.create(taxonomy=studyguideline, extended_name=word, code='NORA')
            return guideline_node

    def get_test_type(self, word):
        test_type_vocab = Taxonomy.objects.get(code='TEST_TYPE')
        try:
            test_type_node = TaxonomyNode.objects.get(taxonomy=test_type_vocab, extended_name=word)
            return test_type_node
        except:
            #print(f'did not find test type node {word}, creating')
            test_type_node = TaxonomyNode.objects.create(taxonomy=test_type_vocab, extended_name=word, code='NORA')
            return test_type_node


    def add_study(self, row):
        print('Adding genotox study for ', row['nf name'])

        result_msg = 'Genotox:'
        
        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        according_to = GuidelineQualifier.objects.get_or_create(title='according to') 

        genotox_study = Genotox.objects.create(novel_food=novel_food, guideline_qualifier=according_to[0])  

        r_test_material = row['test material']
        
        if not pd.isna(r_test_material):
            genotox_study.test_material = r_test_material
            genotox_study.save()
        else:
            result_msg += f"Test material missing." # if missing, report it

        r_guideline = row['guideline']
        if not pd.isna(r_guideline):
            guideline_node = self.get_guideline(r_guideline)
            genotox_study.guideline = guideline_node
            genotox_study.save()

        r_outcome = row['outcome']
        
        if not pd.isna(r_outcome):
            outcome_node = self.get_pos_neg(r_outcome)
            genotox_study.outcome = outcome_node
            genotox_study.save()
        else:
            result_msg += f"Outcome missing." # if missing, report it

        r_study_source = row['study source']
        study_source_node = StudySource.objects.get(title=r_study_source)
        genotox_study.study_source = study_source_node
        genotox_study.save()

        r_test_type = row['test type']
        if not pd.isna(r_test_type):
            test_type_node = self.get_test_type(r_test_type)
            genotox_study.test_type = test_type_node
            genotox_study.save()
        else:
            result_msg += f"Test type missing." # if missing, report it

        if not pd.isna(row['remarks']):
            genotox_study.remarks = row['remarks']
            genotox_study.save()

        if result_msg != 'Genotox:': # We have to report something
            result_msg += '\n'

            try:
                contribution = Contribution.objects.get(opinion=opinion)
                contribution.remarks = contribution.remarks + result_msg
                contribution.save()
            except:
                pass

        return result_msg
        
        


    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        Genotox.objects.all().delete()

        for index, row in df.iterrows():
            self.add_study(row)