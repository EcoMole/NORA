from administrative.models import MandateType, Panel
from composition.models import FoodForm, ParameterType, ProposedUseType
from django.core.management.base import BaseCommand
from novel_food.models import Allergenicity, Category, FoodCategory, SynonymType
from taxonomies.models import Taxonomy, TaxonomyNode


class Command(BaseCommand):
    help = "command to initialize options in the database - panels, categories, mandates, allergenicity etc."

    def create_panels(self):
        for name in ["EFSA", "NDA", "GMO"]:
            Panel.objects.get_or_create(panel=name)

    def create_novel_food_categories(self):
        legref, _ = Taxonomy.objects.get_or_create(code="LEGREF")
        # pridat do slovniku Comission Recommendation 97/618/EC
        # pridat do slovniku: Regulation (EC) No 2015/2283 Article 3

        article_3 = TaxonomyNode.objects.get_or_create(
            code="NORA",
            taxonomy=legref,
            short_name="Regulation (EC) No 2015/2283 Article 3",
            extended_name="Regulation (EU) 2015/2283 of the European Parliament and of the Council of 25 November 2015 on novel foods,\
            amending Regulation (EU) No 1169/2011 of the European Parliament and of the Council and repealing Regulation (EC) No 258/97 \
            of the European Parliament and of the Council and Commission Regulation (EC) No 1852/2001 Article 3£https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=OJ:JOL_2015_327_R_0001",
        )

        recommendation = TaxonomyNode.objects.get_or_create(
            code="NORA",
            taxonomy=legref,
            short_name="Commission Recommendation 97/618/EC",
        )

        regulation_258_97 = TaxonomyNode.objects.get_or_create(
            taxonomy=legref, code="N124A"
        )

        categories_2015_2283 = {
            "Modified molecular structure": "food with a new or intentionally modified molecular structure, where that structure was not used as, or in, a food within the Union before 15 May 1997;",
            "From microorganisms, fungi or algae": "food consisting of, isolated from or produced from microorganisms, fungi or algae;",
            "From plants or their parts": "food consisting of, isolated from or produced from plants or their parts, except when the food has a history of safe food use within the Union and is consisting of,\
            isolated from or produced from a plant or a variety of the same species obtained by: — traditional propagating practices which have been used for food production within the Union before 15 May 1997; or \
            — non-traditional propagating practices which have not been used for food production within the Union before 15 May 1997, where those practices do not give rise to significant changes in the composition or \
            structure of the food affecting its nutritional value, metabolism or level of undesirable substances;",
            "From animals or their parts": "food consisting of, isolated from or produced from animals or their parts, except for animals obtained by\
                                        traditional breeding practices which have been used for food production within the Union before 15 May 1997\
                                        and the food from those animals has a history of safe food use within the Union;",
            "Cell culture or tissue culture": "food consisting of, isolated from or produced from cell culture or tissue culture derived from animals, plants, micro-organisms, fungi or algae;",
            "New production process": "food resulting from a production process not used for food production within the Union before 15 May 1997,\
                                    which gives rise to significant changes in the composition or structure of a food, affecting its nutritional value,\
                                    metabolism or level of undesirable substances;",
            "Vitamins, minerals and other substances ": "vitamins, minerals and other substances used in accordance with Directive 2002/46/EC, Regulation (EC)\
                                         No 1925/2006 or Regulation (EU) No 609/2013, where: — a production process not used for food production within the Union before 15 May 1997 has been applied\
                                        as referred to in point (a) (vii) of this paragraph; or — they contain or consist of engineered nanomaterials as defined in point (f) of this paragraph;",
            "Engineered nanomaterials": "food consisting of engineered nanomaterials as defined in point (f) of this paragraph;",
            "Exclusive use in food supplements prior 1997": "food used exclusively in food supplements within the Union before 15 May 1997, where it is intended to be\
                                                    used in foods other than food supplements as defined in point (a) of Article 2 of Directive 2002/46/EC;",
        }

        for key, value in categories_2015_2283.items():
            Category.objects.get_or_create(
                title=key, definition=value, regulation=article_3[0]
            )

        categories_97_618 = {
            "1.1 - Chemicals": "1.1 Pure chemicals or simple mixtures from non-GM sources -  the source of the NF has a history of food use in the Community",
            "1.2 - Chamicals": "1.2 Pure chemicals or simple mixtures from non-GM sources - the source of the NF has no history of food use in the Community",
            "2.1 - Complex NF": "2.1 Complex NF from non-GM source - the source of the NF has a history of food use in the Community",
            "2.2 - Complex NF": "2.2 Complex NF from non-GM source - the source of the NF has no history of food use in the Community",
            "3.1 - Plants": "3.1 GM plants and their products - the host plant used for the genetic modification has a history of use as food or as a source of food in\
                                                                                the Community under comparable conditions of preparation and intake ;",
            "3.2 - Plants": "3.2 GM plants and their products - the host plant used for the genetic modification has no history of use as food or as a source of food in\
                                                the Community under comparable conditions of preparation and intake .",
            "4.1 - Animals": "4.1 GM animals and their products - the host animal used for the genetic modification has a history of use as food or as a source of food in\
                                                    the Community under comparable conditions of preparation and intake ;",
            "4.2 - Animals": "4.2 GM animals and their products - the host animal used for the genetic modification has no history of use as food or as a source of food\
                                                    in the Community under comparable conditions of preparation and intake.",
            "5.1 - Microogranisms": "5.1 GM microorganisms and their products - the host microorganism used for the genetic modification has a history of use as food or as a source of\
                                                                food in the Community under comparable conditions of preparation and intake;",
            "5.2 - Micoorganisms": "5.2 GM microorganisms and their products - the host microorganism used for the genetic modification has no history of use as food or as a source\
                                                            of food in the Community under comparable conditions of preparation and intake.",
            "6 - Novel production process": "6 Foods produced using a novel process",
        }

        for key, value in categories_97_618.items():
            Category.objects.get_or_create(
                title=key, definition=value, regulation=recommendation[0]
            )

        categories_258_97 = {
            "a) containing GMO": "a) foods and food ingredients containing or consisting of genetically modified organisms within the meaning of Directive 90 /220 /EEC;",
            "b) producted from GMO, non GMO": "b) Non GMO - foods and food ingredients producted from, but not containing, genetically modified organisms;",
            "c) modified molecular structure": "c) Modified molecular structure - foods and food ingredients with a new or intentionally modified primary molecular structure;",
            "d) microoganisms, fungi, algae": "d)foods and food ingredients consisting of or isolated from micro-organisms, fungi or algae;",
            "e) from plants or animals": "e) foods and food ingredients consisting of or isolated from plants and food ingredients isolated from animals, except for foods and food ingredients\
                                        obtained by traditional propagating or breeding prac­tices and having a history of safe food use;",
            "f) new production process": "f) foods and food ingredients to which has been applied a production process not currently used, where that process gives rise to significant changes in the com­\
                        position or structure of the foods or food ingredients which affect their nutritional value, metabolism or level of undesirable substances .",
        }

        for key, value in categories_258_97.items():
            Category.objects.get_or_create(
                title=key, definition=value, regulation=regulation_258_97[0]
            )

    def create_mandates(self):
        MandateType.objects.get_or_create(title="traditional_food")
        MandateType.objects.get_or_create(title="nutrient_source")

        novel_food = MandateType.objects.get_or_create(title="novel_food")

        # Create children for novel food
        MandateType.objects.get_or_create(
            title="new_dossier", mandate_parent=novel_food[0]
        )
        MandateType.objects.get_or_create(
            title="extension_of_use", mandate_parent=novel_food[0]
        )
        MandateType.objects.get_or_create(
            title="nutrient_source", mandate_parent=novel_food[0]
        )

    def create_allergenicity(self):
        options = [
            "Low",
            "Unlikely",
            "Possible",
            "Possible cross-reactivity",
            "Possible primary sensitization",
            "Certainty",
            "N/A",
        ]
        for option in options:
            Allergenicity.objects.get_or_create(title=option)

    def create_food_categories(self):
        options = ["FoodEx", "FAIM"]
        for option in options:
            FoodCategory.objects.get_or_create(title=option)

    def create_food_forms(self):
        options = [
            "powder",
            "paste",
            "whole frozen",
            "whole dried",
            "juice",
            "pulp",
            "extract",
            "decorticated grain",
        ]
        for option in options:
            FoodForm.objects.get_or_create(title=option)

    def create_synonym_types(self):
        options = ["synonym", "common name", "trade name"]
        for option in options:
            SynonymType.objects.get_or_create(synonym_type=option)

    def create_parameter_types(self):
        options = [
            "Microbiological",
            "Mycotoxins",
            "Heavy metals",
            "Minerals",
            "Hoodigosides",
            "Vitamins",
        ]
        for option in options:
            ParameterType.objects.get_or_create(title=option)

    def create_proposed_use_types(self):
        options = [
            "whole_foods",
            "food_ingredients",
            "food_supplements",
            "infant_follow_on_formula",
            "special_medical_purpose",
            "total_diet_replacement",
        ]
        for option in options:
            ProposedUseType.objects.get_or_create(title=option)

    def handle(self, *args, **options):
        self.create_panels()
        self.create_allergenicity()
        self.create_food_categories()
        self.create_food_forms()
        self.create_synonym_types()
        self.create_parameter_types()
        self.create_proposed_use_types()
        self.create_novel_food_categories()
        self.create_mandates()
