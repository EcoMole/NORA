import pandas as pd
from administrative.models import Opinion, OpinionQuestion, Question
from composition.models import Composition, NovelFoodVariant, Parameter, ParameterType
from core.models import Contribution
from django.core.management.base import BaseCommand
from novel_food.models import NovelFood
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "Command that loads NF composition from csv."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def initialize_characterisations(self):
        # Take all novel food variants:
        novel_food_variants = NovelFoodVariant.objects.all()

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

        # For each novel food variant and for each parameter, create a composition for
        # extractor to fill it in.
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
            lower, upper = value.split("-")
            return (
                float(lower.strip()),
                float(upper.strip()),
                TaxonomyNode.objects.get(
                    extended_name="Equal to", taxonomy__code="QUALIFIER"
                ),
            )

        elif any(qualifier in value for qualifier in qualifiers):
            for qualifier in qualifiers:
                if qualifier in value:
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

        try:
            question = Question.objects.get(number=row["question"])
        except Question.DoesNotExist:
            print("Question not found - returning")
            return
        opinion_question = OpinionQuestion.objects.get(question=question)
        try:
            novel_food_obj = NovelFood.objects.get(opinion=opinion_question.opinion)
        except NovelFood.DoesNotExist:
            print("Novel food not found - returning")
            return

        # Get the proper variant
        r_food_form = row["food form"]

        if not pd.isna(r_food_form): # Food form defined
            novel_food_variants = NovelFoodVariant.objects.filter(
                novel_food=novel_food_obj, food_form__title=r_food_form
            )

        else: # Food form not defined - use for all available food forms
            novel_food_variants = NovelFoodVariant.objects.filter(
                novel_food=novel_food_obj
            )

        for variant_obj in novel_food_variants:
            if '(' in row["parameter"]:
                parameter, type = row["parameter"].split('(')
                parameter = parameter.strip()
                type = type.replace(')', '').strip()
                parameter_type_obj, _ = ParameterType.objects.get_or_create(title=type)
                parameter_obj, _ = Parameter.objects.get_or_create(
                    title=parameter, type=parameter_type_obj
                )

            else:
                parameter_obj, _ = Parameter.objects.get_or_create(title=row["parameter"]) 

            composition_obj, _ = Composition.objects.get_or_create(
                nf_variant=variant_obj, parameter=parameter_obj
            )
            if not composition_obj.value and pd.notna(row["value"]): # Add value if available
                value, upper_value, qualifier = self.interpret_value(row["value"])
                composition_obj.value = value
                if upper_value:
                    composition_obj.upper_range_value = upper_value
                composition_obj.qualifier = qualifier
                if row["footnote"]:
                    composition_obj.footnote = row["footnote"]
                composition_obj.save()
            if pd.notna(row['unit']): # Add units if we have them
                unit_obj = TaxonomyNode.objects.get(extended_name=row['unit'], taxonomy__code='UNIT')
                composition_obj.unit = unit_obj
                composition_obj.save()

            if pd.isna(row['type']):
                composition_obj.type = "specification"
            elif row['type'] == 'other':
                composition_obj.type = "other"
            elif row['type'] == 'Characterisation':
                composition_obj.type = 'characterisation'
            composition_obj.save()
            

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], keep_default_na=False, na_values=[""])

        self.initialize_characterisations()

        for _, row in df.iterrows():
            self.add_composition(row)
