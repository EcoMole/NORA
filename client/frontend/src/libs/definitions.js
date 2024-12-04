export const objectTypes = {
  allergenicities: {
    displayName: 'Allergenicity',
    displayGroupName: 'Allergenicity',
    showInFilters: true,
    djangoLookupFilter: 'allergenicities__allergenicity',
    djangoApp: 'novel_food',
    djangoModel: 'Allergenicity'
  },
  synonyms: {
    displayName: 'Novel Food Synonym',
    displayGroupName: 'Synonym',
    showInFilters: true,
    djangoLookupFilter: 'synonyms',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodSyn'
  },
  panels: {
    displayName: 'Panel',
    displayGroupName: 'Administrative',
    showInFilters: true,
    djangoLookupFilter: 'opinion__panels__panel',
    djangoApp: 'administrative',
    djangoModel: 'Panel'
  },
  sciOfficers: {
    displayName: 'Scientific Officer',
    displayGroupName: 'Administrative',
    showInFilters: true,
    djangoLookupFilter: 'opinion__sci_officers__sci_officer',
    djangoApp: 'administrative',
    djangoModel: 'ScientificOfficer'
  },
  questions: {
    displayName: 'Question',
    displayGroupName: 'Question',
    showInFilters: true,
    djangoLookupFilter: 'opinion__questions__question',
    djangoApp: 'administrative',
    djangoModel: 'Question'
  },
  'questions.applicants': {
    displayName: 'Applicant',
    displayGroupName: 'Applicant',
    showInFilters: true,
    djangoLookupFilter: 'opinion__questions__question__applicants__applicant',
    djangoApp: 'administrative',
    djangoModel: 'Applicant'
  },
  'questions.mandates': {
    displayName: 'Mandate',
    displayGroupName: 'Mandate',
    showInFilters: true,
    djangoLookupFilter: 'opinion__questions__question__mandates',
    djangoApp: 'administrative',
    djangoModel: 'Mandate'
  },
  foodCategories: {
    displayName: 'Food Category',
    displayGroupName: 'Novel Food',
    showInFilters: true,
    djangoLookupFilter: 'food_categories__food_category',
    djangoApp: 'novel_food',
    djangoModel: 'FoodCategory'
  },
  novelFoodCategories: {
    displayName: 'Novel Food Category',
    displayGroupName: 'Novel Food',
    showInFilters: true,
    djangoLookupFilter: 'novel_food_categories__novel_food_category',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodCategory'
  },
  admes: {
    displayName: 'ADME',
    displayGroupName: 'ADME',
    showInFilters: true,
    djangoLookupFilter: 'adme',
    djangoApp: 'studies',
    djangoModel: 'ADME'
  },
  'admes.investigationTypes': {
    displayName: 'Investigation Type',
    displayGroupName: 'ADME',
    showInFilters: true,
    djangoLookupFilter: 'adme__investigation_types__investigation_type',
    djangoApp: 'studies',
    djangoModel: 'InvestigationType'
  },
  genotoxes: {
    displayName: 'Genotox',
    displayGroupName: 'Genotox',
    showInFilters: true,
    djangoLookupFilter: 'genotox',
    djangoApp: 'studies',
    djangoModel: 'Genotox'
  },
  endpointstudies: {
    displayName: 'Endpoint Study',
    displayGroupName: 'Endpoint Study',
    showInFilters: true,
    djangoLookupFilter: 'endpointstudy',
    djangoApp: 'studies',
    djangoModel: 'Endpointstudy'
  },
  'endpointstudies.endpoints': {
    displayName: 'Endpoint',
    displayGroupName: 'Endpoint',
    showInFilters: true,
    djangoLookupFilter: 'endpointstudy__endpoints',
    djangoApp: 'studies',
    djangoModel: 'Endpoint'
  },
  'endpointstudies.endpoints.finalOutcomes': {
    displayName: 'Final Outcome',
    displayGroupName: 'Final Outcome',
    showInFilters: true,
    djangoLookupFilter: 'endpointstudy__endpoints__finaloutcome',
    djangoApp: 'studies',
    djangoModel: 'FinalOutcome'
  },
  'endpointstudies.endpoints.finalOutcomes.populations': {
    displayName: 'Population',
    displayGroupName: 'Population',
    showInFilters: true,
    djangoLookupFilter: 'endpointstudy__endpoints__finaloutcome__populations__population',
    djangoApp: 'taxonomies',
    djangoModel: 'Population'
  },
  novelFoodVariants: {
    displayName: 'Novel Food Variant',
    displayGroupName: 'Novel Food Variant',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant',
    djangoApp: 'composition',
    djangoModel: 'NovelFoodVariant'
  },
  'novelFoodVariants.riskAssessRedFlags': {
    displayName: 'Risk Assessment Red Flag',
    displayGroupName: 'Production process of Novel Food Variant',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant__risk_assess_red_flags__risk_assess_red_flag',
    djangoApp: 'composition',
    djangoModel: 'RiskAssessRedFlag'
  },
  'novelFoodVariants.productionProcesses': {
    displayName: 'Production Process',
    displayGroupName: 'Production process of Novel Food Variant',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant__productions',
    djangoApp: 'composition',
    djangoModel: 'ProductionNovelFoodVariant'
  },
  'novelFoodVariants.proposedUses': {
    displayName: 'Proposed Use',
    displayGroupName: 'Proposed Use of Novel Food Variant',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant__proposed_uses',
    djangoApp: 'composition',
    djangoModel: 'ProposedUse'
  },
  'novelFoodVariants.proposedUses.population': {
    displayName: 'Proposed Uses Population',
    displayGroupName: 'Proposed Use Population Subgroup',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant__proposed_uses__population',
    djangoApp: 'taxonomies',
    djangoModel: 'Population'
  },
  'novelFoodVariants.compositions': {
    displayName: 'Composition',
    displayGroupName: 'Novel Food Variant Composition',
    showInFilters: true,
    djangoLookupFilter: 'novelfoodvariant__compositions',
    djangoApp: 'composition',
    djangoModel: 'Composition'
  },
  organisms: {
    displayName: 'Organism',
    displayGroupName: 'Identity',
    showInFilters: true,
    djangoLookupFilter: 'organisms',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodOrganism'
  },
  'organisms.species': {
    displayName: 'Taxonomy',
    displayGroupName: 'Identity',
    showInFilters: true,
    djangoLookupFilter: 'organisms__organism__species',
    djangoApp: 'novel_food',
    djangoModel: 'Species'
  },
  'organisms.orgSynonyms': {
    displayName: 'Organism Synonym',
    displayGroupName: 'Synonym',
    showInFilters: true,
    djangoLookupFilter: 'organisms__organism__synonyms',
    djangoApp: 'novel_food',
    djangoModel: 'OrganismSyn'
  },
  chemicals: {
    displayName: 'Chemical',
    displayGroupName: 'Identity',
    showInFilters: true,
    djangoLookupFilter: 'chemicals',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodChemical'
  },
  'chemicals.chemSynonyms': {
    displayName: 'Chemical Synonym',
    displayGroupName: 'Synonym',
    showInFilters: true,
    djangoLookupFilter: 'chemicals__chemical__synonyms',
    djangoApp: 'novel_food',
    djangoModel: 'ChemicalSyn'
  },
  'chemicals.chemDescriptors': {
    displayName: 'Chemical Descriptor',
    displayGroupName: 'Chemical',
    showInFilters: true,
    djangoLookupFilter: 'chemicals__chemical__chem_descriptors',
    djangoApp: 'novel_food',
    djangoModel: 'ChemDescriptor'
  },
  specificToxicities: {
    displayName: 'Specific Toxicity',
    displayGroupName: 'Hazards',
    showInFilters: true,
    djangoLookupFilter: 'specific_toxicities',
    djangoApp: 'novel_food',
    djangoModel: 'SpecificToxicity'
  },
  substancesOfConcern: {
    displayName: 'Substance of Concern',
    displayGroupName: 'Hazards',
    showInFilters: true,
    djangoLookupFilter: 'substances_of_concern',
    djangoApp: 'novel_food',
    djangoModel: 'SubstanceOfConcernNovelFood'
  },
  backgroundExposureAssessments: {
    displayName: 'Background Exposure Assessment',
    displayGroupName: 'Nutrition',
    showInFilters: true,
    djangoLookupFilter: 'bg_expo_assessments',
    djangoApp: 'novel_food',
    djangoModel: 'BackgroundExposureAssessment'
  },
  hbgvs: {
    displayName: 'HBGV',
    displayGroupName: 'Hazards',
    showInFilters: true,
    djangoLookupFilter: 'hbgvs',
    djangoApp: 'novel_food',
    djangoModel: 'HBGV'
  }
}

export const novelFoodAndOpinionFields = {
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
    fieldType: 'tax_node',
    djangoLookupField: 'protein_digestibility',
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
    flattenedDisplayName: 'Nutrition - Antinutritional factors',
    type: 'text',

    djangoLookupField: 'antinutritional_factors',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',

    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'antinutritional_factors',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-stomach',
    filterDescription:
      'Indicates whether antinutritional factors (substances that may interfere with nutrient absorption or have negative health effects, e.g. tannins or phytic acid) are discussed in the Novel Food assessment.',
    showInFilters: true
  },
  hasNutriDisadvantage: {
    displayName: 'Nutritional Disadvantage',
    displayGroupName: 'Novel Food',
    flattenedDisplayName: 'Nutrition - Nutritional Disadvantage',
    type: 'text',
    djangoLookupField: 'has_nutri_disadvantage',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFood',
    djangoLimitchoicesField: 'has_nutri_disadvantage',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-stomach',
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
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Sufficient Data',
    type: 'text',
    djangoLookupField: 'sufficient_data',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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
    apiEndpoint: 'picklist/',
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

  // opinion

  opinionDocumentType: {
    displayName: 'Opinion Document Type',
    displayGroupName: 'Opinion',
    type: 'text',
    djangoLookupField: 'opinion__document_type',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
  }
}

export const fields = {
  'allergenicities.title': {
    displayName: '',
    flattenedDisplayName: 'Allergenicity',
    type: 'text',
    djangoLookupField: 'allergenicities__allergenicity__title',
    apiEndpoint: 'picklist/',
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
    flattenedDisplayName: 'Hazards - Specific Toxicity',
    type: 'text',
    djangoLookupField: 'specific_toxicities__specific_toxicity',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'SpecificToxicity',
    djangoLimitchoicesField: 'specific_toxicity',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      "Indicates whether specific toxicity, such as hepatotoxicity, nephrotoxicity, or neurotoxicity, was discussed in the NF/TF opinion's discussion section. If no specific toxicity is associated with the Novel or Traditional Food, this field will be set to NONE (TOX14A).",
    showInFilters: true
  },
  'substancesOfConcern.substanceOfConcern': {
    displayName: '',
    flattenedDisplayName: 'Hazards - Substance of Concern',
    type: 'text',
    djangoLookupField: 'substances_of_concern__substance_of_concern',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'SubstanceOfConcernNovelFood',
    djangoLimitchoicesField: 'substance_of_concern',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      "Specifies the substances of concern, such as contaminants, heavy metals, or pesticide residues, discussed in the Novel Food opinion's discussion section. This field is left blank if no substances of concern were identified.",
    showInFilters: true
  },
  'backgroundExposureAssessments.compOfInterest': {
    displayName: 'Background exposure assess.',
    flattenedDisplayName: 'Nutrition - Background Exposure Assessment',
    type: 'text',
    djangoLookupField: 'bg_expo_assessments__comp_of_interest',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'BackgroundExposureAssessment',
    djangoLimitchoicesField: 'comp_of_interest',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale-balance',
    filterDescription:
      'Specifies the substances for which background exposure was assessed, indicating the baseline dietary exposure levels considered in the NF/TF assessment. This field is left blank if no background exposure assessment was conducted. ',
    showInFilters: true
  },
  'hbgvs.type': {
    displayName: 'Type',
    flattenedDisplayName: 'Hazards - HBGV Type',
    type: 'text',
    djangoLookupField: 'hbgvs__type',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      'Specifies the type of Health-Based Guidance Value (HBGV) considered in the NF/TF assessment, such as Acceptable Daily Intake (ADI), Tolerable Daily Intake (TDI), or Reference Dose (RfD)."',
    showInFilters: true
  },
  'hbgvs.exceeded': {
    displayName: 'Exceeded',
    flattenedDisplayName: 'Hazards - HBGV Exceeded',
    type: 'text',
    djangoLookupField: 'hbgvs__exceeded',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'exceeded',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      'Indicates whether the estimated intake of the NF/TF exceeds the established Health-Based Guidance Value (HBGV), such as the Acceptable Daily Intake (ADI) or Tolerable Daily Intake (TDI).',
    showInFilters: true
  },
  'hbgvs.substance': {
    displayName: 'Substance',
    flattenedDisplayName: 'Hazards - HBGV Substance',
    type: 'text',
    djangoLookupField: 'hbgvs__substance',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'HBGV',
    djangoLimitchoicesField: 'substance',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-outline',
    filterDescription:
      'Specifies the substance for which a Health-Based Guidance Value (HBGV) was considered in the NF/TF assessment.',
    showInFilters: true
  },

  // Novel Food Synonyms

  'synonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Novel Food Synonym',
    type: 'text',
    djangoLookupField: 'synonyms__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Specifies alternative names or synonyms for the NF/TF, including common names and trade names.',
    showInFilters: true
  },
  'synonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Novel Food Synonym Type',
    type: 'text',
    djangoLookupField: 'synonyms__syn_type__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'Specifies whether the type of synonym is a common name or trade name.',
    showInFilters: true
  },
  'synonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Novel Food Synonym Type Definition',
    type: 'text',
    djangoLookupField: 'synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Novel Food Synonym Type Definition',
    showInFilters: true
  },

  'panels.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Opinion - Panel',
    type: 'text',
    djangoLookupField: 'opinion__panels__panel__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'opinion__questions__question__number',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'Question number of the opinion/technical report, e.g., EFSA-Q-2018-00373',
    showInFilters: true
  },

  'questions.applicants.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Opinion - Applicant',
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
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__mandate_type__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__mandate_type__definition',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type Definition',
    showInFilters: true
  },
  'questions.mandates.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Opinion - Mandate Regulation',
    type: 'text',
    djangoLookupField: 'opinion__questions__question__mandates__regulation',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    flattenedDisplayName: 'Food Category Tool Name',
    type: 'text',
    djangoLookupField: 'food_categories__food_category__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'FoodCategory',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-circle-outline',
    filterDescription:
      'Specifies if the FAIM, FoodEx, or both food category tools were used in the assessment.',
    showInFilters: true
  },
  'foodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Food Category Definition',
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
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'novel_food_categories__novel_food_category__regulation',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    flattenedDisplayName: 'Identity - Organism Vocab ID',
    type: 'text',
    djangoLookupField: 'organisms__organism__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'Organism',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Specifies the entry from the MTX vocabulary used to classify the source organism of the NF/TF.',
    showInFilters: true
  },
  'organisms.orgPart': {
    displayName: 'Part',
    flattenedDisplayName: 'Identity - Organism Part',
    type: 'text',
    djangoLookupField: 'organisms__org_part',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'org_part',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Specifies the part of the organism used in the NF/TF, such as "leaf," "root," "seed," or "whole organism."',
    showInFilters: true
  },
  'organisms.variant': {
    displayName: 'Variant',
    flattenedDisplayName: 'Identity - Organism Variant',
    type: 'text',
    djangoLookupField: 'organisms__variant',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodOrganism',
    djangoField: 'variant',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Specifies the variant of the organism used for the production of the NF/TF, such as strain (microorganisms), subspecies (animals), or cultivar (plants). ',
    showInFilters: true
  },
  'organisms.isGmo': {
    displayName: 'is GMO',
    flattenedDisplayName: 'Identity - Organism is GMO',
    type: 'text',
    djangoLookupField: 'organisms__is_gmo',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'is_gmo',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Indicates whether the organism used in the NF/TF has been genetically modified (GMO). Options include "Yes" for genetically modified organisms, "No" for non-GMOs, and "Unknown" if the GMO status is not specified.',
    showInFilters: true
  },
  'organisms.hasQps': {
    displayName: 'has QPS',
    flattenedDisplayName: 'Identity - Organism has QPS',
    type: 'text',
    djangoLookupField: 'organisms__has_qps',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'has_qps',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Indicates whether the organism used in the NF/TF has Qualified Presumption of Safety (QPS) status, which is granted by EFSA for certain microorganisms deemed safe for use. Options include "Yes" if the organism has QPS status, "No" if it does not, and "Unknown" if the QPS status is not specified. Only applicable for microorganisms.',
    showInFilters: true
  },

  'organisms.cellCulture': {
    displayName: 'Cell Culture',
    flattenedDisplayName: 'Identity - Organism Cell Culture',
    type: 'text',
    djangoLookupField: 'organisms__cell_culture',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'NovelFoodOrganism',
    djangoField: 'cell_culture',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Indicates the type of cell culture that the NF/TF was derived from. Only applicable to cell or tissue cultures.',
    showInFilters: true
  },

  'organisms.cellsModified': {
    displayName: 'Cells Modified',
    flattenedDisplayName: 'Identity - Organism Cell Modification',
    type: 'text',
    djangoLookupField: 'organisms__cells_modified',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'NovelFoodOrganism',
    djangoLimitchoicesField: 'cells_modified',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Indicates whether the cells used in the NF/TF were modified, such as “pluripotent stem cells”. Only applicable to cell or tissue cultures.',
    showInFilters: true
  },
  'organisms.species.name': {
    displayName: 'Species Name',
    flattenedDisplayName: 'Identity - Species Name',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__name',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'Species',
    djangoField: 'name',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-tree-outline',
    filterDescription:
      'Specifies the species name of the organism used in the NF/TF, following scientific nomenclature (e.g., Escherichia coli, Saccharomyces cerevisiae). ',
    showInFilters: true
  },
  'organisms.species.scientificName': {
    displayName: 'Identity - Organism Scientific Name',
    flattenedDisplayName: 'Identity - Species Scientific Name',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__scientific_name',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'Species',
    djangoField: 'scientific_name',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-tree-outline',
    filterDescription:
      'Specifies the full scientific name of the species used in the NF/TF, including genus, species, and the authority who named the species (e.g., Salvia hispanica L., Cryptops ulomoides (Solier, 1851).',
    showInFilters: true
  },
  'organisms.species.genus': {
    displayName: 'Genus',
    flattenedDisplayName: 'Identity - Species Genus',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'Genus',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-tree-outline',
    filterDescription:
      'Specifies the genus of the species used in the NF/TF, representing the broader taxonomic category to which the organism belongs (e.g., Lactobacillus, Salvia). ',
    showInFilters: true
  },
  'organisms.species.family': {
    displayName: 'Family',
    flattenedDisplayName: 'Identity - Species Family',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__family__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'Family',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-tree-outline',
    filterDescription:
      'Specifies the family of the species used in the NF/TF, representing a higher taxonomic classification above the genus (e.g., Poaceae, Lamiaceae).',
    showInFilters: true
  },
  'organisms.species.orgType': {
    displayName: 'Organism Type',
    flattenedDisplayName: 'Identity - Species Organism Type',
    type: 'text',
    djangoLookupField: 'organisms__organism__species__genus__family__org_type__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'OrgType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-file-tree-outline',
    filterDescription:
      'Specifies the broad biological category of the source organism used in the NF/TF, such as “Bacteria”, “Fungi”, “Plant”, or “Animal”.',
    showInFilters: true
  },
  'organisms.orgSynonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Identity - Organism Synonym',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'OrganismSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Specifies alternative names or synonyms for the organism used in the NF/TF, such as common names. ',
    showInFilters: true
  },
  'organisms.orgSynonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Identity - Organism Synonym Type',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__syn_type__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription:
      'Specifies the type of synonym provided for the organism used in the NF/TF, such as common name, or synonym',
    showInFilters: true
  },
  'organisms.orgSynonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Organism Synonym Type Definition',
    type: 'text',
    djangoLookupField: 'organisms__organism__synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-leaf',
    filterDescription: 'description for Organism Synonym Type Definition',
    showInFilters: true
  },

  'chemicals.chemical': {
    displayName: 'Vocab ID',
    flattenedDisplayName: 'Identity - Chemical Vocab ID',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'novel_food',
    djangoLimitchoicesModel: 'Chemical',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription:
      'Specifies the entry from the PARAM vocabulary used to classify the source substance of the NF/TF.',
    showInFilters: true
  },
  'chemicals.chemSynonyms.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Identity - Chemical Synonym',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'ChemicalSyn',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription:
      'Specifies alternative names or synonyms for the chemical component in the NF/TF, including common names, or synonyms',
    showInFilters: true
  },
  'chemicals.chemSynonyms.typeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Identity - Chemical Synonym Type',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__syn_type__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'SynonymType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription:
      'Specifies the type of synonym provided for the chemical used in the NF/TF, such as "common name" or "synonym"',
    showInFilters: true
  },
  'chemicals.chemSynonyms.typeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Chemical Synonym Type Definition',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__synonyms__syn_type__definition',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription: 'description for Chemical Synonym Type Definition',
    showInFilters: true
  },
  'chemicals.chemDescriptors.type': {
    displayName: 'Type',
    flattenedDisplayName: 'Identity - Chemical Descriptor Type',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__chem_descriptors__type',
    apiEndpoint: 'picklist/',
    djangoApp: 'novel_food',
    djangoModel: 'ChemDescriptor',
    djangoField: 'type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription:
      'Specifies the type of additional descriptors for the chemical component in the NF/TF that were not included in the PARAM catalogue, such as unique identifiers or structural information.',
    showInFilters: true
  },
  'chemicals.chemDescriptors.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Identity -  Chemical Descriptor Value',
    type: 'text',
    djangoLookupField: 'chemicals__chemical__chem_descriptors__value',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-molecule',
    filterDescription:
      'Provides the specific value for additional chemical descriptors not found in the PARAM catalogue, such as a unique identifier, molecular formula, or specific structural data.',
    showInFilters: true
  },

  // adme

  'admes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'ADME Test Type',
    type: 'text',
    djangoLookupField: 'adme__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'adme__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'adme__guideline_qualifier__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'adme__study_source__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'adme__investigation_types__investigation_type__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'adme__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Provides additional comments or context regarding the ADME study for the NF/TF',
    showInFilters: true
  },
  'admes.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'ADME Test Material',
    type: 'text',
    djangoLookupField: 'adme__test_material',
    apiEndpoint: 'picklist/',
    djangoApp: 'studies',
    djangoModel: 'ADME',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Specifies the test material used in the ADME study for the NF/TF, such as the specific form or preparation of the substance tested.',
    showInFilters: true
  },

  // genotox

  'genotoxes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Genotoxicity Test Type',
    type: 'text',
    djangoLookupField: 'genotox__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'genotox__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'genotox__guideline_qualifier__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'genotox__study_source__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'genotox__outcome',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    flattenedDisplayName: 'Genotoxicity Remarks',
    type: 'text',
    djangoLookupField: 'genotox__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Provides additional comments or context regarding the genotoxicity study for the NF/TF',
    showInFilters: true
  },
  'genotoxes.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'Genotoxicity Test Material',
    type: 'text',
    djangoLookupField: 'genotox__test_material',
    apiEndpoint: 'picklist/',
    djangoApp: 'studies',
    djangoModel: 'Genotox',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Specifies the test material used in the genotoxicity study for the NF/TF, such as the specific form or preparation of the substance tested.',
    showInFilters: true
  },

  // endpoint studies

  'endpointstudies.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Toxicology - Endpoint Study Test Type',
    type: 'text',
    djangoLookupField: 'endpointstudy__test_type',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'endpointstudy__guideline_qualifier__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'GuidelineQualifier',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'Describes whether the study was conducted according to, similar to, or not according to a guideline. This field is left blank for cases when the guideline was not specified in the opinion.',
    showInFilters: true
  },
  'endpointstudies.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Toxicology - Endpoint Study Guideline',
    type: 'text',
    djangoLookupField: 'endpointstudy__guideline',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'endpointstudy__species',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'endpointstudy__sex',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    flattenedDisplayName: 'Toxicology - Endpoint Study Duration Unit',
    type: 'text',
    djangoLookupField: 'endpointstudy__duration_unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpointstudy',
    djangoLimitchoicesField: 'duration_unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-clock-outline',
    filterDescription: 'Study Duration Unit',
    showInFilters: true
  },
  'endpointstudies.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'Toxicology - Endpoint Study Source',
    type: 'text',
    djangoLookupField: 'endpointstudy__study_source__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'studies',
    djangoModel: 'StudySource',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Study source can be selected from the following options: Original (applicant), Literature, Previous assessment, Previous assessment (FEEDAP Panel), and Original (EFSA).',
    showInFilters: true
  },
  'endpointstudies.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Toxicology - Endpoint Study Remarks',
    type: 'text',
    djangoLookupField: 'endpointstudy__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Provides additional comments or context regarding the endpoint study for the NF/TF',
    showInFilters: true
  },
  'endpointstudies.testMaterial': {
    displayName: 'Test Material',
    flattenedDisplayName: 'Toxicology - Endpoint Study Test Material',
    type: 'text',
    djangoLookupField: 'endpointstudy__test_material',
    apiEndpoint: 'picklist/',
    djangoApp: 'studies',
    djangoModel: 'Endpointstudy',
    djangoField: 'test_material',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-outline',
    filterDescription:
      'Specifies the test material used in the endpoint study for the NF/TF, such as the specific form or preparation of the substance tested.',
    showInFilters: true
  },

  // endpoint

  'endpointstudies.endpoints.referencePoint': {
    displayName: 'Reference Point',
    flattenedDisplayName: 'Toxicology - Endpoint - Reference point',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__reference_point',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
  'endpointstudies.endpoints.subpopulation': {
    displayName: 'Subpopulation',
    flattenedDisplayName: 'Toxicology - Endpoint - Reference point subpopulation',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__subpopulation',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
  'endpointstudies.endpoints.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Toxicology - Endpoint - Reference point qualifier',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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

  'endpointstudies.endpoints.lovalue': {
    displayName: 'Value',
    flattenedDisplayName: 'Toxicology - Endpoint - Reference point value',
    type: 'number',
    djangoLookupField: 'endpointstudy__endpoints__lovalue',
    fieldType: 'value_field',
    valueFields: {
      djangoApp: 'studies',
      djangoModel: 'Endpoint',
      qualifierField: 'qualifier',
      valueField: 'lovalue'
    },
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-arrow-down',
    filterDescription:
      'Specifies the numerical value of the reference point (e.g. NOAEL), as determined in the endpoint study or by EFSA.',
    showInFilters: true
  },
  'endpointstudies.endpoints.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Toxicology - Endpoint - Unit',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'Endpoint',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the unit of the numerical value of the reference point (e.g. NOAEL).',
    showInFilters: true
  },

  // Final Outcome

  'endpointstudies.endpoints.finalOutcomes.outcome': {
    displayName: 'Outcome',
    flattenedDisplayName: 'Toxicology - Final Outcome',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__outcome',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    fieldType: 'value_field',
    valueFields: {
      djangoApp: 'studies',
      djangoModel: 'FinalOutcome',
      qualifierField: 'qualifier',
      valueField: 'value'
    },
    type: 'number',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription:
      'Specifies the numerical value of the final outcome, such as a margin of exposure (MOE), acceptable daily intake (ADI), or tolerable upper intake level (UL), as derived by EFSA (in most cases).',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Toxicology - Final Outcome Unit',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'studies',
    djangoLimitchoicesModel: 'FinalOutcome',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the unit of the numerical value of the final outcome (e.g. safe level).',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.uncertaintyFactor': {
    displayName: 'Uncertainty Factor',
    flattenedDisplayName: 'Toxicology - Final Outcome Uncertainty Factor',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__uncertainty_factor',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the uncertainty factor applied to the reference point from the endpoint study to reach the final outcome, accounting for variability or gaps in data to ensure safety (e.g., an uncertainty factor of 10 for interspecies differences)',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.remarks': {
    displayName: 'Remarks',
    flattenedDisplayName: 'Toxicology - Final Outcome Remarks',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription:
      'Provides additional comments or context regarding the Final outcome for the NF/TF',
    showInFilters: true
  },

  'endpointstudies.endpoints.finalOutcomes.populations.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Toxicology - Final Outcome Population Subgroup',
    type: 'text',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__subgroup__title',
    apiEndpoint: 'picklist/',
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
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__populations__population__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
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
    type: 'number',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__populations__population__value',
    fieldType: 'value_field',
    valueFields: {
      djangoApp: 'taxonomies',
      djangoModel: 'Population',
      qualifierField: 'qualifier',
      valueField: 'value',
      upperRangeValueField: 'upper_range_value'
    },
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription:
      'Numerical value that specifies the age or lower part of an age range of the population subgroup for which the final outcome was determined.',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.upperRangeValue': {
    displayName: 'Upper Range Value',
    flattenedDisplayName: 'Toxicology - Final Outcome Population Upper Range Value',
    type: 'number',
    djangoLookupField:
      'endpointstudy__endpoints__finaloutcome__populations__population__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription:
      'Value representing the upper limit of the age range of the population subgroup for which the final outcome was determined.',
    showInFilters: true
  },
  'endpointstudies.endpoints.finalOutcomes.populations.unit': {
    displayName: 'Unit',
    flattenedDisplayName: 'Final Outcome Population Unit',
    type: 'text',
    djangoLookupField: 'endpointstudy__endpoints__finaloutcome__populations__population__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription:
      'Specifies the unit of measurement for the age of the population subgroup in the final outcome, such as "years" or "months."',
    showInFilters: true
  },

  // Novel Food Variant

  'novelFoodVariants.foodForm': {
    displayName: 'Food Form',
    flattenedDisplayName: 'Novel Food Variant Food Form',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__food_form__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'FoodForm',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-rice',
    filterDescription: 'variant or food form of Novel Food',
    showInFilters: true
  },
  'novelFoodVariants.riskAssessRedFlags.title': {
    displayName: 'Production process Risk Assessment Red flag',
    flattenedDisplayName: 'Production process Risk Assessment Red Flag',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__risk_assess_red_flags__risk_assess_red_flag__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'RiskAssessRedFlag',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-alert-circle',
    filterDescription: 'possible Red Flags in the production process',
    showInFilters: true
  },
  'novelFoodVariants.productionProcesses.process': {
    displayName: 'Production Process',
    flattenedDisplayName: 'Production Process of Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__productions__process',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'ProductionNovelFoodVariant',
    djangoLimitchoicesField: 'process',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-factory',
    filterDescription: 'Process in Production of Novel Food Variant',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.useType': {
    displayName: 'Proposed Use Type',
    flattenedDisplayName: 'Proposed Use of Novel Food Variant',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__use_type',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'ProposedUse',
    djangoField: 'use_type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-pill',
    filterDescription: 'Uses of Novel Food Variant proposed by applicant',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.remarks': {
    displayName: 'Remarks for Proposed Use',
    flattenedDisplayName: 'Proposed Use - Remarks',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__remarks',
    fieldType: 'text_field',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'Remarks for Proposed Use of Novel Food Variants',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Proposed Use - Population Subgroup',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__subgroup__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'Subgroup',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-account-multiple-outline',
    filterDescription: 'Subgroup of population for Proposed Use',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.qualifier': {
    displayName: 'Age Qualifier',
    flattenedDisplayName: 'Proposed Use - Qualifier for Age Value of Population Subgroup',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'Qualifier for Age Value of Proposed Use Population Subgroup',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.value': {
    displayName: 'Age Value',
    flattenedDisplayName: 'Proposed Use - Age Value of Population Subgroup',
    type: 'number',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__value',
    fieldType: 'value_field',
    valueFields: {
      djangoApp: 'taxonomies',
      djangoModel: 'Population',
      qualifierField: 'qualifier',
      valueField: 'value',
      upperRangeValueField: 'upper_range_value'
    },
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'Age Value of Proposed Use Population Subgroup',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.upperRangeValue': {
    displayName: 'Upper Range Age Value',
    flattenedDisplayName: 'Proposed Use - Upper Range Age Value of Population Subgroup',
    type: 'number',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'Upper Range Age Value of Proposed Use Population Subgroup',
    showInFilters: true
  },
  'novelFoodVariants.proposedUses.population.unit': {
    displayName: 'Age Value Unit',
    flattenedDisplayName: 'Proposed Use - Unit for Age Value of Population Subgroup',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__proposed_uses__population__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'taxonomies',
    djangoLimitchoicesModel: 'Population',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'Unit for Age Value of Proposed Use Population Subgroup',
    showInFilters: true
  },
  'novelFoodVariants.compositions.qualifier': {
    displayName: 'Value Qualifier',
    flattenedDisplayName: 'Composition Value Qualifier',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__qualifier',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Composition',
    djangoLimitchoicesField: 'qualifier',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'Qualifier for Composition Value',
    showInFilters: true
  },
  'novelFoodVariants.compositions.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Composition Value',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__value',
    fieldType: 'value_field',
    valueFields: {
      djangoApp: 'composition',
      djangoModel: 'Composition',
      qualifierField: 'qualifier',
      valueField: 'value',
      upperRangeValueField: 'upper_range_value'
    },
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'Value of Composition component',
    showInFilters: true
  },
  'novelFoodVariants.compositions.upperRangeValue': {
    displayName: 'Upper Range Value',
    flattenedDisplayName: 'Composition Upper Range Value',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__upper_range_value',
    qualifiers: ['is', 'is greater than', 'is less than', 'is None'],
    icon: 'mdi-numeric',
    filterDescription: 'Upper Range Value of Composition component',
    showInFilters: true
  },
  'novelFoodVariants.compositions.unit': {
    displayName: 'Value Unit',
    flattenedDisplayName: 'Composition Value Unit',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__unit',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Composition',
    djangoLimitchoicesField: 'unit',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-scale',
    filterDescription: 'Unit for Composition Value',
    showInFilters: true
  },

  'novelFoodVariants.compositions.type': {
    displayName: 'Composition Type',
    flattenedDisplayName: 'Composition Type',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__type',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'Composition',
    djangoField: 'type',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-beaker',
    filterDescription: 'Novel Food Variant Composition Type',
    showInFilters: true
  },
  'novelFoodVariants.compositions.footnote': {
    displayName: 'Footnote',
    flattenedDisplayName: 'Composition Footnote',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__footnote__text_field',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'Composition',
    djangoField: 'footnote',
    qualifiers: ['contains', 'is', 'is None'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'Footnote for Composition of Novel Food Variant',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterTitle': {
    displayName: 'Parameter',
    flattenedDisplayName: 'Composition - Parameter',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'Parameter',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-test-tube',
    filterDescription: 'Title of Composition Parameter',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterTypeTitle': {
    displayName: 'Parameter Type',
    flattenedDisplayName: 'Composition - Parameter Type',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__type__title',
    apiEndpoint: 'picklist/',
    djangoApp: 'composition',
    djangoModel: 'ParameterType',
    djangoField: 'title',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-beaker',
    filterDescription: 'Composition Parameter Type',
    showInFilters: true
  },
  'novelFoodVariants.compositions.parameterVocabId': {
    displayName: 'Parameter Vocab ID',
    flattenedDisplayName: 'Composition - Parameter Vocabulary ID',
    type: 'text',
    djangoLookupField: 'novelfoodvariant__compositions__parameter__vocab_id',
    fieldType: 'tax_node',
    apiEndpoint: 'picklist/',
    djangoApp: 'taxonomies',
    djangoModel: 'TaxonomyNode',
    djangoField: 'short_name',
    djangoLimitchoicesApp: 'composition',
    djangoLimitchoicesModel: 'Parameter',
    djangoLimitchoicesField: 'vocab_id',
    qualifiers: ['is', 'is None'],
    icon: 'mdi-book-open-outline',
    filterDescription:
      'This field is only used for Composition Parameter that already exist in the catalogue',
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

export const preselectGroups = {
  'endpointstudies.endpoints.finalOutcomes.value': [
    'endpointstudies.endpoints.finalOutcomes.qualifier',
    'endpointstudies.endpoints.finalOutcomes.value',
    'endpointstudies.endpoints.finalOutcomes.unit'
  ],
  'endpointstudies.endpoints.finalOutcomes.populations.value': [
    'endpointstudies.endpoints.finalOutcomes.populations.qualifier',
    'endpointstudies.endpoints.finalOutcomes.populations.value',
    'endpointstudies.endpoints.finalOutcomes.populations.upperRangeValue',
    'endpointstudies.endpoints.finalOutcomes.populations.unit'
  ],
  'novelFoodVariants.proposedUses.population.value': [
    'novelFoodVariants.proposedUses.population.qualifier',
    'novelFoodVariants.proposedUses.population.value',
    'novelFoodVariants.proposedUses.population.upperRangeValue',
    'novelFoodVariants.proposedUses.population.unit'
  ],
  'novelFoodVariants.compositions.value': [
    'novelFoodVariants.compositions.qualifier',
    'novelFoodVariants.compositions.value',
    'novelFoodVariants.compositions.upperRangeValue',
    'novelFoodVariants.compositions.unit'
  ]
}
