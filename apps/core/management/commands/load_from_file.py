import datetime  # TODO - remove if not needed
from datetime import date

import pandas as pd

#Importting models from administrative app:
from administrative.models import (
    Applicant,
    Dossier,
    MandateType,
    Opinion,
    OpinionPanel,
    OpinionQuestion,
    OpinionSciOfficer,
    Panel,
    Question,
    ScientificOfficer,
)
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"])

        # Create mandate types
        #nf_obj, tf_obj, nutrient_obj, nf_dossier_obj, nf_nutrient_obj, nf_extension_obj = self.create_mandate_types()
        mandate_types = self.create_mandate_types()

        for row in df.iterrows():
            # Create dossier with applicant
            dossier_obj = Dossier.objects.get_or_create(number=row[0])
            applicant_name = row[1]["applicant"]
            if not pd.isnull(applicant_name):
                applicant_obj = Applicant.objects.get_or_create(title=applicant_name)
                dossier_obj[0].applicant = applicant_obj[0]
                dossier_obj[0].save()

            # Add scientific officers to the db
            officers_objs = []
            if not pd.isnull(row[1]['scientific_officers']):
                officers = row[1]['scientific_officers'].split(',')
                for officer in officers:
                    names = officer.strip().split(' ')
                    if len(names) == 2: # todo make it more general
                        officers_objs.append(ScientificOfficer.objects.get_or_create(first_name=names[0], last_name=names[1]))
                    elif len(names) == 3:
                        officers_objs.append(ScientificOfficer.objects.get_or_create(first_name=names[0], middle_name=names[1], last_name=names[2]))


            # Create mandate
            mandates = row[1]['mandate_type'].strip().split(',')
            mandate_obj = self.create_mandate(mandates, mandate_types, row[0])

            # Create question
            question_number = row[1]['question_number']
            question_obj = Question.objects.get_or_create(number=question_number, dossier=dossier_obj[0]) #TODO vice mandatu

            if mandate_obj != None:
                question_obj[0].mandate = mandate_obj[0]
                question_obj[0].save()


            publication_date = row[1]['publication_date']
            if '/' in publication_date:
                day, month, year = publication_date.split('/')
                pub_date = date(int(year), int(month), int(day))
            elif '-' in publication_date:
                day, month, year = publication_date.split('-')
                pub_date = date(int(year), int(month), int(day))

            opinion_obj = Opinion.objects.get_or_create(title=row[1]['title'], doi = row[1]['doi'], publication_date=pub_date)

            if not pd.isnull(row[1]['url']): # we have both url and adoption date
                opinion_obj[0].url = row[1]['url']
                opinion_obj[0].save()

            if not pd.isnull(row[1]['adoption_date']):
                day, month, year = row[1]['adoption_date'].split(' ')
                month = datetime.datetime.strptime(month, '%B').month
                adoption_date = date(int(year), month, int(day))
                opinion_obj[0].adoption_date = adoption_date
                opinion_obj[0].save()


            OpinionQuestion.objects.get_or_create(opinion=opinion_obj[0], question=question_obj[0])
            for officer in officers_objs:
                OpinionSciOfficer.objects.get_or_create(opinion=opinion_obj[0], sci_officer=officer[0])


            panels = row[1]['panel'].split(',')
            for panel in panels:
                panel_obj = Panel.objects.get_or_create(title=panel.strip())
                OpinionPanel.objects.get_or_create(opinion=opinion_obj[0], panel=panel_obj[0])


    def create_mandate_types(self):
        nf_obj = MandateType.objects.get_or_create(title='Novel food')
        tf_obj = MandateType.objects.get_or_create(title='Traditional food')
        nutrient_obj = MandateType.objects.get_or_create(title='Nutrient source')

        nf_dossier_obj = MandateType.objects.get_or_create(title='NF - New dossier', mandate_type_parent=nf_obj[0])
        nf_nutrient_obj = MandateType.objects.get_or_create(title='NF - Nutrient source', mandate_type_parent=nf_obj[0])
        nf_extension_obj = MandateType.objects.get_or_create(title='NF - Extension of use', mandate_type_parent=nf_obj[0])
        return nf_obj, tf_obj, nutrient_obj, nf_dossier_obj, nf_nutrient_obj, nf_extension_obj


    def create_mandate(self, mandates, mandate_types, number):

        nf_obj, tf_obj, nutrient_obj, nf_dossier_obj, nf_nutrient_obj, nf_extension_obj = mandate_types
        #mandate_objs = []

        match mandates[0]: # TODO vice mandatu pro jednu question
            case 'TF':
                mandate_obj = MandateType.objects.get_or_create(mandate_type=tf_obj[0], number=number)
            case 'NF: new dossier':
                mandate_obj = MandateType.objects.get_or_create(mandate_type=nf_dossier_obj[0], number=number)
            case 'NF: extension of use':
                mandate_obj = MandateType.objects.get_or_create(mandate_type=nf_extension_obj[0], number=number)
            case 'NF: nutrient source':
                mandate_obj = MandateType.objects.get_or_create(mandate_type=nf_nutrient_obj[0], number=number)
            case 'new dossier?':
                mandate_obj = MandateType.objects.get_or_create(mandate_type=nf_dossier_obj[0], number=number)
            case _:
                mandate_obj = None

        #mandate_objs.append(mandate_obj)
        return mandate_obj
