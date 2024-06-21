from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from studies.models import Genotox, StudySource
from taxonomies.models import Taxonomy, TaxonomyNode, GuidelineQualifier
from novel_food.models import NovelFood

class Command(BaseCommand):
    help = "Closes the specified poll for voting" #TODO fix

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
    
    def get_guideline(self, word): #TODO tady se bude menit slovnik
        guideline, _ = Taxonomy.objects.get_or_create(code='GUIDELINE')
        if 'OECD TG' in word:
            number = word.split('OECD TG')[1].strip()
            #get the guideline node:
            try:
                guideline_node = TaxonomyNode.objects.get(taxonomy=guideline, extended_name__icontains=f'OECD Guideline {number}')
                return guideline_node
            # CHeck if it exists
            except TaxonomyNode.DoesNotExist:
                guideline_node = TaxonomyNode.objects.create(taxonomy=guideline, extended_name=f'OECD Guideline {number}', code='NORA')
                print(f'did not find oece guideline node {word}, creating')
                return guideline_node
        
        else:
            print(f'did not find oece guideline node {word}, creating')
            guideline_node = TaxonomyNode.objects.create(taxonomy=guideline, extended_name=word, code='NORA')
            return guideline_node

    def get_test_type(self, word):
        test_type_vocab = Taxonomy.objects.get(code='TEST_TYPE')
        try:
            test_type_node = TaxonomyNode.objects.get(taxonomy=test_type_vocab, extended_name=word)
            return test_type_node
        except:
            print(f'did not find test type node {word}, creating')
            test_type_node = TaxonomyNode.objects.create(taxonomy=test_type_vocab, extended_name=word, code='NORA')
            return test_type_node


    def add_study(self, row):
        print('adding genotox study')
        r_study_nf = row['nf code']
        r_study_nf_name = row['nf name']
        #r_study_q_number = row['question number'] #TODO

        #find novel food with this code and name #TODO Better use q number
        if not pd.isna(r_study_nf):
            nf = NovelFood.objects.filter(nf_code=r_study_nf).first()
        else: #tady chci q number
            nf = NovelFood.objects.filter(title=r_study_nf_name).first()

        according_to = GuidelineQualifier.objects.get_or_create(title='according to') 

        genotox_study = Genotox.objects.create(novel_food=nf, guideline_qualifier=according_to[0])  

        r_test_material = row['test material']
        genotox_study.test_material = r_test_material
        genotox_study.save()

        r_guideline = row['guideline'] #TODO tady se zmeni slovnik
        if not pd.isna(r_guideline):
            guideline_node = self.get_guideline(r_guideline)
            genotox_study.genotox_guideline = guideline_node
            genotox_study.save()

        r_outcome = row['outcome']
        if not pd.isna(r_outcome):
            outcome_node = self.get_pos_neg(r_outcome)
            genotox_study.outcome = outcome_node
            genotox_study.save()

        #TODO remarks-jeste chybi v modelech

        r_study_source = row['study source']
        study_source_node = StudySource.objects.get(title=r_study_source)
        genotox_study.study_source = study_source_node
        genotox_study.save()

        r_test_type = row['test type']
        test_type_node = self.get_test_type(r_test_type)
        genotox_study.test_type = test_type_node
        genotox_study.save()

        if not pd.isna(row['remark']):
            genotox_study.remark = row['remark']
            genotox_study.save()
        


    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        Genotox.objects.all().delete()

        for index, row in df.iterrows():
            self.add_study(row)