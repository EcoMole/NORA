import graphene
from graphene_django.types import DjangoObjectType

# from novel_food.models import NovelFood
from studies.models import (  # FinalOutcomePopulation,; StudySource,
    ADME,
    Endpoint,
    Endpointstudy,
    FinalOutcome,
    Genotox,
    InvestigationType,
)
from taxonomies.models import Population
from taxonomies.schema import PopulationType


class InvestigationTypeObjectType(DjangoObjectType):
    class Meta:
        model = InvestigationType
        fields = "__all__"


class ADMEType(DjangoObjectType):
    test_type = graphene.String()
    guideline = graphene.String()
    guideline_qualifier = graphene.String()
    study_source = graphene.String()
    investigation_types = graphene.List(InvestigationTypeObjectType)

    class Meta:
        model = ADME
        fields = "__all__"

    def resolve_test_type(self, info):
        return self.test_type.name if self.test_type else None

    def resolve_guideline(self, info):
        return self.guideline.name if self.guideline else None

    def resolve_guideline_qualifier(self, info):
        return self.guideline_qualifier.title if self.guideline_qualifier else None

    def resolve_study_source(self, info):
        return self.study_source.title if self.study_source else None

    def resolve_investigation_types(self, info):
        return InvestigationType.objects.filter(admeinvestigationtype__adme=self)


class GenotoxType(DjangoObjectType):
    guideline_qualifier = graphene.String()
    study_source = graphene.String()
    test_type = graphene.String()
    outcome = graphene.String()
    guideline = graphene.String()

    class Meta:
        model = Genotox
        fields = "__all__"

    def resolve_guideline_qualifier(self, info):
        return self.guideline_qualifier.title if self.guideline_qualifier else None

    def resolve_study_source(self, info):
        return self.study_source.title if self.study_source else None

    def resolve_test_type(self, info):
        return self.test_type.name if self.test_type else None

    def resolve_outcome(self, info):
        return self.outcome.name if self.outcome else None

    def resolve_guideline(self, info):
        return self.guideline.name if self.guideline else None


class FinalOutcomeType(DjangoObjectType):
    outcome = graphene.String()
    qualifier = graphene.String()
    value = graphene.String()
    populations = graphene.List(PopulationType)

    class Meta:
        model = FinalOutcome
        exclude = ["unit"]

    def resolve_outcome(self, info):
        return self.outcome.name if self.outcome else None

    def resolve_qualifier(self, info):
        return self.qualifier.name if self.qualifier else None

    def resolve_value(self, info):
        return f"{str(self.value)} {self.unit.name if self.unit else None}"

    def resolve_populations(self, info):
        return Population.objects.filter(
            population_outcome_populations__final_outcome=self
        )


class EndpointType(DjangoObjectType):
    reference_point = graphene.String()
    qualifier = graphene.String()
    subpopulation = graphene.String()
    lovalue = graphene.String()
    final_outcomes = graphene.List(FinalOutcomeType)

    class Meta:
        model = Endpoint
        exclude = ["unit"]

    def resolve_reference_point(self, info):
        return self.reference_point.name if self.reference_point else None

    def resolve_qualifier(self, info):
        return self.qualifier.name if self.qualifier else None

    def resolve_subpopulation(self, info):
        return self.subpopulation.name if self.subpopulation else None

    def resolve_lovalue(self, info):
        return f"{str(self.lovalue)} {self.unit.name if self.unit else None}"

    def resolve_final_outcomes(self, info):
        return FinalOutcome.objects.filter(endpoint=self)


class EndpointStudyType(DjangoObjectType):
    test_type = graphene.String()
    guideline = graphene.String()
    species = graphene.String()
    guideline_qualifier = graphene.String()
    study_source = graphene.String()
    sex = graphene.String()
    study_duration = graphene.String()
    endpoints = graphene.List(EndpointType)

    class Meta:
        model = Endpointstudy
        exclude = ["duration_unit"]

    def resolve_test_type(self, info):
        return self.test_type.name if self.test_type else None

    def resolve_guideline(self, info):
        return self.guideline.name if self.guideline else None

    def resolve_species(self, info):
        return self.species.name if self.species else None

    def resolve_sex(self, info):
        return self.sex.name if self.sex else None

    def resolve_guideline_qualifier(self, info):
        return self.guideline_qualifier.title if self.guideline_qualifier else None

    def resolve_study_source(self, info):
        return self.study_source.title if self.study_source else None

    def resolve_study_duration(self, info):
        duration = str(self.study_duration)
        unit = self.duration_unit.name if self.duration_unit else None
        return f"{duration} {unit}"

    def resolve_endpoints(self, info):
        return Endpoint.objects.filter(endpointstudy=self)
