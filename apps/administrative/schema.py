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
    name = graphene.String()

    class Meta:
        model = TaxonomyNode
        fields = "__all__"

    def resolve_name(self, info):
        return self.name


class MandateObjectType(DjangoObjectType):
    mandate_type_title = graphene.String()
    mandate_type_definition = graphene.String()
    regulation = graphene.String()

    class Meta:
        model = Mandate
        fields = "__all__"

    def resolve_mandate_type_title(self, info):
        return self.mandate_type.title

    def resolve_mandate_type_definition(self, info):
        return self.mandate_type.definition

    def resolve_regulation(self, info):
        return self.regulation.name if self.regulation else None


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

    questions = graphene.List(QuestionType)

    def resolve_questions(self, info):
        return Question.objects.filter(opinionquestion__opinion=self)


class Query(graphene.ObjectType):
    opinions = graphene.List(OpinionType)

    def resolve_opinions(self, info):
        return Opinion.objects.all()
