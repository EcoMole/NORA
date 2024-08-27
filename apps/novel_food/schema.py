import graphene
from administrative.models import Panel, Question, ScientificOfficer
from administrative.schema import (  # noqa
    OpinionType,
    PanelType,
    QuestionType,
    ScientificOfficerType,
)
from graphene_django.types import DjangoObjectType

from .models import NovelFood


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

    class Meta:
        model = NovelFood
        fields = "__all__"

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


class Query(graphene.ObjectType):
    novel_foods = graphene.List(NovelFoodType)

    def resolve_novel_foods(self, info):
        return NovelFood.objects.all()
