import pandas as pd
from administrative.models import Opinion, OpinionQuestion, Question
from composition.models import Composition, NovelFoodVariant, Parameter, ParameterType
from core.models import Contribution
from django.core.management.base import BaseCommand
from novel_food.models import NovelFood
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "Script to load organism identities of Novel Foods."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def annotate(self, opinion, text):
        contribution = Contribution.objects.get(opinion=opinion)
        contribution.remarks = contribution.remarks + text
        contribution.save()

    def initialize_characterisations(self):
        # Take all novel food variants:
        novel_food_variants = NovelFoodVariant.objects.all()

        parameters = [
            "Carbohydrates",
            "Fat",
            "Protein",
            "Minerals",
            "Moisture",
            "Vitamins",
        ]

        # create all 6 parameters
        carbs = Parameter.objects.create(title="Carbohydrates")
        fat = Parameter.objects.create(title="Fat")
        protein = Parameter.objects.create(title="Protein")
        minerals = Parameter.objects.create(title="Minerals")
        moisture = Parameter.objects.create(title="Moisture")
        vitamins = Parameter.objects.create(title="Vitamins")

        parameters_objs = [carbs, fat, protein, minerals, moisture, vitamins]

        percent_unit_obj = TaxonomyNode.objects.get(
            extended_name="Percent", taxonomy__code="UNIT"
        )

        # For each novel food variant and for each parameter, create a composition
        for nf_variant in novel_food_variants:
            for parameter in parameters_objs:
                Composition.objects.create(
                    nf_variant=nf_variant,
                    parameter=parameter,
                    unit=percent_unit_obj,
                    type="characterisation",
                )

    def interpret_value(self, value):
        qualifiers = ["<=", ">=", "<", ">"]
        print(f"value: {value}")

        qualifier_vocab_map = {
            "<": "Less than",
            "<=": "Less than or equal",
            ">": "Greater than",
            ">=": "Greater than or equal",
            "=": "Equal to",
        }

        if (
            "-" in value
        ):  # We know its range, we want to get lower value and upper value
            print("range")
            lower, upper = value.split("-")
            return (
                float(lower.strip()),
                float(upper.strip()),
                TaxonomyNode.objects.get(
                    extended_name="Equal to", taxonomy__code="QUALIFIER"
                ),
            )

        elif any(qualifier in value for qualifier in qualifiers):
            print("qualifier found")
            for qualifier in qualifiers:
                if qualifier in value:
                    print(f"matched qualifier {qualifier}")
                    return (
                        float(value.split(qualifier)[1].strip()),
                        None,
                        TaxonomyNode.objects.get(
                            extended_name=qualifier_vocab_map[qualifier],
                            taxonomy__code="QUALIFIER",
                        ),
                    )

        else:
            return (
                float(value),
                None,
                TaxonomyNode.objects.get(
                    extended_name="Equal to", taxonomy__code="QUALIFIER"
                ),
            )

    def add_composition(self, row):
        print(f"Adding composition.")

        r_question_number = row["question"]
        try:
            question = Question.objects.get(number=r_question_number)
        except Question.DoesNotExist:
            print("Question not found - returning")
            return
        opinion_question = OpinionQuestion.objects.get(question=question)
        opinion = opinion_question.opinion
        try:
            novel_food_obj = NovelFood.objects.get(opinion=opinion)
        except NovelFood.DoesNotExist:
            print("Novel food not found - returning")
            return

        # Get the proper variant
        r_food_form = row["food form"]

        if not pd.isna(r_food_form):
            print("Food form defined: ", r_food_form)
            novel_food_variants = NovelFoodVariant.objects.filter(
                novel_food=novel_food_obj, food_form__title=r_food_form
            )

        else:
            print("Food form not defined")
            novel_food_variants = NovelFoodVariant.objects.filter(
                novel_food=novel_food_obj
            )

        for variant_obj in novel_food_variants:
            parameter, _ = Parameter.objects.get_or_create(
                title=row["parameter"]
            )  # TODO zpracovat parameter
            composition_obj, _ = Composition.objects.get_or_create(
                nf_variant=variant_obj, parameter=parameter
            )
            if not composition_obj.value and pd.notna(row["value"]):
                value, upper_value, qualifier = self.interpret_value(row["value"])
                composition_obj.value = value
                if upper_value:
                    composition_obj.upper_range_value = upper_value
                composition_obj.qualifier = qualifier
                if row["footnote"]:
                    composition_obj.footnote = row["footnote"]
                composition_obj.save()

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])
        Composition.objects.all().delete()
        Parameter.objects.all().delete()

        self.initialize_characterisations()

        for index, row in df.iterrows():
            self.add_composition(row)
