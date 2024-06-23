from typing import Any
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from studies.models import StudySource, Endpoint, Endpointstudy
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution


class Command(BaseCommand):
    help = "TODO" #TODO

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def get_test_type(self, word):
        test_type_vocab = Taxonomy.objects.get(code='TEST_TYPE')
        try:
            test_type_node = TaxonomyNode.objects.get(taxonomy=test_type_vocab, extended_name=word)
            return test_type_node
        except:
            test_type_node = TaxonomyNode.objects.create(taxonomy=test_type_vocab, extended_name=word, code='NORA')
            return test_type_node
        
    def get_species(self, word):
        mtx_vocab = Taxonomy.objects.get(code='MTX')
        base = word.strip().lower()
        if base != 'human':
            search_term = base.capitalize() + ' (as animal)'
        else:
            search_term = base.capitalize() + ' (as organism)'

        try:
            species_node = TaxonomyNode.objects.get(taxonomy=mtx_vocab, extended_name=search_term)
            return species_node
        except:
            species_node = TaxonomyNode.objects.create(taxonomy=mtx_vocab, extended_name=search_term, code='NORA')
            return species_node
        
    def get_guideline(self, word):
        if 'OECD TG' in word:
            number = word.split('OECD TG')[1].strip()
            search_term = f'OECD Guideline {number}'
        else:
            search_term = word

        studyguideline = Taxonomy.objects.get(code='STUDYGUIDELINE')
        
        try:
            guideline = TaxonomyNode.objects.get(taxonomy=studyguideline, extended_name__icontains=search_term)
            return guideline
        except:
            guideline = TaxonomyNode.objects.create(taxonomy=studyguideline, extended_name=search_term, code='NORA')
            return guideline
        
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
        
    def add_study(self, row):
        print(f'Adding endpoint study for NF {row["nf name"]}')
        result_msg = 'Endpoint studies:'
        r_question_number = row["question"]
        #Find opinion with this question
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        #Find novel food with this opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        r_study_source = row["study source"]
        study_source_node = StudySource.objects.get(title=r_study_source)

        according_to = GuidelineQualifier.objects.get_or_create(title='according to')

        endpoint_study = Endpointstudy.objects.create(novel_food=novel_food, study_source=study_source_node, guideline_qualifier=according_to[0])

        r_remarks = row["remarks"]
        if not pd.isna(r_remarks):
            endpoint_study.remarks = r_remarks
        
        if not pd.isna(row["test material"]):
            endpoint_study.test_material = row["test material"]
        else:
            result_msg += f' Test material not found.'

        mtx_vocab = Taxonomy.objects.get(code='MTX')

        # Get sex from vocab
        if not pd.isna(row['sex']):
            sex_object = TaxonomyNode.objects.get(taxonomy=mtx_vocab, extended_name=row['sex'])
            endpoint_study.sex = sex_object

        r_study_type = row["study type"]
        if not pd.isna(r_study_type):
            study_type_node = self.get_test_type(r_study_type)
            endpoint_study.test_type = study_type_node
        else:
            result_msg += f'Test type missing.'

        r_species = row["species"]
        if not pd.isna(r_species):
            species_node = self.get_species(r_species)
            endpoint_study.species = species_node
        else:
            result_msg += f'Species missing.'

        r_guideline = row["guideline"]
        if not pd.isna(r_guideline):
            guideline_node = self.get_guideline(r_guideline)
            endpoint_study.guideline = guideline_node

        r_duration = row["duration"]
        if r_duration == 'single' or pd.isna(r_duration) or '-' in r_duration or '<' in r_duration: #TODO Fix after asking
            pass
        else:
            duration, unit = self.get_duration(r_duration)
            endpoint_study.study_duration = duration
            endpoint_study.duration_unit = unit

        endpoint_study.save()

        if result_msg != 'Endpoint studies:': # We have to report something
            result_msg += '\n'

            try:
                contribution = Contribution.objects.get(opinion=opinion)
                contribution.remarks = contribution.remarks + result_msg
                contribution.save()
            except:
                pass

        return result_msg




    def handle(self, *args: Any, **options: Any):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])

        Endpointstudy.objects.all().delete()

        for index, row in df.iterrows():
            self.add_study(row)