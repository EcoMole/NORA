import graphene
from administrative.models import Panel, Question, ScientificOfficer
from administrative.schema import (  # noqa
    OpinionType,
    PanelType,
    QuestionType,
    ScientificOfficerType,
)
from composition.models import NovelFoodVariant
from composition.schema import NovelFoodVariantType
from graphene_django.types import DjangoObjectType
from studies.models import ADME, Endpointstudy, Genotox
from studies.schema import ADMEType, EndpointStudyType, GenotoxType

from .models import (
    HBGV,
    Allergenicity,
    BackgroundExposureAssessment,
    ChemDescriptor,
    ChemicalSyn,
    FoodCategory,
    NovelFood,
    NovelFoodCategory,
    NovelFoodChemical,
    NovelFoodOrganism,
    NovelFoodSyn,
    OrganismSyn,
    Species,
    SpecificToxicity,
    SubstanceOfConcernNovelFood,
)


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


class NovelFoodSynType(DjangoObjectType):
    class Meta:
        model = NovelFoodSyn
        fields = "__all__"

    type_title = graphene.String()
    type_definition = graphene.String()

    def resolve_type_title(self, info):
        return self.syn_type.title if self.syn_type else None

    def resolve_type_definition(self, info):
        return self.syn_type.definition if self.syn_type else None


class OrganismSynType(DjangoObjectType):
    class Meta:
        model = OrganismSyn
        fields = "__all__"

    type_title = graphene.String()
    type_definition = graphene.String()

    def resolve_type_title(self, info):
        return self.syn_type.title if self.syn_type else None

    def resolve_type_definition(self, info):
        return self.syn_type.definition if self.syn_type else None


class SpeciesType(DjangoObjectType):
    class Meta:
        model = Species
        fields = "__all__"

    genus = graphene.String()
    family = graphene.String()
    org_type = graphene.String()

    def resolve_genus(self, info):
        return self.genus.title if self.genus else None

    def resolve_family(self, info):
        return self.genus.family.title if self.genus and self.genus.family else None

    def resolve_org_type(self, info):
        return (
            self.genus.family.org_type.title
            if self.genus and self.genus.family and self.genus.family.org_type
            else None
        )


class NovelFoodOrganismType(DjangoObjectType):
    class Meta:
        model = NovelFoodOrganism
        fields = "__all__"

    organism = graphene.String()
    org_part = graphene.String()
    is_gmo = graphene.String()
    has_qps = graphene.String()
    cells_modified = graphene.String()
    species = graphene.List(SpeciesType)
    org_synonyms = graphene.List(OrganismSynType)

    def resolve_organism(self, info):
        return (
            self.organism.vocab_id.name
            if self.organism and self.organism.vocab_id
            else None
        )

    def resolve_org_part(self, info):
        return self.org_part.name if self.org_part else None

    def resolve_is_gmo(self, info):
        return self.is_gmo.name if self.is_gmo else None

    def resolve_has_qps(self, info):
        return self.has_qps.name if self.has_qps else None

    def resolve_cells_modified(self, info):
        return self.cells_modified.name if self.cells_modified else None

    def resolve_species(self, info):
        return Species.objects.filter(organism__novelfoodorganism=self)

    def resolve_org_synonyms(self, info):
        return OrganismSyn.objects.filter(organism__novelfoodorganism=self)


class ChemDescriptorType(DjangoObjectType):
    class Meta:
        model = ChemDescriptor
        fields = "__all__"


class ChemicalSynType(DjangoObjectType):
    class Meta:
        model = ChemicalSyn
        fields = "__all__"

    type_title = graphene.String()
    type_definition = graphene.String()

    def resolve_type_title(self, info):
        return self.syn_type.title if self.syn_type else None

    def resolve_type_definition(self, info):
        return self.syn_type.definition if self.syn_type else None


class NovelFoodChemicalType(DjangoObjectType):
    class Meta:
        model = NovelFoodChemical
        fields = "__all__"

    chemical = graphene.String()
    chem_synonyms = graphene.List(ChemicalSynType)
    chem_descriptors = graphene.List(ChemDescriptorType)

    def resolve_chemical(self, info):
        return (
            self.chemical.vocab_id.name
            if self.chemical and self.chemical.vocab_id
            else None
        )

    def resolve_chem_synonyms(self, info):
        return ChemicalSyn.objects.filter(chemical__novelfoodchemical=self)

    def resolve_chem_descriptors(self, info):
        return ChemDescriptor.objects.filter(chemical__novelfoodchemical=self)


class SpecificToxicityType(DjangoObjectType):
    class Meta:
        model = SpecificToxicity
        fields = "__all__"

    specific_toxicity = graphene.String()

    def resolve_specific_toxicity(self, info):
        return self.specific_toxicity.name if self.specific_toxicity else None


class SubstanceOfConcernNovelFoodType(DjangoObjectType):
    class Meta:
        model = SubstanceOfConcernNovelFood
        fields = "__all__"

    substance_of_concern = graphene.String()

    def resolve_substance_of_concern(self, info):
        return self.substance_of_concern.name if self.substance_of_concern else None


class BackgroundExposureAssessmentType(DjangoObjectType):
    class Meta:
        model = BackgroundExposureAssessment
        fields = "__all__"

    comp_of_interest = graphene.String()

    def resolve_comp_of_interest(self, info):
        return self.comp_of_interest.name if self.comp_of_interest else None


class HBGVType(DjangoObjectType):
    class Meta:
        model = HBGV
        fields = "__all__"

    type = graphene.String()
    exceeded = graphene.String()
    substance = graphene.String()

    def resolve_type(self, info):
        return self.type.name if self.type else None

    def resolve_exceeded(self, info):
        return self.exceeded.name if self.exceeded else None

    def resolve_substance(self, info):
        return self.substance.name if self.substance else None


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
    django_admin_opinion = graphene.String()
    django_admin_novel_food = graphene.String()
    novel_food_variants = graphene.List(NovelFoodVariantType)
    synonyms = graphene.List(NovelFoodSynType)
    organisms = graphene.List(NovelFoodOrganismType)
    chemicals = graphene.List(NovelFoodChemicalType)
    specific_toxicities = graphene.List(SpecificToxicityType)
    substances_of_concern = graphene.List(SubstanceOfConcernNovelFoodType)
    background_exposure_assessments = graphene.List(BackgroundExposureAssessmentType)
    hbgvs = graphene.List(HBGVType)

    class Meta:
        model = NovelFood
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

    def resolve_specific_toxicities(self, info):
        return SpecificToxicity.objects.filter(novel_food=self)

    def resolve_substances_of_concern(self, info):
        return SubstanceOfConcernNovelFood.objects.filter(novel_food=self)

    def resolve_background_exposure_assessments(self, info):
        return BackgroundExposureAssessment.objects.filter(novel_food=self)

    def resolve_hbgvs(self, info):
        return HBGV.objects.filter(novel_food=self)

    def resolve_chemicals(self, info):
        return NovelFoodChemical.objects.filter(novel_food=self)

    def resolve_organisms(self, info):
        return NovelFoodOrganism.objects.filter(novel_food=self)

    def resolve_synonyms(self, info):
        return NovelFoodSyn.objects.filter(novel_food=self)

    def resolve_django_admin_opinion(self, info):
        return f"administrative/opinion/{self.opinion.id}/change/"

    def resolve_django_admin_novel_food(self, info):
        return f"novel_food/novelfood/{self.id}/change/"

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

    def resolve_novel_food_variants(self, info):
        return NovelFoodVariant.objects.filter(novel_food=self)
