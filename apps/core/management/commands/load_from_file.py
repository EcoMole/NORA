from django.core.management.base import BaseCommand, CommandError
from core.models import User, Contribution
from administrative.models import Opinion, Panel, OPAuthor, Question, OPQuestion, ScientificOfficer, OPScientificOfficer
from novel_food.models import NovelFood, Allergenicity, AllergenicityNovelFood, NutritionalDisadvantage, NovelFoodSyn, SynonymType, GenotoxFinalOutcome
from taxonomies.models import Taxonomy, TaxonomyNode
import pandas as pd

from datetime import date
import datetime

class Command(BaseCommand):
    help = "Closes the specified poll for voting" #TODO fix

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def import_opinion(self, row):
        KN = User.objects.get(username='klara@ecomole.com') #FINAL delete create
        MF = User.objects.get(username='marketa@mit.edu')
        LC = User.objects.get(username='lucie@ecomole.com')

        #TODO document type

        r_title = row['title']
        r_doi = row['doi']
        if not pd.isnull(row['url']):
            r_url = row['url']
        else:
            r_url = None

        opinion_obj = Opinion.objects.create(title=r_title, doi=r_doi, url=r_url)

        r_publication_date = row['publication date']
        if not pd.isnull(r_publication_date):
            if '/' in r_publication_date:
                month, day, year = r_publication_date.split('/')
                if int(year) < 25:
                    year = '20' + year
                else:
                    year = '19' + year
                pub_date = date(int(year), int(month), int(day))
            elif '-' in r_publication_date:
                day, month, year = r_publication_date.split('-')
                pub_date = date(int(year), int(month), int(day))

            opinion_obj.publication_date = pub_date
            opinion_obj.save()

        r_adoption_date = row['adoption date']
        if not pd.isnull(r_adoption_date):
            day, month, year = r_adoption_date.split(' ')
            month = datetime.datetime.strptime(month, '%B').month
            adopt_date = date(int(year), month, int(day))

            opinion_obj.adoption_date = adopt_date
            opinion_obj.save()


        person = row['person']

        if person == 'KN':
            Contribution.objects.create(opinion=opinion_obj, user=KN, remarks=row['status']) #TODO status
        elif person == 'MF':
            Contribution.objects.create(opinion=opinion_obj, user=MF, remarks=row['status'])
        elif person == 'LČ':
            Contribution.objects.create(opinion=opinion_obj, user=LC, remarks=row['status'])

        status = row['status']

        # import panels
        panels = row['panel'].split(',')
        for panel in panels:
            panel_obj = Panel.objects.get(panel=panel.strip())
            OPAuthor.objects.create(id_op=opinion_obj, id_panel=panel_obj)

        # import questions
        r_question = row['question']
        r_mandate = row['mandate']
        # TODO mandates
        """ if '?' in r_mandate:
            mandate = None
        if 'TF' or 'traditional' in r_mandate:
            mandate =  """

        question = Question.objects.create(question=r_question)
        OPQuestion.objects.create(id_op=opinion_obj, id_question=question)

        # Import scientific officers
        r_so = row['so']
        if not pd.isna(r_so) and not r_so == 'N/A':
            sos = r_so.split(',')
            for so in sos:
                so_first_name, so_last_name = so.strip().split(' ', maxsplit=1)
                so_obj = ScientificOfficer.objects.get_or_create(first_name=so_first_name, last_name=so_last_name)
                OPScientificOfficer.objects.create(id_op=opinion_obj, id_sci_officer=so_obj[0])


        return opinion_obj

    def get_yes_no(self, word):
        yesno, _ = Taxonomy.objects.get_or_create(code='YESNO') #FINAL delete create
        yes = TaxonomyNode.objects.get_or_create(taxonomy=yesno, code='Y') #FINAL delete create
        no = TaxonomyNode.objects.get_or_create(taxonomy=yesno, code='N') #FINAL delete create
        unknown = TaxonomyNode.objects.get_or_create(taxonomy=yesno, code='U') #FINAL delete create

        if word == 'Yes' or word == 'yes':
            return yes[0] #FINAL delete tu nulu
        
        if word == 'No' or word == 'no':
            return no[0]
        
        if word == 'Not specified' or word == 'not specified' or word == 'N/A':
            return unknown[0]

    def get_unit(self, word):
        unit, _ = Taxonomy.objects.get_or_create(code='UNIT') #FINAL delete create
        year = TaxonomyNode.objects.get_or_create(taxonomy=unit, code='6207A', short_name='Year') #FINAL delete create, FINAL delete short_name
        month = TaxonomyNode.objects.get_or_create(taxonomy=unit, code='6206A', short_name='Month') #FINAL delete create, FINAL delete short_name
        day = TaxonomyNode.objects.get_or_create(taxonomy=unit, code='6134A', short_name='Day') #FINAL delete create, FINAL delete short_name

        if word in ['month', 'Month', 'month(s)', 'Month(s)']:
            return month[0] #FINAL delete 0
        
        if word in ['year', 'Year', 'year(s)', 'Year(s)']:
            return year[0]
        
        if word in ['day', 'Day', 'days', 'Days']:
            return day[0]

    def import_novel_food(self, row, opinion):
        result_msg = 'Novel food: '
        r_nf_name = row['nf name']
        if pd.isna(row['nf code']):
            r_nf_code = None
        else:
            r_nf_code = row['nf code']

        novel_food_obj = NovelFood.objects.create(opinion=opinion, title = r_nf_name, nf_code = r_nf_code)

        r_allergenicities = row['allergenicity']
        if not pd.isna(r_allergenicities):
            allergenicities = r_allergenicities.split(',')
            for allergenicity in allergenicities:
                all_obj = Allergenicity.objects.get(title=allergenicity.strip())
                AllergenicityNovelFood.objects.create(novel_food=novel_food_obj, allergenicity=all_obj)
                

        r_suff_data = row['stability - sufficient stability data']
        if not pd.isna(r_suff_data):
            novel_food_obj.sufficient_data = self.get_yes_no(r_suff_data)

        r_food_matrices = row['stability - food matrices']
        if not pd.isna(r_food_matrices):
            novel_food_obj.food_matrices = self.get_yes_no(r_food_matrices)

        r_instability_concern = row['stability - instability concern']
        if not pd.isna(r_instability_concern):
            novel_food_obj.instability_concerns = self.get_yes_no(r_instability_concern)

        novel_food_obj.save()

        r_shelflife_value = row['stability – shelf life value']
        if not pd.isna(r_shelflife_value):
            novel_food_obj.shelflife_value = r_shelflife_value

        r_shelflife_unit = row['stability – shelf life unit']
        if not pd.isna(r_shelflife_unit):
            novel_food_obj.shelflife_unit = self.get_unit(r_shelflife_unit)

        novel_food_obj.save()

        if row['nutritional – background exposure assessment'] == 'Yes':
            result_msg += 'missing background exposure assessment (components of interest)\n'
        

        r_nutr_disadvantages = row['nutritional – disadvantageous']
        r_nutr_dis_reason = row['nutritional - reason']

        if not pd.isna(r_nutr_disadvantages): #TODO upravit NutriDisadv na OnetoMany
            nutri = NutritionalDisadvantage.objects.create(yes_no = self.get_yes_no(r_nutr_disadvantages), explanation = r_nutr_dis_reason)
            novel_food_obj.nutritional_disadvantage = nutri
            novel_food_obj.save()

        r_protein_digestibility = row['nutritional - protein digestibility']
        if not pd.isna(r_protein_digestibility):
            novel_food_obj.protein_digestibility = self.get_yes_no(r_protein_digestibility)
            novel_food_obj.save()

        if row['nutritional – antinutritional factors'] in ['Yes', 'yes']:
            result_msg += 'missing antinutritional factors\n'


        r_common_names = row['nf - common name']
        if not pd.isna(r_common_names):
            syn_common_name = SynonymType.objects.get(synonym_type = 'common name')
            for common_name in r_common_names.split(','):
                NovelFoodSyn.objects.create(type=syn_common_name, novel_food=novel_food_obj, novel_food_synonym=common_name.strip())

        r_trade_names = row['nf - trade name']
        if not pd.isna(r_trade_names):
            syn_trade_name = SynonymType.objects.get(synonym_type = 'trade name')
            for trade_name in r_trade_names.split(','):
                NovelFoodSyn.objects.create(type=syn_trade_name, novel_food=novel_food_obj, novel_food_synonym=trade_name.strip())

        r_genotox_final = row['genotox_final_outcome']
        if not pd.isna(r_genotox_final):
            novel_food_obj.genotox_final_outcome = GenotoxFinalOutcome.objects.get_or_create(title=r_genotox_final)[0]
        else:
            result_msg += 'genotox final outcome missing \n' #TODO musi byt ale jeste i tox required=True



        return result_msg



    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"])

        print(df.head())
        print(df.columns)

        #delete all Opinion objects
        Opinion.objects.all().delete()

        #delete all question objects
        Question.objects.all().delete()

        #delete all novel foods
        NovelFood.objects.all().delete()

        #delete all nutritional disadvantages
        NutritionalDisadvantage.objects.all().delete()

        
        for row_obj in df.iterrows():
            opinion = self.import_opinion(row_obj[1])
            self.import_novel_food(row_obj[1], opinion)


        
            