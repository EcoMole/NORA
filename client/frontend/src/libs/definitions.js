export const objectTypes = {
  allergenicities: {
    displayName: 'Allergenicity'
  },
  synonyms: {
    displayName: 'Novel Food Synonym'
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
  },
  novelFoodVariants: {
    displayName: 'Novel Food Variant'
  },
  'novelFoodVariants.riskAssessRedFlags': {
    displayName: 'Risk Assessment Red Flag'
  },
  'novelFoodVariants.productionProcesses': {
    displayName: 'Production Process'
  },
  'novelFoodVariants.proposedUses': {
    displayName: 'Proposed Use'
  },
  'novelFoodVariants.proposedUses.population': {
    displayName: 'Proposed Uses Population'
  },
  'novelFoodVariants.compositions': {
    displayName: 'Composition'
  },
  organisms: {
    displayName: 'Organism'
  },
  'organisms.species': {
    displayName: 'Taxonomy'
  },
  'organisms.orgSynonyms': {
    displayName: 'Organism Synonym'
  },
  chemicals: {
    displayName: 'Chemical'
  },
  'chemicals.chemSynonyms': {
    displayName: 'Chemical Synonym'
  },
  'chemicals.chemDescriptors': {
    displayName: 'Chemical Descriptor'
  },
  specificToxicities: {
    displayName: 'Specific Toxicity'
  },
  substancesOfConcern: {
    displayName: 'Substance of Concern'
  },
  backgroundExposureAssessments: {
    displayName: 'Background Exposure Assessment'
  },
  hbgvs: {
    displayName: 'HBGV'
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
    filterDescription: 'A unique numerical ID of the Novel Food in the database',
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
    filterDescription: 'Dossier number, e.g., NF 2018/0381',
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
    filterDescription:
      'Name of the Novel Food taken word-for-word from the title of the opinion, e.g., mung bean protein',
    showInFilters: true
  },
  toxStudyRequired: {
    displayName: 'Toxicology Study Required',
    flattenedDisplayName: 'Toxicology Study Required',
    displayGroupName: 'Toxicology',
    type: 'text',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFood',
    djangoField: 'tox_study_required',
    djangoLookupField: 'tox_study_required',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription: 'Were toxicology studies required for the assessment of the NF/TF?',
    showInFilters: true
  },
  genotoxFinalOutcome: {
    displayName: 'Genotoxicity Final Outcome',
    flattenedDisplayName: 'Genotoxicity Final Outcome',
    displayGroupName: 'Novel Food',
    type: 'text',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'GenotoxFinalOutcome',
    djangoField: 'title',
    djangoLookupField: 'genotox_final_outcome__title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-dna',
    filterDescription:
      'Panel’s final conclusion on genotoxicity. Can be either blank, “no concerns”, “concerns” or “inconclusive”',
    showInFilters: true
  },
  finalToxicologyRemarks: {
    displayName: 'Final Toxicology Remarks',
    flattenedDisplayName: 'Final Toxicology Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'final_toxicology_remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription:
      'Remarks relevant to the final assessment of toxicology, e.g.,  “insufficient data to support the use of the NF at the proposed level”',
    showInFilters: true
  },
  proteinDigestibility: {
    displayName: 'Protein Digestibility',
    flattenedDisplayName: 'Nutrition - Protein Digestibility',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'protein_digestibility',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'protein_digestibility',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-food-drumstick-outline',
    filterDescription:
      'Was the digestibility of protein in the NF/TF discussed within the opinion?',
    showInFilters: true
  },
  antinutritionalFactors: {
    displayName: 'Antinutritional Factors',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'antinutritional_factors',
    fieldType: 'tax_node',
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
    showInFilters: true
  },
  hasNutriDisadvantage: {
    displayName: 'Nutritional Disadvantage',
    displayGroupName: 'Novel Food',
    flattenedDisplayName: 'Nutrition - Nutritional Disadvantage',
    type: 'text',
    djangoLookupField: 'has_nutri_disadvantage',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'has_nutri_disadvantage',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale-balance',
    filterDescription:
      'The Panel’s conclusion on whether the NF/TF is nutritionally disadvantageous, e.g., due to a significant amount of antinutritional factors',
    showInFilters: true
  },
  nutriDisadvantageExplanation: {
    displayName: 'Nutritional Disadvantage Explanation',
    displayGroupName: 'Novel Food',
    flattenedDisplayName: 'Nutrition - Nutritional Disadvantage Explanation',
    type: 'text',
    djangoLookupField: 'nutri_disadvantage_explanation',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-text-box-outline',
    filterDescription:
      'Reasoning for why the NF/TF is considered nutritionally disadvantageous. Only filled in for NF/TF which were claimed nutritionally disadvantageous by the Panel.',
    showInFilters: true
  },
  sufficientData: {
    displayName: 'Sufficient Data',
    displayGroupName: 'Novel Food',
    flattenedDisplayName: 'Stability - Sufficient Data',
    type: 'text',
    djangoLookupField: 'sufficient_data',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'sufficient_data',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-database-check',
    filterDescription: 'Were sufficient data provided to demonstrate the stability of the NF/TF?',
    showInFilters: true
  },
  foodMatrices: {
    displayName: 'Food Matrices',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Food Matrices',
    type: 'text',
    djangoLookupField: 'food_matrices',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'food_matrices',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-grid',
    filterDescription: 'Was stability within different food matrices discussed within the opinion?',
    showInFilters: true
  },
  instabilityConcerns: {
    displayName: 'Instability Concerns',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Instability concerns',
    type: 'text',
    djangoLookupField: 'instability_concerns',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'instability_concerns',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      'Were any instability concerns identified within the opinion (e.g., instability within certain food matrices, at high temperatures or in the absence of stabilisers)?',
    showInFilters: true
  },
  shelflifeValue: {
    displayName: 'Shelf Life Value',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Shelf Life Value',
    type: 'number',
    djangoLookupField: 'shelflife_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription:
      'The numerical value for shelf life, either proposed by the applicant or specified by the Panel.',
    showInFilters: true
  },
  shelflifeUnit: {
    displayName: 'Shelf Life Unit',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Shelf Life Unit',
    type: 'text',
    djangoLookupField: 'shelflife_unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'shelflife_unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-timer-sand',
    filterDescription: 'Unit of the proposed shelf life (e.g., day, month, year)',
    showInFilters: true
  },
  endocrineDisruptProp: {
    displayName: 'Endocrine Disruptive Properties',
    displayGroupName: 'Hazards',
    flattenedDisplayName: 'Hazards - Endocrine Disruptive Properties',
    type: 'text',
    djangoLookupField: 'endocrine_disrupt_prop',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'endocrine_disrupt_prop',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription: 'Were endocrine disrupting properties identified in the NF/TF?',
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
    filterDescription:
      'Conclusion of the opinion. Can be either: “positive”, “partially negative”, or “negative”.',
    showInFilters: true
  },
  outcomeRemarks: {
    displayName: 'Outcome Remarks',
    flattenedDisplayName: 'Novel Food Outcome Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'outcome_remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'Reasoning for a partially negative or negative Opinion Outcome',
    showInFilters: true
  },
  vocabId: {
    displayName: 'Vocabulary Name',
    flattenedDisplayName: 'Novel Food Vocabulary Name',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Specifies the name from the PARAM catalogue used to map the Novel Food to an existing entry in the catalogue. This field is only used for Novel Foods that already exist in the catalogue, as no new terms are added.',
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
    filterDescription: 'Panel’s conclusion on allergenicity risk posed by the NF/TF',
    showInFilters: true
  },

  'specificToxicities.specificToxicity': {
    displayName: '',
    flattenedDisplayName: 'Specific Toxicity',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'specific_toxicities__specific_toxicity',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'SpecificToxicity',
    djangoLimitchoicesField: 'specific_toxicity',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Specific Toxicity',
    showInFilters: true
  },
  'substancesOfConcern.substanceOfConcern': {
    displayName: '',
    flattenedDisplayName: 'Substance of Concern',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'substances_of_concern__substance_of_concern',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'SubstanceOfConcernNovelFood',
    djangoLimitchoicesField: 'substance_of_concern',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Substance of Concern',
    showInFilters: true
  },
  'backgroundExposureAssessments.compOfInterest': {
    displayName: 'Composition of Interest',
    flattenedDisplayName: 'Background Exposure Assessment - Composition of Interest',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'bg_expo_assessments__comp_of_interest',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'BackgroundExposureAssessment',
    djangoLimitchoicesField: 'comp_of_interest',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Background Exposure Assessment',
    showInFilters: true
  },
  'hbgvs.type': {
    displayName: 'Type',
    flattenedDisplayName: 'HBGV Type',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'hbgvs__type',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'type',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for HBGV Type',
    showInFilters: true
  },
  'hbgvs.exceeded': {
    displayName: 'Exceeded',
    flattenedDisplayName: 'HBGV Exceeded',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'hbgvs__exceeded',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'exceeded',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for HBGV Exceeded',
    showInFilters: true
  },
  'hbgvs.substance': {
    displayName: 'Substance',
    flattenedDisplayName: 'HBGV Substance',
    displayGroupName: 'Hazards',
    type: 'text',
    djangoLookupField: 'hbgvs__substance',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'substance',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for HBGV Substance',
    showInFilters: true
  },

  // Novel Food Synonyms

  'synonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Novel Food Synonym',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'synonyms__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Novel Food Synonym',
    showInFilters: true
  },
  'synonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Novel Food Synonym Type',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'synonyms__syn_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Novel Food Synonym Type',
    showInFilters: true
  },
  'synonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Novel Food Synonym Type Definition',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: '',
    filterDescription: 'description for Novel Food Synonym Type Definition',
    showInFilters: true
  },

  // opinion

  opinionDocumentType: {
    displayName: 'Opinion Document Type',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__document_type',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'administrative',
    djangoLimitchoicesModel: 'Opinion',
    djangoLimitchoicesField: 'document_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Defines whether the document is an EFSA opinion, Technical Report or an EFSA statement.',
    showInFilters: true
  },
  opinionTitle: {
    displayName: 'Opinion Title',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__title',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Title of the publication, e.g., “Safety of chia seeds (Salvia hispanica L.) powders, as novel foods, pursuant to Regulation (EU) 2015/2283”',
    showInFilters: true
  },
  opinionDoi: {
    displayName: 'Opinion DOI',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__doi',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Digital Object Identifier (DOI) of the publication, e.g., “10.2903/j.efsa.2021.6846”',
    showInFilters: true
  },
  opinionUrl: {
    displayName: 'Opinion URL',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__url',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'URL to the publication on the EFSA Journal website, e.g., “https://efsa.onlinelibrary.wiley.com/doi/10.2903/j.efsa.2021.6846”',
    showInFilters: true
  },
  opinionPublicationDate: {
    displayName: 'Opinion Publication Date',
    displayGroupName: 'Opinion',
    type: 'date',
    djangoLookupField: 'opinion__publication_date',
    qualifiers: ['is before', 'is after', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'The date when the publication (scientific opinion/technical report/statement) was published',
    showInFilters: true
  },
  opinionAdoptionDate: {
    displayName: 'Opinion Adoption Date',
    displayGroupName: 'Opinion',
    type: 'date',
    djangoLookupField: 'opinion__adoption_date',
    qualifiers: ['is before', 'is after', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'The date when the publication (scientific opinion/statement) was adopted by the Panel. For Technical reports, this is the “Approval date”.',
    showInFilters: true
  },

  'panels.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Opinion - Panel',
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__panels__panel__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'administrative',
    djangoModel: 'Panel',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'The abbreviation of the EFSA Panel that authored the publication. “EFSA” was used instead of Panel in cases of Technical Reports or when EFSA was the sole author.',
    showInFilters: true
  },

  'sciOfficers.firstName': {
    displayName: 'First Name',
    flattenedDisplayName: "Opinion - Scientific Officer's First Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__first_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'First Name of the EFSA Scientific officer that authored the publication',
    showInFilters: true
  },
  'sciOfficers.middleName': {
    displayName: 'Middle Name',
    flattenedDisplayName: "Opinion - Scientific officer's Middle Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__middle_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'Middle name of the EFSA Scientific officer that authored the publication',
    showInFilters: true
  },
  'sciOfficers.lastName': {
    displayName: 'Last Name',
    flattenedDisplayName: "Opinion - Scientific officer's Last Name",
    displayGroupName: 'Administrative',
    type: 'text',
    djangoLookupField: 'opinion__sci_officers__sci_officer__last_name',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Last name (family name) of the EFSA Scientific officer that authored the publication',
    showInFilters: true
  },

  // question

  'questions.number': {
    displayName: 'Number',
    flattenedDisplayName: 'Opinion - Question Number',
    displayGroupName: 'Question',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__number',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'Question number of the opinion/techical report, e.g., EFSA-Q-2018-00373',
    showInFilters: true
  },

  'questions.applicants.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Opinion - Applicant',
    displayGroupName: 'Applicant',
    djangoLookupField: 'opinion__questions__question__applicants__applicant__title',
    type: 'text',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'Name of the applicant (usually a company)',
    showInFilters: true
  },

  'questions.mandates.mandateTypeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Opinion - Mandate Type',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__mandate_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'administrative',
    djangoModel: 'MandateType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Describes the whether the mandate was for Novel Food (New dossier, Extension of use, or Nutrient source) or Traditional Food.',
    showInFilters: true
  },
  'questions.mandates.mandateTypeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Mandate Type Definition',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField:
      'opinion__questions__question__mandates__mandate_type__definition',
      fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type Definition',
    showInFilters: true
  },
  'questions.mandates.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Opinion - Mandate Regulation',
    displayGroupName: 'Mandate',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__regulation',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'administrative',
    djangoLimitchoicesModel: 'Mandate',
    djangoLimitchoicesField: 'regulation',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Assigns the regulation(s) according to which the NF/TF was assessed, e.g., EU 2015/2283.',
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
    showInFilters: true
  },
  'foodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'food_categories__food_category__definition',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Food Category Definition',
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
    filterDescription:
      'Describes which food category as defined by a relevant legislation (e.g., Article 3 of Regulation (EU) 2015/22832) the NF/TF falls under (e.g., “From microorganisms, fungi or algae” or “New production process”',
    showInFilters: true
  },
  'novelFoodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Novel Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__definition',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription:
      'The full text of the definition of the food category in the legislation (e.g., Article 3 of Regulation (EU) 2015/2283).',
    showInFilters: true
  },
  'novelFoodCategories.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Novel Food Category Regulation',
    displayGroupName: 'Novel Food',
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__regulation',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodCategory',
    djangoLimitchoicesField: 'regulation',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription:
      'Describes which legislation (e.g., Article 3 of Regulation (EU) 2015/22832) defined the NF category.',
    showInFilters: true
  },

  // identities

  'organisms.organism': {
    displayName: 'Vocab ID',
    flattenedDisplayName: 'Organism Vocab ID',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'Organism',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Vocab ID',
    showInFilters: true
  },
  'organisms.orgPart': {
    displayName: 'Part',
    flattenedDisplayName: 'Organism Part',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__org_part',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'org_part',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Part',
    showInFilters: true
  },
  'organisms.variant': {
    displayName: 'Variant',
    flattenedDisplayName: 'Organism Variant',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__variant',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodOrganism',
    djangoField: 'variant',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Variant',
    showInFilters: true
  },
  'organisms.isGmo': {
    displayName: 'is GMO',
    flattenedDisplayName: 'Organism is GMO',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__is_gmo',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'is_gmo',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism is GMO',
    showInFilters: true
  },
  'organisms.hasQps': {
    displayName: 'has QPS',
    flattenedDisplayName: 'Organism has QPS',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__has_qps',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'has_qps',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism has QPS',
    showInFilters: true
  },

  'organisms.cellCulture': {
    displayName: 'Cell Culture',
    flattenedDisplayName: 'Organism Cell Culture',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__cell_culture',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodOrganism',
    djangoField: 'cell_culture',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Cell Culture',
    showInFilters: true
  },

  'organisms.cellsModified': {
    displayName: 'Cells Modified',
    flattenedDisplayName: 'Organism Cell Modification',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__cells_modified',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'cells_modified',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Cell Modification',
    showInFilters: true
  },
  'organisms.species.name': {
    displayName: 'Species Name',
    flattenedDisplayName: 'Species Name',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__name',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'Species',
    djangoField: 'name',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Species Name',
    showInFilters: true
  },
  'organisms.species.scientificName': {
    displayName: 'Scientific Name',
    flattenedDisplayName: 'Species Scientific Name',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__scientific_name',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'Species',
    djangoField: 'scientific_name',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Species Scientific Name',
    showInFilters: true
  },
  'organisms.species.genus': {
    displayName: 'Genus',
    flattenedDisplayName: 'Species Genus',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'Genus',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Species Genus',
    showInFilters: true
  },
  'organisms.species.family': {
    displayName: 'Family',
    flattenedDisplayName: 'Species Family',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__family__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'Family',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Species Family',
    showInFilters: true
  },
  'organisms.species.orgType': {
    displayName: 'Organism Type',
    flattenedDisplayName: 'Species Organism Type',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__family__org_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'OrgType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Species Organism Type',
    showInFilters: true
  },
  'organisms.orgSynonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Organism Synonym',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'OrganismSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Synonym',
    showInFilters: true
  },
  'organisms.orgSynonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Organism Synonym Type',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__syn_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Synonym Type',
    showInFilters: true
  },
  'organisms.orgSynonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Organism Synonym Type Definition',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: '',
    filterDescription: 'description for Organism Synonym Type Definition',
    showInFilters: true
  },

  'chemicals.chemical': {
    displayName: 'Vocab ID',
    flattenedDisplayName: 'Chemical Vocab ID',
    displayGroupName: 'Identity',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'Chemical',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Vocab ID',
    showInFilters: true
  },
  'chemicals.chemSynonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Chemical Synonym',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'ChemicalSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Synonym',
    showInFilters: true
  },
  'chemicals.chemSynonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Chemical Synonym Type',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__syn_type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Synonym Type',
    showInFilters: true
  },
  'chemicals.chemSynonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Chemical Synonym Type Definition',
    displayGroupName: 'Synonym',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Synonym Type Definition',
    showInFilters: true
  },
  'chemicals.chemDescriptors.type': {
    displayName: 'Type',
    flattenedDisplayName: 'Chemical Descriptor Type',
    displayGroupName: 'Chemical',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__chem_descriptors__type',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'novel_food',
    djangoModel: 'ChemDescriptor',
    djangoField: 'type',
    qualifiers: ['is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Descriptor Type',
    showInFilters: true
  },
  'chemicals.chemDescriptors.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Chemical Descriptor Value',
    displayGroupName: 'Chemical',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__chem_descriptors__value',
    qualifiers: ['contains', 'is', 'is None'],
    icon: '',
    filterDescription: 'description for Chemical Descriptor Value',
    showInFilters: true
  },

  // adme

  'admes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'ADME Test Type',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'ADME',
    djangoLimitchoicesField: 'test_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription:
      'Selects the type of study from the following options: In silico, In vitro, Animal, Human interventional clinical trial, Human observational clinical trial, Human other, Other, Not reported',
    showInFilters: true
  },
  'admes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'ADME Guideline',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'ADME',
    djangoLimitchoicesField: 'guideline',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Describes the guideline according to which the study was carried out (e.g. ICH-GCP).',
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
    filterDescription:
      'Describes whether the study was conducted according to, similar to, or not according to a guideline. This field is left blank for cases when the guideline was not specified in the opinion.',
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
    filterDescription:
      'Study source can be selected from the following options: Original (applicant), Literature, Previous assessment, Previous assessment (FEEDAP Panel), and Original (EFSA)',
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
    filterDescription:
      'Describes what was investigated in the study, e.g. “absorption”, “metabolism”, or “bioavailability”. A study can have multiple investigation types.',
    showInFilters: true
  },
  'admes.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'ADME Remarks',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for ADME remarks',
    showInFilters: true
  },
  'admes.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'ADME Test Material',
    displayGroupName: 'ADME',
    type: 'text',
    djangoLookupField: 'adme__test_material',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'ADME',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for ADME Test Material',
    showInFilters: true
  },

  // genotox

  'genotoxes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Genotoxicity Test Type',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'test_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-dna',
    filterDescription:
      'Specifies the type of genotoxicity test conducted in the study, such as "bacterial reverse mutation test," "in vitro mammalian chromosome aberration test," or "in vivo micronucleus test”.',
    showInFilters: true
  },
  'genotoxes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Genotoxicity Guideline',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'guideline',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Specifies the guideline followed by the genotoxicity study, such as OECD test guidelines (e.g., OECD TG471).',
    showInFilters: true
  },
  'genotoxes.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'Genotoxicity Guideline Qualifier',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__guideline_qualifier__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'GuidelineQualifier',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Describes whether the study was conducted according to, similar to, or not according to a guideline. This field is left blank for cases when the guideline was not specified in the opinion.',
    showInFilters: true
  },
  'genotoxes.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'Genotoxicity Study Source',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__study_source__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'StudySource',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Study source can be selected from the following options: Original (applicant), Literature, Previous assessment, Previous assessment (FEEDAP Panel), and Original (EFSA)',
    showInFilters: true
  },
  'genotoxes.outcome': {
    displayName: 'Outcome',
    flattenedDisplayName: 'Genotoxicity Outcome',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__outcome',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Genotox',
    djangoLimitchoicesField: 'outcome',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-check-circle-outline',
    filterDescription:
      'Specifies the outcome of the genotoxicity test. The available options are: "Negative/Absent," "Positive/Present," and "Inconclusive".',
    showInFilters: true
  },

  'genotoxes.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Genotox Remarks',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Genotox remarks',
    showInFilters: true
  },
  'genotoxes.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'Genotox Test Material',
    displayGroupName: 'Genotox',
    type: 'text',
    djangoLookupField: 'genotox__test_material',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'Genotox',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Genotox Test Material',
    showInFilters: true
  },

  // endpoint studies

  'endpointstudies.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Toxicology - Endpoint Study Test Type',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'test_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-flask-outline',
    filterDescription:
      'Specifies the type of test conducted in the endpoint study, such as "In vitro," "Animal," or "Human clinical trial".',
    showInFilters: true
  },
  'endpointstudies.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'Endpoint Study Guideline Qualifier',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__guideline_qualifier__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'GuidelineQualifier',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline Qualifier',
    showInFilters: true
  },
  'endpointstudies.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Toxicolgy - Endpoint Study Guideline',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'guideline',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Specifies the guideline followed for the endpoint study, such as OECD guidelines (e.g. OECD TG 407)',
    showInFilters: true
  },
  'endpointstudies.species': {
    displayName: 'Species',
    flattenedDisplayName: 'Toxicology - Endpoint Study Species',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__species',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'species',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-paw',
    filterDescription:
      'Specifies the species used in the endpoint study, such as "rat," "mouse," or "human".',
    showInFilters: true
  },
  'endpointstudies.sex': {
    displayName: 'Sex',
    flattenedDisplayName: 'Toxicology - Endpoint Study Sex',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__sex',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'sex',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-gender-male-female',
    filterDescription:
      'Specifies the sex of the subjects or test animals used in the endpoint study, such as "male," "female," or "Mixed females and males".',
    showInFilters: true
  },
  'endpointstudies.studyDuration': {
    displayName: 'Study Duration',
    flattenedDisplayName: 'Toxicology - Endpoint Study Duration',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__study_duration',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription:
      'Specifies the duration of the endpoint study, expressed in time units such as days, weeks, or months.',
    showInFilters: true
  },
  'endpointstudies.durationUnit': {
    displayName: 'Study Duration Unit',
    flattenedDisplayName: 'Endpoint Study Duration Unit',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__duration_unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'duration_unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription: 'description for Study Duration Unit',
    showInFilters: true
  },
  'endpointstudies.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'Endpoint Study Source',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__study_source__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'StudySource',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Study Source',
    showInFilters: true
  },
  'endpointstudies.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Endpoint Study Remarks',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Endpoint Study Remarks',
    showInFilters: true
  },
  'endpointstudies.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'Endpoint Study Test Material',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    djangoLookupField: 'endpointstudy__test_material',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'studies',
    djangoModel: 'Endpointstudy',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Endpoint Study Test Material',
    showInFilters: true
  },

  // endpoint

  'endpointstudies.endpoints.referencePoint': {
    displayName: 'Reference Point',
    flattenedDisplayName: 'Toxicology - Endpoint Study - Reference point',
    displayGroupName: 'Endpoint',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__reference_point',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpoint',
    djangoLimitchoicesField: 'reference_point',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-target',
    filterDescription:
      'Specifies the reference point which was derived from the endpoint study, such as NOAEL or LOAEL.',
    showInFilters: true
  },
  'endpointstudies.endpoints.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Toxicology - Endpoint Study - Reference point qualifier',
    displayGroupName: 'Endpoint',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpoint',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the qualifier for the reference point, such as "greater than," "less than," or "equal to".',
    showInFilters: true
  },
  'endpointstudies.endpoints.subpopulation': {
    displayName: 'Subpopulation',
    flattenedDisplayName: 'Toxicology - Endpoint Study - Reference point subpopulation',
    displayGroupName: 'Endpoint',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__subpopulation',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpoint',
    djangoLimitchoicesField: 'subpopulation',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-account-group',
    filterDescription:
      'Specifies the subpopulation for which the reference point (e.g., LOAEL or NOAEL) was derived, such as "males," "females," or "fetus." This field is used when different reference points are determined for specific subpopulations within the study.',
    showInFilters: true
  },
  'endpointstudies.endpoints.lovalue': {
    displayName: 'Value',
    flattenedDisplayName: 'Toxicology - Endpoint Study - Reference point value',
    displayGroupName: 'Endpoint',
    type: 'number',
    djangoLookupField: 'endpointstudy__endpoints__lovalue',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-arrow-down',
    filterDescription:
      'Specifies the numerical value of the reference point (e.g. NOAEL), as determined in the endpoint study or by EFSA.',
    showInFilters: true
  },
  'endpointstudies.endpoints.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Endpoint Unit',
    displayGroupName: 'Endpoint',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpoint',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Endpoint Unit',
    showInFilters: true
  },

  // Final Outcome

  'endpointstudies.endpoints.finalOutcomes.outcome': {
    displayName: 'Outcome',
    flattenedDisplayName: 'Final Outcome Outcome',
    displayGroupName: 'Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__outcome',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'FinalOutcome',
    djangoLimitchoicesField: 'outcome',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-check-circle-outline',
    filterDescription:
      '"Specifies the final outcome derived from a reference point in the endpoint study, such as a margin of exposure (MOE), acceptable daily intake (ADI), or tolerable upper intake level (UL).',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Toxicology - Final Outcome Qualifier',
    displayGroupName: 'Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'FinalOutcome',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the qualifier for the final outcome, such as "greater than," "less than," or "equal to," in relation to the derived value (e.g., margin of exposure or safe intake level).',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Toxicology - Final Outcome Value',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__value',
    displayGroupName: 'Final Outcome',
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription:
      'Specifies the numerical value of the final outcome, such as a margin of exposure (MOE), acceptable daily intake (ADI), or tolerable upper intake level (UL), as derived by EFSA (in most cases).',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Final Outcome Unit',
    displayGroupName: 'Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'FinalOutcome',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Final Outcome Unit',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.uncertaintyFactor': {
    displayName: 'Uncertainty Factor',
    flattenedDisplayName: 'Final Outcome Uncertainty Factor',
    displayGroupName: 'Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__uncertainty_factor',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Final Outcome Uncertainty Factor',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Final Outcome Remarks',
    displayGroupName: 'Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Final Outcome Remarks',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.populations.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Toxicology - Final Outcome Population Subgroup',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__subgroup__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'Subgroup',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-account-multiple-outline',
    filterDescription:
      'Specifies the population subgroup based on age for which the final outcome is derived, such as "infants", "other children", "adolescents", "adults” (including or excluding pregnant and lactating women), or "general population." This field is used when different final outcome values are calculated for specific age-based subpopulations in the study.',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Toxicology - Final Outcome Population Qualifier',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__qualifier',
      fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the qualifier for the age of the population subgroup, such as "greater than," "less than," or "equal to," indicating the age range for which the final outcome (e.g., MOE, ADI) is applicable, such as children from 5 years of age.',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Toxicology - Final Outcome Population Value',
    displayGroupName: 'Population',
    type: 'number',
    qualifierDjangoLookupField:
    'endpointstudy__endpoints__finaloutcome__populations__population__qualifier',
    fieldType: 'tax_node',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__populations__population__value',
    upperRangeDjangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription:
      'Specifies the exact age or age range of the population subgroup (e.g., months, 18-65 years) for which the final outcome was determined.',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.upperRangeValue': {
    displayName: 'Upper Range Value',
    flattenedDisplayName: 'Final Outcome Population Upper Range Value',
    displayGroupName: 'Population',
    type: 'number',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Upper Range Value',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Final Outcome Population Unit',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__unit',
      fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Unit',
    showInFilters: true
  },

  // Novel Food Variant

  'novelFoodVariants.foodForm': {
    displayName: 'Food Form',
    flattenedDisplayName: 'Novel Food Variant Food Form',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__food_form__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'FoodForm',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Novel Food Variant Food Form',
    showInFilters: true
  },
  'novelFoodVariants.riskAssessRedFlags.title': {
    displayName: 'Title',
    flattenedDisplayName: 'Risk Assessment Red Flag',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__risk_assess_red_flags__risk_assess_red_flag__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'RiskAssessRedFlag',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Risk Assessment Red Flags',
    showInFilters: true
  },
  'novelFoodVariants.productionProcesses.process': {
    displayName: 'Production Process',
    flattenedDisplayName: 'Production Process',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__productions__process',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'ProductionNovelFoodVariant',
    djangoLimitchoicesField: 'process',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Production Process',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.useType': {
    displayName: 'Use Type',
    flattenedDisplayName: 'Proposed Use Type',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__use_type',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'ProposedUse',
    djangoField: 'use_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Proposed Use Type',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Proposed Use Remarks',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'description for Proposed Use Remarks',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Proposed Use Population Subgroup',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__subgroup__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'Subgroup',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-account-multiple-outline',
    filterDescription: 'description for Subgroup',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Proposed Use Population Qualifier',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Proposed Use Population Value',
    displayGroupName: 'Population',
    type: 'number',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Value',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.upperRangeValue': {
    displayName: 'Upper Range Value',
    flattenedDisplayName: 'Proposed Use Population Upper Range Value',
    displayGroupName: 'Population',
    type: 'number',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Upper Range Value',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Proposed Use Population Unit',
    displayGroupName: 'Population',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Unit',
    showInFilters: true
  },


  'novelFoodVariants.compositions.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Composition Value',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Value',
    showInFilters: true
  },
  'novelFoodVariants.compositions.upperRangeValue': {
    displayName: 'Upper Range Value',
    flattenedDisplayName: 'Composition Upper Range Value',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Upper Range Value',
    showInFilters: true
  },
  'novelFoodVariants.compositions.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Composition Unit',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Composition',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Unit',
    showInFilters: true
  },
  'novelFoodVariants.compositions.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Composition Qualifier',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Composition',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Qualifier',
    showInFilters: true
  },
  'novelFoodVariants.compositions.type': {
    displayName: 'Type',
    flattenedDisplayName: 'Composition Type',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__type',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'Composition',
    djangoField: 'type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Type',
    showInFilters: true
  },
  'novelFoodVariants.compositions.footnote': {
    displayName: 'Footnote',
    flattenedDisplayName: 'Composition Footnote',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__footnote',
    fieldType: 'text_field',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'Composition',
    djangoField: 'footnote',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Composition Footnote',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterTitle': {
    displayName: 'Title',
    flattenedDisplayName: 'Parameter Title',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'Parameter',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Parameter Title',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterTypeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Parameter Type',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__type__title',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'composition',
    djangoModel: 'ParameterType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Parameter Type',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterVocabId': {
    displayName: 'Vocab ID',
    flattenedDisplayName: 'Parameter Vocabulary ID',
    displayGroupName: 'Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'novel-food-values-list/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Parameter',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'description for Parameter Vocabulary ID',
    showInFilters: true
  },

  // links do django admin
  djangoAdminOpinion: {
    displayName: 'Opinion Admin',
    flattenedDisplayName: 'Opinion Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  djangoAdminNovelFood: {
    displayName: 'Novel Food Admin',
    flattenedDisplayName: 'Novel Food Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'admes.djangoAdminAdme': {
    displayName: 'ADME Admin',
    flattenedDisplayName: 'ADME Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'genotoxes.djangoAdminGenotox': {
    displayName: 'Genotox Admin',
    flattenedDisplayName: 'Genotox Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'endpointstudies.djangoAdminEndpointstudy': {
    displayName: 'Endpoint Study Admin',
    flattenedDisplayName: 'Endpoint Study Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'endpointstudies.endpoints.finalOutcomes.djangoAdminFinalOutcome': {
    displayName: 'Final Outcome Admin',
    flattenedDisplayName: 'Final Outcome Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  },
  'novelFoodVariants.djangoAdminNovelFoodVariant': {
    displayName: 'Novel Food Variant Admin',
    flattenedDisplayName: 'Novel Food Variant Admin',
    icon: 'mdi-account-cowboy-hat',
    filterDescription: 'will provide a link to django admin',
    showInFilters: false
  }
}
