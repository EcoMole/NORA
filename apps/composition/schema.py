import graphene
from composition.models import (
    Composition,
    NovelFoodVariant,
    ProductionNovelFoodVariant,
    ProposedUse,
    RiskAssessRedFlag,
)
from graphene_django.types import DjangoObjectType
from taxonomies.models import Population
from taxonomies.schema import PopulationType


class RiskAssessRedFlagType(DjangoObjectType):
    class Meta:
        model = RiskAssessRedFlag
        fields = "__all__"


class ProductionNovelFoodVariantType(DjangoObjectType):
    process = graphene.String()

    class Meta:
        model = ProductionNovelFoodVariant
        fields = "__all__"

    def resolve_process(self, info):
        return self.process.name if self.process else None


class ProposedUseType(DjangoObjectType):
    class Meta:
        model = ProposedUse
        fields = "__all__"


class CompositionType(DjangoObjectType):
    unit = graphene.String()
    qualifier = graphene.String()
    parameter_title = graphene.String()
    parameter_vocab_id = graphene.String()
    parameter_type_title = graphene.String()

    class Meta:
        model = Composition
        fields = "__all__"

    def resolve_parameter(self, info):
        return self.parameter

    def resolve_unit(self, info):
        return self.unit.name if self.unit else None

    def resolve_qualifier(self, info):
        return self.qualifier.name if self.qualifier else None

    def resolve_parameter_title(self, info):
        return self.parameter.title if self.parameter else None

    def resolve_parameter_vocab_id(self, info):
        return (
            self.parameter.vocab_id.name
            if self.parameter and self.parameter.vocab_id
            else None
        )

    def resolve_parameter_type_title(self, info):
        return (
            self.parameter.type.title
            if self.parameter and self.parameter.type
            else None
        )


class NovelFoodVariantType(DjangoObjectType):
    food_form = graphene.String()
    risk_assess_red_flags = graphene.List(RiskAssessRedFlagType)
    production_processes = graphene.List(ProductionNovelFoodVariantType)
    proposed_uses = graphene.List(ProposedUseType)
    population = graphene.List(PopulationType)
    compositions = graphene.List(CompositionType)
    django_admin_novel_food_variant = graphene.String()

    class Meta:
        model = NovelFoodVariant
        fields = "__all__"

    def resolve_food_form(self, info):
        return self.food_form.title if self.food_form else None

    def resolve_risk_assess_red_flags(self, info):
        return RiskAssessRedFlag.objects.filter(
            riskassessredflagnfvariant__nf_variant=self
        )

    def resolve_production_processes(self, info):
        return ProductionNovelFoodVariant.objects.filter(nf_variant=self)

    def resolve_proposed_uses(self, info):
        return ProposedUse.objects.filter(nf_variant=self)

    def resolve_population(self, info):
        return Population.objects.filter(population_proposed_uses__nf_variant=self)

    def resolve_compositions(self, info):
        return Composition.objects.filter(nf_variant=self)

    def resolve_django_admin_novel_food_variant(self, info):
        return f"composition/novelfoodvariant/{self.id}/change/"
