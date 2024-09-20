import graphene
from administrative.models import Panel, Question, ScientificOfficer
from administrative.schema import (  # noqa
    OpinionType,
    PanelType,
    QuestionType,
    ScientificOfficerType,
)
from graphene_django.types import DjangoObjectType
from studies.models import ADME, Endpointstudy, Genotox
from studies.schema import ADMEType, EndpointStudyType, GenotoxType

from .models import Allergenicity, FoodCategory, NovelFood, NovelFoodCategory


class NovelFoodCategoryType(DjangoObjectType):
    regulation = graphene.String()

    class Meta:
        model = NovelFoodCategory
        fields = "__all__"

    def resolve_regulation(self, info):
        return self.regulation.name if self.regulation else None


class FoodCategoryType(DjangoObjectType):
    class Meta:
        model = FoodCategory
        fields = "__all__"


class AllergenicityType(DjangoObjectType):
    class Meta:
        model = Allergenicity
        fields = "__all__"


class NovelFoodType(DjangoObjectType):
    opinion_document_type = graphene.String()
    opinion_title = graphene.String()
    opinion_doi = graphene.String()
    opinion_url = graphene.String()
    opinion_publication_date = graphene.Date()
    opinion_adoption_date = graphene.Date()
    panels = graphene.List(PanelType)
    sci_officers = graphene.List(ScientificOfficerType)
    questions = graphene.List(QuestionType)
    genotox_final_outcome = graphene.String()
    protein_digestibility = graphene.String()
    antinutritional_factors = graphene.String()
    has_nutri_disadvantage = graphene.String()
    sufficient_data = graphene.String()
    food_matrices = graphene.String()
    instability_concerns = graphene.String()
    shelflife_unit = graphene.String()
    endocrine_disrupt_prop = graphene.String()
    vocab_id = graphene.String()
    allergenicities = graphene.List(AllergenicityType)
    food_categories = graphene.List(FoodCategoryType)
    novel_food_categories = graphene.List(NovelFoodCategoryType)
    admes = graphene.List(ADMEType)
    genotoxes = graphene.List(GenotoxType)
    endpointstudies = graphene.List(EndpointStudyType)
    novel_food_id = graphene.Int()

    class Meta:
        model = NovelFood
        fields = "__all__"

    def resolve_novel_food_id(self, info):
        return self.id

    def resolve_opinion_document_type(self, info):
        return self.opinion.document_type.name if self.opinion.document_type else None

    def resolve_opinion_title(self, info):
        return self.opinion.title

    def resolve_opinion_doi(self, info):
        return self.opinion.doi

    def resolve_opinion_url(self, info):
        return self.opinion.url

    def resolve_opinion_publication_date(self, info):
        return self.opinion.publication_date

    def resolve_opinion_adoption_date(self, info):
        return self.opinion.adoption_date

    def resolve_panels(self, info):
        return Panel.objects.filter(opinionpanel__opinion__opinion_novel_foods=self)

    def resolve_sci_officers(self, info):
        return ScientificOfficer.objects.filter(opinionsciofficer__opinion=self.opinion)

    def resolve_questions(self, info):
        return Question.objects.filter(opinionquestion__opinion=self.opinion)

    def resolve_genotox_final_outcome(self, info):
        return self.genotox_final_outcome.title if self.genotox_final_outcome else None

    def resolve_protein_digestibility(self, info):
        return self.protein_digestibility.name if self.protein_digestibility else None

    def resolve_antinutritional_factors(self, info):
        return (
            self.antinutritional_factors.name if self.antinutritional_factors else None
        )

    def resolve_has_nutri_disadvantage(self, info):
        return self.has_nutri_disadvantage.name if self.has_nutri_disadvantage else None

    def resolve_sufficient_data(self, info):
        return self.sufficient_data.name if self.sufficient_data else None

    def resolve_food_matrices(self, info):
        return self.food_matrices.name if self.food_matrices else None

    def resolve_instability_concerns(self, info):
        return self.instability_concerns.name if self.instability_concerns else None

    def resolve_shelflife_unit(self, info):
        return self.shelflife_unit.name if self.shelflife_unit else None

    def resolve_endocrine_disrupt_prop(self, info):
        return self.endocrine_disrupt_prop.name if self.endocrine_disrupt_prop else None

    def resolve_vocab_id(self, info):
        return self.vocab_id.name if self.vocab_id else None

    def resolve_allergenicities(self, info):
        return Allergenicity.objects.filter(allergenicitynovelfood__novel_food=self)

    def resolve_food_categories(self, info):
        return FoodCategory.objects.filter(foodcategorynovelfood__novel_food=self)

    def resolve_novel_food_categories(self, info):
        return NovelFoodCategory.objects.filter(
            novelfoodcategorynovelfood__novel_food=self
        )

    def resolve_admes(self, info):
        return ADME.objects.filter(novel_food=self)

    def resolve_genotoxes(self, info):
        return Genotox.objects.filter(novel_food=self)

    def resolve_endpointstudies(self, info):
        return Endpointstudy.objects.filter(novel_food=self)
