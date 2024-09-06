export const newAvailableAttrs = {
  novelFoods_nfCode: {
    displayName: 'NF code',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-rice',
    filterDescription: 'description for NF code',
    tooltipDescription: 'NF code tooltip description'
  },
  novelFoods_title: {
    displayName: 'Novel food title',
    displayGroupName: 'Novel Food',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-rice',
    filterDescription: 'description for novel food title',
    tooltipDescription: 'Novel food title tooltip description'
  },

  panels_title: {
    displayName: "Panel's title",
    displayGroupName: 'Administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    icon: 'mdi-file-document-outline',
    filterDescription: "description for panel's title",
    tooltipDescription: 'Panel title tooltip description'
  }
}

export const availableAttrs = [
  // novel food
  {
    text: 'NF code',
    model: 'novelFoods',
    field: 'nfCode',
    icon: 'mdi-rice',
    description: 'description'
  },
  {
    text: 'novel food title',
    model: 'novelFoods',
    field: 'title',
    icon: 'mdi-rice',
    description: 'description'
  },
  {
    text: 'opinion document type',
    model: 'novelFoods',
    field: 'opinionDocumentType',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'Toxicology Study Required',
    model: 'novelFoods',
    field: 'toxStudyRequired',
    icon: 'mdi-flask-outline',
    description: 'description'
  },
  {
    text: 'Genotoxicity Final Outcome',
    model: 'novelFoods',
    field: 'genotoxFinalOutcome',
    icon: 'mdi-dna',
    description: 'description'
  },
  {
    text: 'Final Toxicology Remarks',
    model: 'novelFoods',
    field: 'finalToxicologyRemarks',
    icon: 'mdi-comment-text-outline',
    description: 'description'
  },
  {
    text: 'Protein Digestibility',
    model: 'novelFoods',
    field: 'proteinDigestibility',
    icon: 'mdi-food-drumstick-outline',
    description: 'description'
  },
  {
    text: 'Antinutritional Factors',
    model: 'novelFoods',
    field: 'antinutritionalFactors',
    icon: 'mdi-alert-circle-outline',
    description: 'description'
  },
  {
    text: 'Nutritional Disadvantage',
    model: 'novelFoods',
    field: 'hasNutriDisadvantage',
    icon: 'mdi-scale-balance',
    description: 'description'
  },
  {
    text: 'Nutritional Disadvantage Explanation',
    model: 'novelFoods',
    field: 'nutriDisadvantageExplanation',
    icon: 'mdi-text-box-outline',
    description: 'description'
  },
  {
    text: 'Sufficient Data',
    model: 'novelFoods',
    field: 'sufficientData',
    icon: 'mdi-database-check',
    description: 'description'
  },
  {
    text: 'Food Matrices',
    model: 'novelFoods',
    field: 'foodMatrices',
    icon: 'mdi-grid',
    description: 'description'
  },
  {
    text: 'Instability Concerns',
    model: 'novelFoods',
    field: 'instabilityConcerns',
    icon: 'mdi-alert-outline',
    description: 'description'
  },
  {
    text: 'Shelf Life Value',
    model: 'novelFoods',
    field: 'shelflifeValue',
    icon: 'mdi-clock-outline',
    description: 'description'
  },
  {
    text: 'Shelf Life Unit',
    model: 'novelFoods',
    field: 'shelflifeUnit',
    icon: 'mdi-timer-sand',
    description: 'description'
  },
  {
    text: 'Endocrine Disruptive Properties',
    model: 'novelFoods',
    field: 'endocrineDisruptProp',
    icon: 'mdi-alert-outline',
    description: 'description'
  },
  {
    text: 'Outcome',
    model: 'novelFoods',
    field: 'outcome',
    icon: 'mdi-check-circle-outline',
    description: 'description'
  },
  {
    text: 'Outcome Remarks',
    model: 'novelFoods',
    field: 'outcomeRemarks',
    icon: 'mdi-comment-text-outline',
    description: 'description'
  },
  {
    text: 'Vocabulary ID',
    model: 'novelFoods',
    field: 'vocabId',
    icon: 'mdi-book-open-outline',
    description: 'description'
  },
  {
    text: 'Allergenicity',
    model: 'allergenicities',
    field: 'title',
    icon: 'mdi-alert-circle-outline',
    description: 'description'
  },

  // opinion
  {
    text: 'opinion document type',
    model: 'novelFoods',
    field: 'opinionDocumentType',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'opinion title',
    model: 'novelFoods',
    field: 'opinionTitle',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'opinion doi',
    model: 'novelFoods',
    field: 'opinionDoi',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'opinion url',
    model: 'novelFoods',
    field: 'opinionUrl',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'opinion publication date',
    model: 'novelFoods',
    field: 'opinionPublicationDate',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'opinion adoption date',
    model: 'novelFoods',
    field: 'opinionAdoptionDate',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: "opinion's panel title",
    model: 'panels',
    field: 'title',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: "opinion's scientific officer first name",
    model: 'sciOfficers',
    field: 'firstName',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: "opinion's scientific officer middle name",
    model: 'sciOfficers',
    field: 'middleName',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: "opinion's scientific officer last name",
    model: 'sciOfficers',
    field: 'lastName',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },

  // question
  {
    text: 'question number',
    model: 'questions',
    field: 'number',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'applicant title',
    model: 'applicants',
    field: 'title',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },

  // mandate
  {
    text: 'mandate type title',
    model: 'mandates',
    field: 'mandateTypeTitle',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'mandate type definition',
    model: 'mandates',
    field: 'mandateTypeDefinition',
    icon: 'mdi-file-document-outline',
    description: 'description'
  },
  {
    text: 'mandate regulation',
    model: 'mandates',
    field: 'regulation',
    icon: 'mdi-file-document-outline',
    description: 'description'
  }
]
