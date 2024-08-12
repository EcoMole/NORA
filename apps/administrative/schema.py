import graphene
from graphene_django import DjangoObjectType
from taxonomies.models import TaxonomyNode

from .models import (
    Applicant,
    Mandate,
    MandateType,
    Opinion,
    Panel,
    Question,
    ScientificOfficer,
)


class PanelType(DjangoObjectType):
    class Meta:
        model = Panel
        fields = "__all__"


class ScientificOfficerType(DjangoObjectType):
    class Meta:
        model = ScientificOfficer
        fields = "__all__"


class ApplicantType(DjangoObjectType):
    class Meta:
        model = Applicant
        fields = "__all__"


class MandateTypeObjectType(DjangoObjectType):
    class Meta:
        model = MandateType
        fields = "__all__"


class TaxonomyNodeType(DjangoObjectType):
    class Meta:
        model = TaxonomyNode
        fields = "__all__"


class MandateObjectType(DjangoObjectType):
    class Meta:
        model = Mandate
        fields = "__all__"


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"

    applicants = graphene.List(ApplicantType)
    mandates = graphene.List(MandateObjectType)

    def resolve_applicants(self, info):
        return Applicant.objects.filter(questionapplicant__question=self)

    def resolve_mandates(self, info):
        return Mandate.objects.filter(question=self)


class OpinionType(DjangoObjectType):
    class Meta:
        model = Opinion
        fields = "__all__"

    panels = graphene.List(PanelType)
    sci_officers = graphene.List(ScientificOfficerType)
    questions = graphene.List(QuestionType)

    def resolve_panels(self, info):
        return Panel.objects.filter(opinionpanel__opinion=self)

    def resolve_sci_officers(self, info):
        return ScientificOfficer.objects.filter(opinionsciofficer__opinion=self)

    def resolve_questions(self, info):
        return Question.objects.filter(opinionquestion__opinion=self)


class Query(graphene.ObjectType):
    opinions = graphene.List(OpinionType)

    def resolve_opinions(self, info):
        return Opinion.objects.all()
