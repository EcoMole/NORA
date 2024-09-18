from typing import Any
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from studies.models import StudySource, Endpoint, Endpointstudy
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion, Opinion
from core.models import Contribution


class Command(BaseCommand):
    help = "Command to load endpoint studies from csv."

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
        if base != 'human': # Distinction between human and animal
            search_term = base.capitalize() + ' (as animal)'
        else:
            search_term = base.capitalize() + ' (as organism)'
        try:
            species_node = TaxonomyNode.objects.get(taxonomy=mtx_vocab, extended_name=search_term)
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
            search_term = word
            amount = 1

        unit = TaxonomyNode.objects.get(taxonomy=unit_vocab, extended_name=search_term)
        return amount, unit
    
    def get_reference_point(self, word):
        endpoint_hgv_vocab = Taxonomy.objects.get(code='ENDPOINT_HGV')
        ref_points_map = {
            'NOAEL' : 'No observed adverse effect level',
            'LOEL' : 'Lowest observable effect level',
            'LOAEL' : 'Lowest observed adverse effect level',
        }

        rp = TaxonomyNode.objects.get(taxonomy=endpoint_hgv_vocab, extended_name=ref_points_map[word])
        return rp
        
    def add_study(self, row):
        print(f'Adding endpoint study for NF {row["nf name"]}')
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

        r_study_source = row["study source"]
        study_source_node, _ = StudySource.objects.get_or_create(title=r_study_source)

        according_to = GuidelineQualifier.objects.get_or_create(title='according to')

        endpoint_study = Endpointstudy.objects.create(novel_food=novel_food, study_source=study_source_node, guideline_qualifier=according_to[0])
        endpoint_study.remarks = row["remarks"]
        endpoint_study.test_material = row["test material"]

        mtx_vocab = Taxonomy.objects.get(code='MTX')

        # Get sex from vocab
        if not pd.isna(row['sex']):
            sex_object = TaxonomyNode.objects.get(taxonomy=mtx_vocab, extended_name=row['sex'])
            endpoint_study.sex = sex_object

        if not pd.isna(row["study type"]):
            endpoint_study.test_type = self.get_test_type(row["study type"])

        if not pd.isna(row["species"]):
            endpoint_study.species =  self.get_species(row["species"])

        if not pd.isna(row["guideline"]):
            endpoint_study.guideline = self.get_guideline(row["guideline"])

        r_duration = row["duration"]
        if r_duration == 'single' or pd.isna(r_duration) or '-' in r_duration or '<' in r_duration:
            # No duration or too complex to parse
            print('Duration for endpoint study not imported.')
        else:
            duration, unit = self.get_duration(r_duration)
            endpoint_study.study_duration = duration
            endpoint_study.duration_unit = unit

        endpoint_study.save()

        r_ref_point = row["reference point"]
        if not pd.isna(r_ref_point):
            if r_ref_point != 'NOAEL' and r_ref_point != 'LOAEL' and r_ref_point != 'LOEL':
                print('Reference point for endpoint study not imported.')
            else:
                ref_point_obj = self.get_reference_point(r_ref_point)
                endpoint = Endpoint.objects.create(endpointstudy=endpoint_study, reference_point=ref_point_obj)
                if not pd.isna(row["qualifier"]):
                    qualifier_vocab = Taxonomy.objects.get(code='QUALIFIER')
                    qualifier_node = TaxonomyNode.objects.get(taxonomy=qualifier_vocab, extended_name=row["qualifier"])
                    endpoint.qualifier = qualifier_node
                

    def handle(self, *args: Any, **options: Any):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])

        for _, row in df.iterrows():
            self.add_study(row)