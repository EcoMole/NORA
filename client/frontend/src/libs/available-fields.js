//! rename to availableFields
export const availableFields = {
  // novel food
  novelFoods: {
    displayName: 'Novel Food',
    fields: {
      nfCode: {
        displayName: 'NF code',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-rice',
        filterDescription: 'description for NF code',
        tooltipDescription: 'NF code tooltip description'
      },
      title: {
        displayName: 'Novel food title',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-rice',
        filterDescription: 'description for novel food title',
        tooltipDescription: 'Novel food title tooltip description'
      },

      toxStudyRequired: {
        displayName: 'Toxicology Study Required',
        displayGroupName: 'Novel Food',
        type: 'boolean',
        qualifiers: ['is true', 'is false'],
        icon: 'mdi-flask-outline',
        filterDescription: 'description for Toxicology Study Required',
        tooltipDescription: 'Toxicology Study Required tooltip description'
      },
      genotoxFinalOutcome: {
        displayName: 'Genotoxicity Final Outcome',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
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
        displayGroupName: 'Novel Food',
        type: 'boolean',
        qualifiers: ['is true', 'is false'],
        icon: 'mdi-database-check',
        filterDescription: 'description for Sufficient Data',
        tooltipDescription: 'Sufficient Data tooltip description'
      },
      foodMatrices: {
        displayName: 'Food Matrices',
        displayGroupName: 'Novel Food',
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
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-check-circle-outline',
        filterDescription: 'description for Outcome',
        tooltipDescription: 'Outcome tooltip description'
      },
      outcomeRemarks: {
        displayName: 'Outcome Remarks',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-comment-text-outline',
        filterDescription: 'description for Outcome Remarks',
        tooltipDescription: 'Outcome Remarks tooltip description'
      },
      vocabId: {
        displayName: 'Vocabulary ID',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-book-open-outline',
        filterDescription: 'description for Vocabulary ID',
        tooltipDescription: 'Vocabulary ID tooltip description'
      },
      allergenicities: {
        displayName: 'Allergenicity',
        fields: {
          title: {
            displayName: 'Allergenicity',
            displayGroupName: 'Allergenicity',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-alert-circle-outline',
            filterDescription: 'description for Allergenicity',
            tooltipDescription: 'Allergenicity tooltip description'
          }
        }
      },

      // opinion
      opinionDocumentType: {
        displayName: 'Opinion document type',
        displayGroupName: 'Novel Food',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-file-document-outline',
        filterDescription: 'description for opinion document type',
        tooltipDescription: 'Opinion document type tooltip description'
      },
      opinionTitle: {
        displayName: 'Opinion title',
        displayGroupName: 'Opinion',
        type: 'text',
        qualifiers: ['contains', 'is'],
        icon: 'mdi-file-document-outline',
        filterDescription: 'description for Opinion title',
        tooltipDescription: 'Opinion title tooltip description'
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
        displayName: 'Opinion publication date',
        displayGroupName: 'Opinion',
        type: 'date',
        qualifiers: ['is before', 'is after', 'is'],
        icon: 'mdi-file-document-outline',
        filterDescription: 'description for Opinion publication date',
        tooltipDescription: 'Opinion publication date tooltip description'
      },
      opinionAdoptionDate: {
        displayName: 'Opinion adoption date',
        displayGroupName: 'Opinion',
        type: 'date',
        qualifiers: ['is before', 'is after', 'is'],
        icon: 'mdi-file-document-outline',
        filterDescription: 'description for Opinion adoption date',
        tooltipDescription: 'Opinion adoption date tooltip description'
      },
      panels: {
        displayName: 'Panel',
        fields: {
          title: {
            displayName: "Panel's title",
            displayGroupName: 'Administrative',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-file-document-outline',
            filterDescription: "description for panel's title",
            tooltipDescription: 'Panel title tooltip description'
          }
        }
      },
      sciOfficers: {
        displayName: 'Scientific Officer',
        fields: {
          firstName: {
            displayName: "Scientific officer's first name",
            displayGroupName: 'Administrative',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-file-document-outline',
            filterDescription: "description for scientific officer's first name",
            tooltipDescription: "Scientific officer's first name tooltip description"
          },
          middleName: {
            displayName: "Scientific officer's middle name",
            displayGroupName: 'Administrative',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-file-document-outline',
            filterDescription: "description for scientific officer's middle name",
            tooltipDescription: "Scientific officer's middle name tooltip description"
          },
          lastName: {
            displayName: "Scientific officer's last name",
            displayGroupName: 'Administrative',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-file-document-outline',
            filterDescription: "description for scientific officer's last name",
            tooltipDescription: "Scientific officer's last name tooltip description"
          }
        }
      },

      // question

      questions: {
        displayName: 'Question',
        fields: {
          number: {
            displayName: 'Question number',
            displayGroupName: 'Question',
            type: 'text',
            qualifiers: ['contains', 'is'],
            icon: 'mdi-file-document-outline',
            filterDescription: 'description for question number',
            tooltipDescription: 'Question number tooltip description'
          },
          applicants: {
            displayName: 'Applicant',
            fields: {
              title: {
                displayName: 'Applicant title',
                displayGroupName: 'Applicant',
                type: 'text',
                qualifiers: ['contains', 'is'],
                icon: 'mdi-file-document-outline',
                filterDescription: 'description for applicant title',
                tooltipDescription: 'Applicant title tooltip description'
              }
            }
          },
          // mandate
          mandates: {
            displayName: 'Mandate',
            fields: {
              mandateTypeTitle: {
                displayName: 'Mandate type title',
                displayGroupName: 'Mandate',
                type: 'text',
                qualifiers: ['contains', 'is'],
                icon: 'mdi-file-document-outline',
                filterDescription: 'description for mandate type title',
                tooltipDescription: 'Mandate type title tooltip description'
              },
              mandateTypeDefinition: {
                displayName: 'Mandate type definition',
                displayGroupName: 'Mandate',
                type: 'text',
                qualifiers: ['contains', 'is'],
                icon: 'mdi-file-document-outline',
                filterDescription: 'description for mandate type definition',
                tooltipDescription: 'Mandate type definition tooltip description'
              },
              regulation: {
                displayName: 'Mandate regulation',
                displayGroupName: 'Mandate',
                type: 'text',
                qualifiers: ['contains', 'is'],
                icon: 'mdi-file-document-outline',
                filterDescription: 'description for mandate regulation',
                tooltipDescription: 'Mandate regulation tooltip description'
              }
            }
          }
        }
      }
    }
  }
}
