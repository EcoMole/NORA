from django.core.management.base import BaseCommand
import pandas as pd
from studies.models import StudySource, InvestigationType, ADME, ADMEInvestigationType
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion
from core.models import Contribution


class Command(BaseCommand):
    help = "Command that loads ADME studies from csv."

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
        
    def get_guideline(self, word):
        studyguideline = Taxonomy.objects.get(code='STUDYGUIDELINE')
        guideline_obj = TaxonomyNode.objects.get_or_create(taxonomy=studyguideline, extended_name=word, code='NORA')
        return guideline_obj[0]

    def add_study(self, row):
        print('Adding ADME study for NF', row["nf name"])
        result_msg = 'ADME:'
        r_question_number = row["question"]
        #Find opinion with this question
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        #Find novel food with this opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        r_study_source = row["study source"]
        if r_study_source == 'no ADME in opinion':
            return

        study_source_node = StudySource.objects.get(title=r_study_source)
        according_to = GuidelineQualifier.objects.get_or_create(title='according to') 
        adme_study = ADME.objects.create(novel_food=novel_food, guideline_qualifier=according_to[0], study_source=study_source_node)  

        r_test_material = row["test material"]
        if not pd.isna(r_test_material):
            adme_study.test_material = r_test_material 

        if not pd.isna(row["guideline"]):
            guideline_node = self.get_guideline(row["guideline"])
            adme_study.guideline = guideline_node

        adme_study.save()

        r_investigation_types = row["investigation types"]
        investigations = r_investigation_types.split(',')
        for investigation in investigations:
            investigation_type_obj = InvestigationType.objects.get(title=investigation.strip())
            ADMEInvestigationType.objects.create(adme=adme_study, investigation_type=investigation_type_obj)

        r_test_type = row["test type"]
        if not pd.isna(r_test_type):
            test_type_node = self.get_test_type(r_test_type)
            adme_study.test_type = test_type_node
            adme_study.save()
        else:
            result_msg += f"Missing test type for ADME study"

        if result_msg != 'ADME:': # We have to report something
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
        ADMEInvestigationType.objects.all().delete()
        ADME.objects.all().delete()

        for index, row in df.iterrows():
            self.add_study(row)