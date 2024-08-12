import graphene
from graphene_django import DjangoObjectType
from taxonomies.models import TaxonomyNode

from .models import (
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


class OpinionType(DjangoObjectType):
    class Meta:
        model = Opinion
        fields = "__all__"


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"


class PanelType(DjangoObjectType):
    class Meta:
        model = Panel
        fields = "__all__"


class OpinionPanelType(DjangoObjectType):
    class Meta:
        model = OpinionPanel
        fields = "__all__"


class ApplicantType(DjangoObjectType):
    class Meta:
        model = Applicant
        fields = "__all__"


class MandateTypeObjectType(DjangoObjectType):
    class Meta:
        model = MandateType
        fields = "__all__"


class OpinionQuestionType(DjangoObjectType):
    class Meta:
        model = OpinionQuestion
        fields = "__all__"


class ScientificOfficerType(DjangoObjectType):
    class Meta:
        model = ScientificOfficer
        fields = "__all__"


class OpinionSciOfficerType(DjangoObjectType):
    class Meta:
        model = OpinionSciOfficer
        fields = "__all__"


class MandateObjectType(DjangoObjectType):
    class Meta:
        model = Mandate
        fields = "__all__"


class QuestionApplicantType(DjangoObjectType):
    class Meta:
        model = QuestionApplicant
        fields = "__all__"


class TaxonomyNodeType(DjangoObjectType):
    class Meta:
        model = TaxonomyNode
        fields = "__all__"


class Query(graphene.ObjectType):
    opinions = graphene.List(OpinionType)
    opinion = graphene.Field(OpinionType, id=graphene.Int())

    questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, id=graphene.Int())

    panels = graphene.List(PanelType)
    panel = graphene.Field(PanelType, id=graphene.Int())

    applicants = graphene.List(ApplicantType)
    applicant = graphene.Field(ApplicantType, id=graphene.Int())

    mandate_types = graphene.List(MandateTypeObjectType)
    mandate_type = graphene.Field(MandateTypeObjectType, id=graphene.Int())

    scientific_officers = graphene.List(ScientificOfficerType)
    scientific_officer = graphene.Field(ScientificOfficerType, id=graphene.Int())

    mandates = graphene.List(MandateObjectType)
    mandate = graphene.Field(MandateObjectType, id=graphene.Int())

    def resolve_opinions(self, info):
        return Opinion.objects.all()

    def resolve_opinion(self, info, id):
        return Opinion.objects.get(pk=id)

    def resolve_questions(self, info):
        return Question.objects.all()

    def resolve_question(self, info, id):
        return Question.objects.get(pk=id)

    def resolve_panels(self, info):
        return Panel.objects.all()

    def resolve_panel(self, info, id):
        return Panel.objects.get(pk=id)

    def resolve_applicants(self, info):
        return Applicant.objects.all()

    def resolve_applicant(self, info, id):
        return Applicant.objects.get(pk=id)

    def resolve_mandate_types(self, info):
        return MandateType.objects.all()

    def resolve_mandate_type(self, info, id):
        return MandateType.objects.get(pk=id)

    def resolve_scientific_officers(self, info):
        return ScientificOfficer.objects.all()

    def resolve_scientific_officer(self, info, id):
        return ScientificOfficer.objects.get(pk=id)

    def resolve_mandates(self, info):
        return Mandate.objects.all()

    def resolve_mandate(self, info, id):
        return Mandate.objects.get(pk=id)
