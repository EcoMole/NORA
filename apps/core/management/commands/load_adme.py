from django.core.management.base import BaseCommand
import pandas as pd
from studies.models import StudySource, InvestigationType, ADME, ADMEInvestigationType
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood
from administrative.models import Question, OpinionQuestion


class Command(BaseCommand):
    help = "Command to load ADME studies from csv."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def get_test_type(self, word):
        test_type_vocab = Taxonomy.objects.get(code='TEST_TYPE')
        try:
            test_type_node = TaxonomyNode.objects.get(taxonomy=test_type_vocab, extended_name=word)
        except TaxonomyNode.DoesNotExist:
            test_type_node = TaxonomyNode.objects.create(taxonomy=test_type_vocab, extended_name=word, code='NORA')
        return test_type_node
        
    def get_guideline(self, word):
        studyguideline = Taxonomy.objects.get(code='STUDYGUIDELINE')
        guideline_obj = TaxonomyNode.objects.get_or_create(taxonomy=studyguideline, extended_name=word, code='NORA')
        return guideline_obj[0]

    def add_study(self, row):
        print('Adding ADME study for NF', row["nf name"])

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

        study_source_node, _ = StudySource.objects.get_or_create(title=row["study source"])
        according_to = GuidelineQualifier.objects.get_or_create(title='according to') 
        adme_study = ADME.objects.create(novel_food=novel_food, guideline_qualifier=according_to[0], study_source=study_source_node)  

        adme_study.test_material = row["test material"]

        if not pd.isna(row["guideline"]):
            adme_study.guideline = self.get_guideline(row["guideline"])

        r_investigation_types = row["investigation types"]
        if not pd.isna(r_investigation_types):
            investigations = r_investigation_types.split(',')
            for investigation in investigations:
                investigation_type_obj = InvestigationType.objects.get_or_create(title=investigation.strip())[0]
                ADMEInvestigationType.objects.create(adme=adme_study, investigation_type=investigation_type_obj)

        if not pd.isna(row["test type"]):
            adme_study.test_type = self.get_test_type(row["test type"])

        adme_study.save()

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        ADMEInvestigationType.objects.all().delete()
        ADME.objects.all().delete()

        for _, row in df.iterrows():
            self.add_study(row)