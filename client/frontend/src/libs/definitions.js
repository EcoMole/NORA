export const objectTypes = {
  allergenicities: {
    displayName: 'Allergenicity'
  },
  panels: {
    displayName: 'Panel'
  },
  sciOfficers: {
    displayName: 'Scientific Officer'
  },
  questions: {
    displayName: 'Question'
  },
  'questions.applicants': {
    displayName: 'Applicant'
  },
  'questions.mandates': {
    displayName: 'Mandate'
  },
  foodCategories: {
    displayName: 'Food Category'
  },
  novelFoodCategories: {
    displayName: 'Novel Food Category'
  },
  admes: {
    displayName: 'ADME'
  },
  'admes.investigationTypes': {
    displayName: 'Investigation Type'
  },
  genotoxes: {
    displayName: 'Genotox'
  },
  endpointstudies: {
    displayName: 'Endpoint Study'
  },
  'endpointstudies.endpoints': {
    displayName: 'Endpoint'
  },
  'endpointstudies.endpoints.finalOutcomes': {
    displayName: 'Final Outcome'
  },
  'endpointstudies.endpoints.finalOutcomes.populations': {
    displayName: 'Population'
  }
}

export const fields = {
  // novel food

  novelFoodId: {
    displayName: 'ID',
    flattenedDisplayName: 'Novel Food ID',
    displayGroupName: 'Novel Food',
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for ID',
    tooltipDescription: 'ID tooltip description',
    showInFilters: false
  },

  nfCode: {
    displayName: 'Code',
    flattenedDisplayName: 'Novel Food Code',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'nf_code',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Code',
    tooltipDescription: 'Code tooltip description',
    showInFilters: true
  },
  title: {
    displayName: 'Title',
    flattenedDisplayName: 'Novel Food Title',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'title',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Title',
    tooltipDescription: 'Title tooltip description',
    showInFilters: true
  },
  toxStudyRequired: {
    displayName: 'Toxicology Study Required',
    displayGroupName: 'Toxicology',
    type: 'text',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFood',
    djangoField: 'tox_study_required',
    djangoLookupField: 'tox_study_required',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Toxicology Study Required',
    tooltipDescription: 'Toxicology Study Required tooltip description',
    showInFilters: true
  },
  genotoxFinalOutcome: {
    displayName: 'Genotoxicity Final Outcome',
    displayGroupName: 'Novel Food',
    type: 'text',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'GenotoxFinalOutcome',
    djangoField: 'title',
    djangoLookupField: 'genotox_final_outcome__title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-dna',
    filterDescription: 'description for Genotoxicity Final Outcome',
    tooltipDescription: 'Genotoxicity Final Outcome tooltip description',
    showInFilters: true
  },
  finalToxicologyRemarks: {
    displayName: 'Final Toxicology Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'final_toxicology_remarks__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'description for Final Toxicology Remarks',
    tooltipDescription: 'Final Toxicology Remarks tooltip description',
    showInFilters: true
  },
  proteinDigestibility: {
    displayName: 'Protein Digestibility',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'protein_digestibility__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'protein_digestibility',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-food-drumstick-outline',
    filterDescription: 'description for Protein Digestibility',
    tooltipDescription: 'Protein Digestibility tooltip description',
    showInFilters: true
  },
  antinutritionalFactors: {
    displayName: 'Antinutritional Factors',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'antinutritional_factors__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'antinutritional_factors',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale-balance',
    filterDescription: 'description for Antinutritional Factors',
    tooltipDescription: 'Antinutritional Factors tooltip description',
    showInFilters: true
  },
  hasNutriDisadvantage: {
    displayName: 'Nutritional Disadvantage',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'has_nutri_disadvantage__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'has_nutri_disadvantage',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale-balance',
    filterDescription: 'description for Nutritional Disadvantage',
    tooltipDescription: 'Nutritional Disadvantage tooltip description',
    showInFilters: true
  },
  nutriDisadvantageExplanation: {
    displayName: 'Nutritional Disadvantage Explanation',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'nutri_disadvantage_explanation__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-text-box-outline',
    filterDescription: 'description for Nutritional Disadvantage Explanation',
    tooltipDescription: 'Nutritional Disadvantage Explanation tooltip description',
    showInFilters: true
  },
  sufficientData: {
    displayName: 'Sufficient Data',
    displayGroupName: 'Novel Food',
    flattenedDisplayName: 'Stability - Sufficient Data',
    type: 'text',
    djangoLookupField: 'sufficient_data__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'sufficient_data',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-database-check',
    filterDescription: 'description for Sufficient Data',
    tooltipDescription: 'Sufficient Data tooltip description',
    showInFilters: true
  },
  foodMatrices: {
    displayName: 'Food Matrices',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Food Matrices',
    type: 'text',
    djangoLookupField: 'food_matrices__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'food_matrices',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-grid',
    filterDescription: 'description for Food Matrices',
    tooltipDescription: 'Food Matrices tooltip description',
    showInFilters: true
  },
  instabilityConcerns: {
    displayName: 'Instability Concerns',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'instability_concerns__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'instability_concerns',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription: 'description for Instability Concerns',
    tooltipDescription: 'Instability Concerns tooltip description',
    showInFilters: true
  },
  shelflifeValue: {
    displayName: 'Shelf Life Value',
    displayGroupName: 'Novel Food',
    type: 'number',
    djangoLookupField: 'shelflife_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription: 'description for Shelf Life Value',
    tooltipDescription: 'Shelf Life Value tooltip description',
    showInFilters: true
  },
  shelflifeUnit: {
    displayName: 'Shelf Life Unit',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'shelflife_unit__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'shelflife_unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-timer-sand',
    filterDescription: 'description for Shelf Life Unit',
    tooltipDescription: 'Shelf Life Unit tooltip description',
    showInFilters: true
  },
  endocrineDisruptProp: {
    displayName: 'Endocrine Disruptive Properties',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'endocrine_disrupt_prop__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'endocrine_disrupt_prop',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription: 'description for Endocrine Disruptive Properties',
    tooltipDescription: 'Endocrine Disruptive Properties tooltip description',
    showInFilters: true
  },
  outcome: {
    displayName: 'Outcome',
    flattenedDisplayName: 'Novel Food Outcome',
    displayGroupName: 'Novel Food',
    type: 'text',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFood',
    djangoField: 'outcome',
    djangoLookupField: 'outcome',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Outcome',
    tooltipDescription: 'Outcome tooltip description',
    showInFilters: true
  },
  outcomeRemarks: {
    displayName: 'Outcome Remarks',
    flattenedDisplayName: 'Novel Food Outcome Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'outcome_remarks__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'description for Outcome Remarks',
    tooltipDescription: 'Outcome Remarks tooltip description',
    showInFilters: true
  },
  vocabId: {
    displayName: 'Vocabulary Name',
    flattenedDisplayName: 'Novel Food Vocabulary Name',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'vocab_id__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Vocabulary Name',
    tooltipDescription: 'Vocabulary Name tooltip description',
    showInFilters: true
  },

  'allergenicities.title': {
    displayName: '',
    flattenedDisplayName: 'Allergenicity',
    displayGroupName: 'Allergenicity',
    type: 'text',
    djangoLookupField: 'allergenicities__allergenicity__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'Allergenicity',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Allergenicity',
    tooltipDescription: 'Allergenicity tooltip description',
    showInFilters: true
  },

  // opinion

  opinionDocumentType: {
    displayName: 'Opinion Document Type',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__document_type__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'administrative',
    djangoLimitchoicesModel: 'Opinion',
    djangoLimitchoicesField: 'document_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Document Type',
    tooltipDescription: 'Opinion Document Type tooltip description',
    showInFilters: true
  },
  opinionTitle: {
    displayName: 'Opinion Title',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__title',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Title',
    tooltipDescription: 'Opinion Title tooltip description',
    showInFilters: true
  },
  opinionDoi: {
    displayName: 'Opinion DOI',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__doi',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion DOI',
    tooltipDescription: 'Opinion DOI tooltip description',
    showInFilters: true
  },
  opinionUrl: {
    displayName: 'Opinion URL',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__url',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion URL',
    tooltipDescription: 'Opinion URL tooltip description',
    showInFilters: true
  },
  opinionPublicationDate: {
    displayName: 'Opinion Publication Date',
    displayGroupName: 'Opinion',
    type: 'date',
    djangoLookupField: 'opinion__publication_date',
    qualifiers: ['is before', 'is after', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Publication Date',
    tooltipDescription: 'Opinion Publication Date tooltip description',
    showInFilters: true
  },
  opinionAdoptionDate: {
    displayName: 'Opinion Adoption Date',
    displayGroupName: 'Opinion',
    type: 'date',
    djangoLookupField: 'opinion__adoption_date',
    qualifiers: ['is before', 'is after', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Adoption Date',
    tooltipDescription: 'Opinion Adoption Date tooltip description',
    showInFilters: true
  },

  'panels.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Panel',
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__panels__panel__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'administrative',
    djangoModel: 'Panel',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for Panel's Name",
    tooltipDescription: "Panel's Name tooltip description",
    showInFilters: true
  },

  'sciOfficers.firstName': {
    displayName: 'First Name',
    flattenedDisplayName: "Scientific Officer's First Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__first_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for Scientific Officer's First Name",
    tooltipDescription: "Scientific Officer's First Name tooltip description",
    showInFilters: true
  },
  'sciOfficers.middleName': {
    displayName: 'Middle Name',
    flattenedDisplayName: "Scientific officer's Middle Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__middle_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for scientific officer's Middle Name",
    tooltipDescription: "Scientific officer's Middle Name tooltip description",
    showInFilters: true
  },
  'sciOfficers.lastName': {
    displayName: 'Last Name',
    flattenedDisplayName: "Scientific officer's Last Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__last_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for scientific officer's Last Name",
    tooltipDescription: "Scientific officer's Last Name tooltip description",
    showInFilters: true
  },

  // question

  'questions.number': {
    displayName: 'Number',
    flattenedDisplayName: 'Question Number',
    displayGroupName: 'Question',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__number',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Number',
    tooltipDescription: 'Number tooltip description',
    showInFilters: true
  },

  'questions.applicants.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Applicant',
    displayGroupName: 'Applicant',
    djangoLookupField: 'opinion__questions__question__applicants__applicant__title',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for applicant title',
    tooltipDescription: 'Applicant title tooltip description',
    showInFilters: true
  },

  'questions.mandates.mandateTypeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Mandate Type',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__mandate_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'administrative',
    djangoModel: 'MandateType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type',
    tooltipDescription: 'Mandate Type tooltip description',
    showInFilters: true
  },
  'questions.mandates.mandateTypeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Mandate Type Definition',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField:
      'opinion__questions__question__mandates__mandate_type__definition__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type Definition',
    tooltipDescription: 'Mandate Type Definition tooltip description',
    showInFilters: true
  },
  'questions.mandates.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Mandate Regulation',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__regulation__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'administrative',
    djangoLimitchoicesModel: 'Mandate',
    djangoLimitchoicesField: 'regulation',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Regulation',
    tooltipDescription: 'Mandate Regulation tooltip description',
    showInFilters: true
  },

  'foodCategories.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Food Category Name',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'food_categories__food_category__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'FoodCategory',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Food Category Name',
    tooltipDescription: 'Food Category Name tooltip description',
    showInFilters: true
  },
  'foodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'food_categories__food_category__definition__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Food Category Definition',
    tooltipDescription: 'Food Category Definition tooltip description',
    showInFilters: true
  },

  'novelFoodCategories.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Novel Food Category',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodCategory',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Novel Food Category',
    tooltipDescription: 'Novel Food Category tooltip description',
    showInFilters: true
  },
  'novelFoodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Novel Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__definition__text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Novel Food Category Definition',
    tooltipDescription: 'Novel Food Category Definition tooltip description',
    showInFilters: true
  },
  'novelFoodCategories.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Novel Food Category Regulation',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__regulation__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodCategory',
    djangoLimitchoicesField: 'regulation',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Novel Food Category regulation',
    tooltipDescription: 'Novel Food Category regulation tooltip description',
    showInFilters: true
  },

  // adme

  'admes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'ADME Test Type',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__test_type__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'ADME',
    djangoLimitchoicesField: 'test_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description',
    showInFilters: true
  },
  'admes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'ADME Guideline',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__guideline__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'ADME',
    djangoLimitchoicesField: 'guideline',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description',
    showInFilters: true
  },
  'admes.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'ADME Guideline Qualifier',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__guideline_qualifier__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'GuidelineQualifier',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline Qualifier',
    tooltipDescription: 'Guideline Qualifier tooltip description',
    showInFilters: true
  },
  'admes.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'ADME Study Source',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__study_source__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'StudySource',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Study Source',
    tooltipDescription: 'Study Source tooltip description',
    showInFilters: true
  },

  'admes.investigationTypes.title': {
    displayName: 'Name',
    flattenedDisplayName: 'ADME Investigation Type',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__investigation_types__investigation_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'InvestigationType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask',
    filterDescription: 'description for Investigation Type Name',
    tooltipDescription: 'Investigation Type Name tooltip description',
    showInFilters: true
  },

  // genotox

  'genotoxes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Genotox Test Type',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__test_type__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'test_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-dna',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description',
    showInFilters: true
  },
  'genotoxes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Genotox Guideline',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__guideline__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'guideline',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description',
    showInFilters: true
  },
  'genotoxes.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'Genotox Guideline Qualifier',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__guideline_qualifier__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'GuidelineQualifier',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline Qualifier',
    tooltipDescription: 'Guideline Qualifier tooltip description',
    showInFilters: true
  },
  'genotoxes.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'Genotox Study Source',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__study_source__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'StudySource',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Study Source',
    tooltipDescription: 'Study Source tooltip description',
    showInFilters: true
  },
  'genotoxes.outcome': {
    displayName: 'Outcome',
    flattenedDisplayName: 'Genotox Outcome',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__outcome__tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'outcome',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Genotox Outcome',
    tooltipDescription: 'Genotox Outcome tooltip description',
    showInFilters: true
  },

  // endpoint studies

  'endpointstudies.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Endpoint Study Test Type',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description',
    showInFilters: false
  },
  'endpointstudies.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Endpoint Study Guideline',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description',
    showInFilters: false
  },
  'endpointstudies.species': {
    displayName: 'Species',
    flattenedDisplayName: 'Endpoint Study Species',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-paw',
    filterDescription: 'description for Species',
    tooltipDescription: 'Species tooltip description',
    showInFilters: false
  },
  'endpointstudies.sex': {
    displayName: 'Sex',
    flattenedDisplayName: 'Endpoint Study Sex',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-gender-male-female',
    filterDescription: 'description for Sex',
    tooltipDescription: 'Sex tooltip description',
    showInFilters: false
  },
  'endpointstudies.studyDuration': {
    displayName: 'Study Duration',
    flattenedDisplayName: 'Endpoint Study Duration',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription: 'description for Study Duration',
    tooltipDescription: 'Study Duration tooltip description',
    showInFilters: false
  },

  'endpointstudies.endpoints.referencePoint': {
    displayName: 'Reference Point',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-target',
    filterDescription: 'description for Reference Point',
    tooltipDescription: 'Reference Point tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Endpoint Qualifier',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.subpopulation': {
    displayName: 'Subpopulation',
    flattenedDisplayName: 'Endpoint Subpopulation',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-account-group',
    filterDescription: 'description for Subpopulation',
    tooltipDescription: 'Subpopulation tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.lovalue': {
    displayName: 'Value',
    flattenedDisplayName: 'Endpoint Value',
    displayGroupName: 'Endpoint',
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than'],
    icon: 'mdi-arrow-down',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description',
    showInFilters: false
  },

  'endpointstudies.endpoints.finalOutcomes.outcome': {
    displayName: '',
    flattenedDisplayName: 'Final Outcome',
    displayGroupName: 'Final Outcome',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Outcome',
    tooltipDescription: 'Outcome tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Final Outcome Qualifier',
    displayGroupName: 'Final Outcome',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Final Outcome Value',
    displayGroupName: 'Final Outcome',
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description',
    showInFilters: false
  },

  'endpointstudies.endpoints.finalOutcomes.populations.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Final Outcome Population Subgroup',
    displayGroupName: 'Population',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-account-multiple-outline',
    filterDescription: 'description for Subgroup',
    tooltipDescription: 'Subgroup tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.populations.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Final Outcome Population Qualifier',
    displayGroupName: 'Population',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.populations.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Final Outcome Population Value',
    displayGroupName: 'Population',
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description',
    showInFilters: false
  },
  // links do django admin
  djangoAdminOpinion: {
    displayName: 'Opinion Admin',
    flattenedDisplayName: 'Opinion Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  djangoAdminNovelFood: {
    displayName: 'Novel Food Admin',
    flattenedDisplayName: 'Novel Food Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'admes.djangoAdminAdme': {
    displayName: 'ADME Admin',
    flattenedDisplayName: 'ADME Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'genotoxes.djangoAdminGenotox': {
    displayName: 'Genotox Admin',
    flattenedDisplayName: 'Genotox Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'Opinion tooltip description',
    showInFilters: false
  },
  'endpointstudies.djangoAdminEndpointstudy': {
    displayName: 'Endpoint Study Admin',
    flattenedDisplayName: 'Endpoint Study Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.djangoAdminFinalOutcome': {
    displayName: 'Final Outcome Admin',
    flattenedDisplayName: 'Final Outcome Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    tooltipDescription: 'will provide a link to django admin',
    showInFilters: false
  },
}
