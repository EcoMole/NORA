from django.contrib import admin
from django import forms

from novel_food.models import (
    NovelFood,
    FoodCategory,
    NutritionalDisadvantage,
    NovelFoodCategory,
    Category,
    NovelFoodComponent,
    NovelFoodOrganism,
    Organism
)

from allergenicity.models import AllergenicityNovelFood, Allergenicity

class NovelFoodCategoryInline(admin.TabularInline):
    model =  NovelFoodCategory #NovelFood.categories.through
    extra = 1


class NovelFoodComponentInline(admin.TabularInline):
    model = NovelFoodComponent
    extra = 1

class NovelFoodOrganismInline(admin.TabularInline):
    model = NovelFoodOrganism
    extra = 1

class NutritionalDisadvantageInline(admin.TabularInline):
    model = NutritionalDisadvantage
    extra = 1


class NovelFoodForm(forms.ModelForm):
    allergenicity = forms.ModelMultipleChoiceField(
        queryset=Allergenicity.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = NovelFood
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['allergenicity'].initial = self.instance.allergenicity.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if instance.pk:
            instance.allergenicity.set(self.cleaned_data['allergenicity'])
        return instance


@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    form = NovelFoodForm
    fieldsets = [
        ('General Information', {
            'fields': ['opinion', 'nf_code']
        }),
        ('Toxicity', {
            'fields': ['is_mutagenic', 'is_genotoxic', 'is_carcinogenic']
        }),
        ('Nutrition', {
            'fields': ['protein_digestibility', 'antinutritional_factors', 'nutritional_disadvantage'],
        }),
        ('STABILITY', {
            'fields': ['sufficient_data', 'food_matrices', ('shelflife_value', 'shelflife_unit')],
            'description': 'This section is for stability related fields'
        }),
        ('Miscellaneous', {
            'fields': ['rms_efsa', 'endocrine_disrupt_prop', ],
            'classes': ['collapse']
        }),
        ('ALLERGENICITY', {
            'fields': ['allergenicity'],
        }),
        ('OUTCOME', {
            'fields': [('outcome', 'outcome_remarks')],
        }),

    ]
    list_display = ['nf_code', 'opinion', 'outcome', 'outcome_remarks']
    search_fields = ['nf_code']
    inlines = [NovelFoodCategoryInline, NovelFoodComponentInline, NovelFoodOrganismInline]
    list_filter = ['is_carcinogenic', 'is_genotoxic', 'is_mutagenic']

""" @admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {
            'fields': ['opinion', 'nf_code']
        }),
        ('Toxicity', {
            'fields': [('is_mutagenic', 'is_genotoxic', 'is_carcinogenic')]
        }),
        ('Nutrition', {
            'fields': ['protein_digestibility', 'antinutritional_factors']
        }),
        ('STABILITY', {
            'fields': ['sufficient_data', 'food_matrices', 'shelflife_value', 'shelflife_unit'],
            'description': 'This section is for stability related fields'
        }),
        ('Miscellaneous', {
            'fields': ['rms_efsa', 'endocrine_disrupt_prop', 'outcome', 'outcome_remarks'],
            'classes': ['collapse']
        })
    ]
    list_display = ['nf_code', 'opinion', 'outcome', 'outcome_remarks']
    search_fields = ['nf_code']
    inlines = [NovelFoodCategoryInline, AllergenicityNovelFoodInline, NutritionalDisadvantageInline, NovelFoodComponentInline, NovelFoodOrganismInline]
    list_filter = ['is_carcinogenic', 'is_genotoxic', 'is_mutagenic'] """


""" class NovelFoodAdmin(admin.ModelAdmin):
    list_display = [
        'nf_code',
        'opinion',
        'outcome',
        'outcome_remarks'
    ]

    inlines = [NovelFoodCategoryInline, AllergenicityNovelFoodInline] """

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'definition'
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'definition',
        'regulation_id'
    ]

@admin.register(NutritionalDisadvantage)
class NutritionalDisadvantageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ['organism_node']
