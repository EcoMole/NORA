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
    qualifiers: ['is', 'greater than', 'less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for ID',
    tooltipDescription: 'ID tooltip description'
  },

  nfCode: {
    displayName: 'Code',
    flattenedDisplayName: 'Novel Food Code',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-rice',
    filterDescription: 'description for Code',
    tooltipDescription: 'Code tooltip description'
  },
  title: {
    displayName: 'Title',
    flattenedDisplayName: 'Novel Food Title',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-rice',
    filterDescription: 'description for Title',
    tooltipDescription: 'Title tooltip description'
  },
  toxStudyRequired: {
    displayName: 'Toxicology Study Required',
    displayGroupName: 'Toxicology',
    apiEndpoint: 'tox-study-required/',
    qualifiers: ['is'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Toxicology Study Required',
    tooltipDescription: 'Toxicology Study Required tooltip description'
  },
  genotoxFinalOutcome: {
    displayName: 'Genotoxicity Final Outcome',
    displayGroupName: 'Novel Food',
    type: 'text',
    apiEndpoint: 'genotox-final-outcome/',
    qualifiers: ['is'],
    icon: 'mdi-dna',
    filterDescription: 'description for Genotoxicity Final Outcome',
    tooltipDescription: 'Genotoxicity Final Outcome tooltip description'
  },
  finalToxicologyRemarks: {
    displayName: 'Final Toxicology Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'description for Final Toxicology Remarks',
    tooltipDescription: 'Final Toxicology Remarks tooltip description'
  },
  proteinDigestibility: {
    displayName: 'Protein Digestibility',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-food-drumstick-outline',
    filterDescription: 'description for Protein Digestibility',
    tooltipDescription: 'Protein Digestibility tooltip description'
  },
  hasNutriDisadvantage: {
    displayName: 'Nutritional Disadvantage',
    displayGroupName: 'Novel Food',
    type: 'boolean',
    qualifiers: ['is true', 'is false'],
    icon: 'mdi-scale-balance',
    filterDescription: 'description for Nutritional Disadvantage',
    tooltipDescription: 'Nutritional Disadvantage tooltip description'
  },
  nutriDisadvantageExplanation: {
    displayName: 'Nutritional Disadvantage Explanation',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-text-box-outline',
    filterDescription: 'description for Nutritional Disadvantage Explanation',
    tooltipDescription: 'Nutritional Disadvantage Explanation tooltip description'
  },
  sufficientData: {
    displayName: 'Sufficient Data',
    flattenedDisplayName: 'Stability - Sufficient Data',
    displayGroupName: 'Novel Food',
    type: 'boolean',
    qualifiers: ['is true', 'is false'],
    icon: 'mdi-database-check',
    filterDescription: 'description for Sufficient Data',
    tooltipDescription: 'Sufficient Data tooltip description'
  },
  foodMatrices: {
    displayName: 'Food Matrices',
    displayGroupName: 'Stability',
    flattenedDisplayName: 'Stability - Food Matrices',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-grid',
    filterDescription: 'description for Food Matrices',
    tooltipDescription: 'Food Matrices tooltip description'
  },
  instabilityConcerns: {
    displayName: 'Instability Concerns',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-outline',
    filterDescription: 'description for Instability Concerns',
    tooltipDescription: 'Instability Concerns tooltip description'
  },
  shelflifeValue: {
    displayName: 'Shelf Life Value',
    displayGroupName: 'Novel Food',
    type: 'number',
    qualifiers: ['is', 'greater than', 'less than'],
    icon: 'mdi-clock-outline',
    filterDescription: 'description for Shelf Life Value',
    tooltipDescription: 'Shelf Life Value tooltip description'
  },
  shelflifeUnit: {
    displayName: 'Shelf Life Unit',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-timer-sand',
    filterDescription: 'description for Shelf Life Unit',
    tooltipDescription: 'Shelf Life Unit tooltip description'
  },
  endocrineDisruptProp: {
    displayName: 'Endocrine Disruptive Properties',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-outline',
    filterDescription: 'description for Endocrine Disruptive Properties',
    tooltipDescription: 'Endocrine Disruptive Properties tooltip description'
  },
  outcome: {
    displayName: 'Outcome',
    flattenedDisplayName: 'Novel Food Outcome',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Outcome',
    tooltipDescription: 'Outcome tooltip description'
  },
  outcomeRemarks: {
    displayName: 'Outcome Remarks',
    flattenedDisplayName: 'Novel Food Outcome Remarks',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-comment-text-outline',
    filterDescription: 'description for Outcome Remarks',
    tooltipDescription: 'Outcome Remarks tooltip description'
  },
  vocabId: {
    displayName: 'Vocabulary Name',
    flattenedDisplayName: 'Novel Food Vocabulary Name',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Vocabulary Name',
    tooltipDescription: 'Vocabulary Name tooltip description'
  },

  'allergenicities.title': {
    displayName: '',
    flattenedDisplayName: 'Allergenicity',
    displayGroupName: 'Allergenicity',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Allergenicity',
    tooltipDescription: 'Allergenicity tooltip description'
  },

  // opinion

  opinionDocumentType: {
    displayName: 'Opinion Document Type',
    displayGroupName: 'Opinion',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Document Type',
    tooltipDescription: 'Opinion Document Type tooltip description'
  },
  opinionTitle: {
    displayName: 'Opinion Title',
    displayGroupName: 'Opinion',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Title',
    tooltipDescription: 'Opinion Title tooltip description'
  },
  opinionDoi: {
    displayName: 'Opinion DOI',
    displayGroupName: 'Opinion',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion DOI',
    tooltipDescription: 'Opinion DOI tooltip description'
  },
  opinionUrl: {
    displayName: 'Opinion URL',
    displayGroupName: 'Opinion',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion URL',
    tooltipDescription: 'Opinion URL tooltip description'
  },
  opinionPublicationDate: {
    displayName: 'Opinion Publication Date',
    displayGroupName: 'Opinion',
    type: 'date',
    qualifiers: ['is before', 'is after', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Publication Date',
    tooltipDescription: 'Opinion Publication Date tooltip description'
  },
  opinionAdoptionDate: {
    displayName: 'Opinion Adoption Date',
    displayGroupName: 'Opinion',
    type: 'date',
    qualifiers: ['is before', 'is after', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Opinion Adoption Date',
    tooltipDescription: 'Opinion Adoption Date tooltip description'
  },

  'panels.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Panel',
    displayGroupName: 'Administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for Panel's Name",
    tooltipDescription: "Panel's Name tooltip description"
  },

  'sciOfficers.firstName': {
    displayName: 'First Name',
    flattenedDisplayName: "Scientific Officer's First Name",
    displayGroupName: 'Administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for Scientific Officer's First Name",
    tooltipDescription: "Scientific Officer's First Name tooltip description"
  },
  'sciOfficers.middleName': {
    displayName: 'Middle Name',
    flattenedDisplayName: "Scientific officer's Middle Name",
    displayGroupName: 'Administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for scientific officer's Middle Name",
    tooltipDescription: "Scientific officer's Middle Name tooltip description"
  },
  'sciOfficers.lastName': {
    displayName: 'Last Name',
    flattenedDisplayName: "Scientific officer's Last Name",
    displayGroupName: 'Administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for scientific officer's Last Name",
    tooltipDescription: "Scientific officer's Last Name tooltip description"
  },

  // question

  'questions.number': {
    displayName: 'Number',
    flattenedDisplayName: 'Question Number',
    displayGroupName: 'Question',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Number',
    tooltipDescription: 'Number tooltip description'
  },

  'questions.applicants.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Applicant',
    displayGroupName: 'Applicant',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for applicant title',
    tooltipDescription: 'Applicant title tooltip description'
  },

  'questions.mandates.mandateTypeTitle': {
    displayName: 'Type',
    flattenedDisplayName: 'Mandate Type',
    displayGroupName: 'Mandate',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type',
    tooltipDescription: 'Mandate Type tooltip description'
  },
  'questions.mandates.mandateTypeDefinition': {
    displayName: 'Type Definition',
    flattenedDisplayName: 'Mandate Type Definition',
    displayGroupName: 'Mandate',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Type Definition',
    tooltipDescription: 'Mandate Type Definition tooltip description'
  },
  'questions.mandates.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Mandate Regulation',
    displayGroupName: 'Mandate',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Mandate Regulation',
    tooltipDescription: 'Mandate Regulation tooltip description'
  },

  'foodCategories.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Food Category Name',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Food Category Name',
    tooltipDescription: 'Food Category Name tooltip description'
  },
  'foodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Food Category Definition',
    tooltipDescription: 'Food Category Definition tooltip description'
  },

  'novelFoodCategories.title': {
    displayName: 'Name',
    flattenedDisplayName: 'Novel Food Category',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Novel Food Category',
    tooltipDescription: 'Novel Food Category tooltip description'
  },
  'novelFoodCategories.definition': {
    displayName: 'Definition',
    flattenedDisplayName: 'Novel Food Category Definition',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-alert-circle-outline',
    filterDescription: 'description for Novel Food Category Definition',
    tooltipDescription: 'Novel Food Category Definition tooltip description'
  },
  'novelFoodCategories.regulation': {
    displayName: 'Regulation',
    flattenedDisplayName: 'Novel Food Category Regulation',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: 'description for Novel Food Category regulation',
    tooltipDescription: 'Novel Food Category regulation tooltip description'
  },

  // adme

  'admes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'ADME Test Type',
    displayGroupName: 'ADME',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description'
  },
  'admes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'ADME Guideline',
    displayGroupName: 'ADME',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description'
  },
  'admes.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'ADME Guideline Qualifier',
    displayGroupName: 'ADME',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline Qualifier',
    tooltipDescription: 'Guideline Qualifier tooltip description'
  },
  'admes.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'ADME Study Source',
    displayGroupName: 'ADME',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Study Source',
    tooltipDescription: 'Study Source tooltip description'
  },

  'admes.investigationTypes.title': {
    displayName: 'Name',
    flattenedDisplayName: 'ADME Investigation Type',
    displayGroupName: 'ADME',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-flask',
    filterDescription: 'description for Investigation Type Name',
    tooltipDescription: 'Investigation Type Name tooltip description'
  },

  // genotox

  'genotoxes.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Genotox Test Type',
    displayGroupName: 'Genotox',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-dna',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description'
  },
  'genotoxes.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Genotox Guideline',
    displayGroupName: 'Genotox',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description'
  },
  'genotoxes.guidelineQualifier': {
    displayName: 'Guideline Qualifier',
    flattenedDisplayName: 'Genotox Guideline Qualifier',
    displayGroupName: 'Genotox',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline Qualifier',
    tooltipDescription: 'Guideline Qualifier tooltip description'
  },
  'genotoxes.studySource': {
    displayName: 'Study Source',
    flattenedDisplayName: 'Genotox Study Source',
    displayGroupName: 'Genotox',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-outline',
    filterDescription: 'description for Study Source',
    tooltipDescription: 'Study Source tooltip description'
  },
  'genotoxes.outcome': {
    displayName: 'Outcome',
    flattenedDisplayName: 'Genotox Outcome',
    displayGroupName: 'Genotox',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Genotox Outcome',
    tooltipDescription: 'Genotox Outcome tooltip description'
  },

  // endpoint studies

  'endpointstudies.testType': {
    displayName: 'Test Type',
    flattenedDisplayName: 'Endpoint Study Test Type',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-flask-outline',
    filterDescription: 'description for Test Type',
    tooltipDescription: 'Test Type tooltip description'
  },
  'endpointstudies.guideline': {
    displayName: 'Guideline',
    flattenedDisplayName: 'Endpoint Study Guideline',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-book-open-outline',
    filterDescription: 'description for Guideline',
    tooltipDescription: 'Guideline tooltip description'
  },
  'endpointstudies.species': {
    displayName: 'Species',
    flattenedDisplayName: 'Endpoint Study Species',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-paw',
    filterDescription: 'description for Species',
    tooltipDescription: 'Species tooltip description'
  },
  'endpointstudies.sex': {
    displayName: 'Sex',
    flattenedDisplayName: 'Endpoint Study Sex',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-gender-male-female',
    filterDescription: 'description for Sex',
    tooltipDescription: 'Sex tooltip description'
  },
  'endpointstudies.studyDuration': {
    displayName: 'Study Duration',
    flattenedDisplayName: 'Endpoint Study Duration',
    displayGroupName: 'Endpoint Study',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-clock-outline',
    filterDescription: 'description for Study Duration',
    tooltipDescription: 'Study Duration tooltip description'
  },

  'endpointstudies.endpoints.referencePoint': {
    displayName: 'Reference Point',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-target',
    filterDescription: 'description for Reference Point',
    tooltipDescription: 'Reference Point tooltip description'
  },
  'endpointstudies.endpoints.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Endpoint Qualifier',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description'
  },
  'endpointstudies.endpoints.subpopulation': {
    displayName: 'Subpopulation',
    flattenedDisplayName: 'Endpoint Subpopulation',
    displayGroupName: 'Endpoint',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-account-group',
    filterDescription: 'description for Subpopulation',
    tooltipDescription: 'Subpopulation tooltip description'
  },
  'endpointstudies.endpoints.lovalue': {
    displayName: 'Value',
    flattenedDisplayName: 'Endpoint Value',
    displayGroupName: 'Endpoint',
    type: 'number',
    qualifiers: ['is', 'greater than', 'less than'],
    icon: 'mdi-arrow-down',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description'
  },

  'endpointstudies.endpoints.finalOutcomes.outcome': {
    displayName: '',
    flattenedDisplayName: 'Final Outcome',
    displayGroupName: 'Final Outcome',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-check-circle-outline',
    filterDescription: 'description for Outcome',
    tooltipDescription: 'Outcome tooltip description'
  },
  'endpointstudies.endpoints.finalOutcomes.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Final Outcome Qualifier',
    displayGroupName: 'Final Outcome',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description'
  },
  'endpointstudies.endpoints.finalOutcomes.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Final Outcome Value',
    displayGroupName: 'Final Outcome',
    type: 'number',
    qualifiers: ['is', 'greater than', 'less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description'
  },

  'endpointstudies.endpoints.finalOutcomes.populations.subgroup': {
    displayName: 'Subgroup',
    flattenedDisplayName: 'Final Outcome Population Subgroup',
    displayGroupName: 'Population',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-account-multiple-outline',
    filterDescription: 'description for Subgroup',
    tooltipDescription: 'Subgroup tooltip description'
  },
  'endpointstudies.endpoints.finalOutcomes.populations.qualifier': {
    displayName: 'Qualifier',
    flattenedDisplayName: 'Final Outcome Population Qualifier',
    displayGroupName: 'Population',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-scale',
    filterDescription: 'description for Qualifier',
    tooltipDescription: 'Qualifier tooltip description'
  },
  'endpointstudies.endpoints.finalOutcomes.populations.value': {
    displayName: 'Value',
    flattenedDisplayName: 'Final Outcome Population Value',
    displayGroupName: 'Population',
    type: 'number',
    qualifiers: ['is', 'greater than', 'less than'],
    icon: 'mdi-numeric',
    filterDescription: 'description for Value',
    tooltipDescription: 'Value tooltip description'
  }
}
