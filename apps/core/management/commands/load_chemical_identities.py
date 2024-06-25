from django.core.management.base import BaseCommand
import pandas as pd
from taxonomies.models import Taxonomy, TaxonomyNode
from novel_food.models import NovelFood, Chemical, NovelFoodChemical, ChemDescriptor, ChemicalSyn, SynonymType
from administrative.models import Question, OpinionQuestion, Opinion



class Command(BaseCommand):
    help = "Script for loading chemical identities of Novel Foods."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)


    def add_chemical_identity(self, row):

        r_question_number = row["question"]
        question = Question.objects.get(number=r_question_number)
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        novel_food = NovelFood.objects.get(opinion=opinion)

        custom = False
        try: #Try to get the chemical
            param_vocab = Taxonomy.objects.get(code='PARAM')
            chemical_vocab = TaxonomyNode.objects.get(taxonomy=param_vocab, extended_name=row['common name'])
            print(f'Found chemical {row["common name"]}')
        except TaxonomyNode.DoesNotExist:
            print(f"Could not find chemical {row['common name']}, creating")
            chemical_vocab = TaxonomyNode.objects.create(taxonomy=param_vocab, extended_name=row['common name'], code='NORA')
            custom = True

        # Create the chemical
        chemical = Chemical.objects.create(vocab_id = chemical_vocab)

        NovelFoodChemical.objects.create(novel_food=novel_food, chemical=chemical)

        if custom: # We have custom chemical -> we want to add IUPAC etc.
            if not pd.isnull(row['IUPAC']):
                ChemDescriptor.objects.create(chemical=chemical, type="IUPAC", value=row['IUPAC'])
            if not pd.isnull(row['CAS']):
                ChemDescriptor.objects.create(chemical=chemical, type="CAS", value=row['CAS'])
            if not pd.isnull(row['SMILES']):
                ChemDescriptor.objects.create(chemical=chemical, type="SMILES_NOTATION", value=row['SMILES'])
            if not pd.isnull(row['molecular formula']):
                ChemDescriptor.objects.create(chemical=chemical, type="MOLECULAR_FORMULA", value=row['molecular formula'])
            if not pd.isnull(row['InChi']):
                ChemDescriptor.objects.create(chemical=chemical, type="INCHI", value=row['InChi'])

        chemical.save()

        # add synonyms
        common_name_synonym_type = SynonymType.objects.get(synonym_type='common name')
        r_synonyms = row['other names']
        if not pd.isnull(r_synonyms):
            synonyms = r_synonyms.split(',')
            for synonym in synonyms:
                if synonym:
                    ChemicalSyn.objects.create(chemical=chemical, synonym=synonym, type=common_name_synonym_type)


    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[''])
        Chemical.objects.all().delete()
        ChemDescriptor.objects.all().delete()
        NovelFoodChemical.objects.all().delete()
        for index, row in df.iterrows():
            self.add_chemical_identity(row)