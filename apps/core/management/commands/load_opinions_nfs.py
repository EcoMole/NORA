import datetime
from datetime import date

import pandas as pd
from administrative.models import (
    Applicant,
    Mandate,
    MandateType,
    Opinion,
    OpinionPanel,
    OpinionQuestion,
    OpinionSciOfficer,
    Panel,
    Question,
    QuestionApplicant,
    ScientificOfficer,
)
from core.models import Contribution, User
from django.core.management.base import BaseCommand, CommandError
from novel_food.models import (
    Allergenicity,
    AllergenicityNovelFood,
    FoodCategory,
    FoodCategoryNovelFood,
    GenotoxFinalOutcome,
    NovelFood,
    NovelFoodSyn,
    SynonymType,
    NovelFoodCategory,
    NovelFoodCategoryNovelFood
)
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "Load opinions and novel foods"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def import_opinion(self, row):
        final_msg = '\nOpinion:\n'
        KN = User.objects.get(username="klara@ecomole.com")
        MF = User.objects.get(username="marketa@mit.edu")
        LC = User.objects.get(username="lucie@ecomole.com")

        if 'statement' in row['title'].lower():
            doc_type = TaxonomyNode.objects.get(extended_name='EFSA statement', taxonomy__code='REF_TYPE')
        elif 'technical report' in row['title'].lower():
            doc_type = TaxonomyNode.objects.get(extended_name='EFSA technical report', taxonomy__code='REF_TYPE')
        else:
            doc_type = TaxonomyNode.objects.get(extended_name='EFSA opinion', taxonomy__code='REF_TYPE')

        print(f'importing opinion {row["title"]}')

        r_title = row["title"]
        r_doi = row["doi"]
        if not pd.isnull(row["url"]):
            r_url = row["url"]
        else:
            r_url = None

        opinion_obj = Opinion.objects.create(title=r_title, doi=r_doi, url=r_url, document_type=doc_type)

        r_publication_date = row["publication date"]
        if not pd.isnull(r_publication_date):
            day, month, year = r_publication_date.split("-")
            pub_date = date(int(year), int(month), int(day))
            opinion_obj.publication_date = pub_date
            opinion_obj.save()

        r_adoption_date = row["adoption date"]
        if not pd.isnull(r_adoption_date):
            day, month, year = r_adoption_date.split(" ")
            month = datetime.datetime.strptime(month, "%B").month
            adopt_date = date(int(year), month, int(day))

            opinion_obj.adoption_date = adopt_date
            opinion_obj.save()

        person = row["person"]

        if pd.isna(row['status']):
            state = ''
        else:
            state = f"""Excel : {row['status']}\n"""
        contribution = None
        if person == "KN":
            contribution = Contribution.objects.create(opinion=opinion_obj, user=KN, remarks=state, status='working_on')
        elif person == "MF":
            contribution = Contribution.objects.create(opinion=opinion_obj, user=MF, remarks=state, status='working_on')
        elif person == "LČ":
            contribution = Contribution.objects.create(opinion=opinion_obj, user=LC, remarks=state, status='working_on')

        # import panels
        panels = row["panel"].split(",")
        for panel in panels:
            panel_obj = Panel.objects.get(title=panel.strip())
            OpinionPanel.objects.create(opinion=opinion_obj, panel=panel_obj)

        # import questions
        r_questions = row["question"]
        r_mandates = row["mandate"]
        r_applicant = row["applicant"]

        questions = r_questions.split(",")
        for question in questions:
            question_obj = Question.objects.create(number=question.strip())
            if not pd.isna(r_applicant):
                applicant_obj, _ = Applicant.objects.get_or_create(title=r_applicant)
                QuestionApplicant.objects.create(question=question_obj, applicant=applicant_obj)

            OpinionQuestion.objects.create(opinion=opinion_obj, question=question_obj)

            if not pd.isna(r_mandates):
                for mandate in r_mandates.split(","):
                    if '?' in mandate:
                        final_msg += 'Check mandate type.\n'
                        mandate = mandate.replace('?', '')
                    mandate_type_obj = MandateType.objects.get(title=mandate.strip())
                    mandate_obj = Mandate.objects.create(question=question_obj, mandate_type=mandate_type_obj)
                    if not pd.isna(row['regulation']):
                        if '2015/2283' in row['regulation']:
                            mandate_obj.regulation = TaxonomyNode.objects.get(short_name='Regulation (EC) No 2015/2283 Article 3', taxonomy__code='LEGREF')
                        if '258/93' in row['regulation']:
                            mandate_obj.regulation = TaxonomyNode.objects.get(code="N124A", taxonomy__code='LEGREF')
                        if '.' in row['regulation']:
                            final_msg += 'Check for missing regulations.\n'
                    mandate_obj.save()  

        if contribution:
            contribution.remarks += final_msg
            contribution.save()

        # Import scientific officers
        r_so = row["so"]
        if not pd.isna(r_so):
            sos = r_so.split(",")
            for so in sos:
                so_first_name, so_last_name = so.strip().split(" ", maxsplit=1)
                so_obj = ScientificOfficer.objects.get_or_create(
                    first_name=so_first_name, last_name=so_last_name
                )
                OpinionSciOfficer.objects.create(
                    opinion=opinion_obj, sci_officer=so_obj[0]
                )

        return opinion_obj

    def get_yes_no(self, word):
        yesno = Taxonomy.objects.get(code="YESNO")
        yes = TaxonomyNode.objects.get(taxonomy=yesno, code="Y")
        no = TaxonomyNode.objects.get(taxonomy=yesno, code="N")
        unknown = TaxonomyNode.objects.get(taxonomy=yesno, code="U")

        if word == "Yes" or word == "yes":
            return yes

        if word == "No" or word == "no":
            return no

        if (
            word == "Not specified"
            or word == "not specified"
            or word == "N/A"
            or word == "Unknown"
        ):
            return unknown

    def get_unit(self, word):
        unit = Taxonomy.objects.get(code="UNIT")
        year = TaxonomyNode.objects.get(
            taxonomy=unit, code="G207A", extended_name="Year"
        )
        month = TaxonomyNode.objects.get(
            taxonomy=unit, code="G206A", extended_name="Month"
        )
        day = TaxonomyNode.objects.get(taxonomy=unit, code="G134A", extended_name="Day")

        if word in ["month", "Month", "month(s)", "Month(s)"]:
            return month

        if word in ["year", "Year", "year(s)", "Year(s)"]:
            return year

        if word in ["day", "Day", "days", "Days"]:
            return day

    def import_novel_food(self, row, opinion):
        result_msg = "Novel food: \n"
        r_nf_name = row["nf name"]
        if pd.isna(row["nf code"]):
            r_nf_code = None
        else:
            r_nf_code = row["nf code"]

        novel_food_obj = NovelFood.objects.create(
            opinion=opinion, title=r_nf_name, nf_code=r_nf_code
        )

        r_allergenicities = row["allergenicity"]
        if not pd.isna(r_allergenicities):
            allergenicities = r_allergenicities.split(",")
            for allergenicity in allergenicities:
                all_obj = Allergenicity.objects.get(title=allergenicity.strip())
                AllergenicityNovelFood.objects.create(
                    novel_food=novel_food_obj, allergenicity=all_obj
                )

        r_suff_data = row["stability - sufficient stability data"]
        if not pd.isna(r_suff_data):
            novel_food_obj.sufficient_data = self.get_yes_no(r_suff_data)

        r_food_matrices = row["stability - food matrices"]
        if not pd.isna(r_food_matrices):
            novel_food_obj.food_matrices = self.get_yes_no(r_food_matrices)

        r_instability_concern = row["stability - instability concern"]
        if not pd.isna(r_instability_concern):
            novel_food_obj.instability_concerns = self.get_yes_no(r_instability_concern)

        novel_food_obj.save()

        r_shelflife_value = row["stability – shelf life value"]
        if not pd.isna(r_shelflife_value) and r_shelflife_value != "N/A":
            novel_food_obj.shelflife_value = r_shelflife_value

        r_shelflife_unit = row["stability – shelf life unit"]
        if not pd.isna(r_shelflife_unit) and r_shelflife_unit != "N/A":
            novel_food_obj.shelflife_unit = self.get_unit(r_shelflife_unit)

        novel_food_obj.save()

        if row["nutritional – background exposure assessment"] == "Yes":
            result_msg += "Background exposure assessment (components of interest) not imported.\n"

        r_nutr_disadvantages = row["nutritional – disadvantageous"]
        novel_food_obj.has_nutri_disadvantage = self.get_yes_no(r_nutr_disadvantages)

        r_protein_digestibility = row["nutritional - protein digestibility"]
        if not pd.isna(r_protein_digestibility):
            novel_food_obj.protein_digestibility = self.get_yes_no(
                r_protein_digestibility
            )
            novel_food_obj.save()

        novel_food_obj.antinutritional_factors = self.get_yes_no(
            row["nutritional – antinutritional factors"]
        )
        novel_food_obj.save()

        r_category = row["category"]
        if not pd.isna(r_category):
            categories = r_category.split(',')
            for category in categories:
                regulation, category = category.split(":") #find category which includes these two as substring:
                category_obj = NovelFoodCategory.objects.get(title__contains=category.strip(), regulation__extended_name__contains=regulation.strip())
                # assign category to novel food
                NovelFoodCategoryNovelFood.objects.create(novel_food=novel_food_obj, novel_food_category=category_obj)


        r_common_names = row["nf - common name"]
        if not pd.isna(r_common_names):
            syn_common_name = SynonymType.objects.get(title="common name")
            for common_name in r_common_names.split(","):
                NovelFoodSyn.objects.create(
                    syn_type=syn_common_name,
                    novel_food=novel_food_obj,
                    title=common_name.strip(),
                )

        r_trade_names = row["nf - trade name"]
        if not pd.isna(r_trade_names):
            syn_trade_name = SynonymType.objects.get(title="trade name")
            for trade_name in r_trade_names.split(","):
                NovelFoodSyn.objects.create(
                    syn_type=syn_trade_name,
                    novel_food=novel_food_obj,
                    title=trade_name.strip(),
                )

        r_outcome = row["outcome"]
        r_outcome_remarks = row["outcome remarks"]
        if not pd.isna(r_outcome):
            novel_food_obj.outcome = r_outcome.lower().replace(" ", "_")
        if not pd.isna(r_outcome_remarks):
            novel_food_obj.outcome_remarks = r_outcome_remarks
        novel_food_obj.save()

        r_endocrine = row["endocrine disrupting properties"]
        if not pd.isna(r_endocrine):
            novel_food_obj.endocrine_disrupt_prop = self.get_yes_no(r_endocrine)

        if row["HBGV"] in ["yes", "Yes"]:
            result_msg += "HBGV not imported.\n"

        if row["substances of concern"] in ["yes", "Yes"]:
            result_msg += "Substances of concern not imported.\n"

        r_specific_toxicity = row["specific toxicity – type"]
        toxicity_vocab = Taxonomy.objects.get(code="TOXICITY")
        if not pd.isna(r_specific_toxicity):
            try:
                toxicity_node = TaxonomyNode.objects.get(
                    taxonomy=toxicity_vocab, extended_name=r_specific_toxicity.upper()
                )
            except:
                print(f"TOXICITY node {r_specific_toxicity} not found, creating.")
                toxicity_node = TaxonomyNode.objects.create(
                    taxonomy=toxicity_vocab,
                    extended_name=r_specific_toxicity.upper(),
                    code="NORA",
                )

            novel_food_obj.specific_toxicity = toxicity_node
            novel_food_obj.save()

        else:
            toxicity_node = TaxonomyNode.objects.get(
                taxonomy=toxicity_vocab, extended_name="NONE"
            )
            novel_food_obj.specific_toxicity = toxicity_node
            novel_food_obj.save()

        r_food_category = row["food category"]
        if not pd.isna(r_food_category):
            categories = r_food_category.split(",")
            for category in categories:
                food_category_obj = FoodCategory.objects.get(title=category.strip())
                FoodCategoryNovelFood.objects.create(
                    novel_food=novel_food_obj, food_category=food_category_obj
                )

        r_genotox_outcome = row["genotox outcome"]
        r_toxicity_required = row["toxicology required"]

        if not pd.isna(r_genotox_outcome):
            genotox_outcome_obj = GenotoxFinalOutcome.objects.get_or_create(
                title=r_genotox_outcome
            )[0]
            novel_food_obj.genotox_final_outcome = genotox_outcome_obj
            novel_food_obj.save()

        if pd.isna(r_toxicity_required):
            result_msg += "Toxicology required (Y/N) missing.\n"
        else:
            novel_food_obj.tox_study_required = r_toxicity_required
            novel_food_obj.save()

        # Find contribution for this opinioon:
        try:
            contribution = Contribution.objects.get(opinion=opinion)
            contribution.remarks = contribution.remarks + result_msg
            contribution.save()
        except:
            pass

        return result_msg

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])

        print(df.head())
        print(df.columns)

        # delete all Opinion objects
        Opinion.objects.all().delete()

        # delete all question objects
        Question.objects.all().delete()

        # delete all novel foods
        NovelFood.objects.all().delete()

        for row_obj in df.iterrows():
            opinion = self.import_opinion(row_obj[1])
            self.import_novel_food(row_obj[1], opinion)