import gql from 'graphql-tag'

function getFields(selectedAttrs, model) {
  const modelPrefix = model + '_'
  return Object.keys(selectedAttrs).reduce((acc, key) => {
    if (key.startsWith(modelPrefix)) {
      const field = key.replace(modelPrefix, '')
      acc.push(field)
    }
    return acc
  }, [])
}

export function buildQraphQLQuery(selectedAttrs) {
  let novelFoodQueryPart = ''
  let questioinsQueryPart = ''

  let novelFoodFields = getFields(selectedAttrs, 'novelFoods')
  if (novelFoodFields.length > 0) {
    novelFoodQueryPart += `
    ${novelFoodFields.includes('nfCode') ? 'nfCode' : ''}
    ${novelFoodFields.includes('title') ? 'title' : ''}
    ${novelFoodFields.includes('opinionDocumentType') ? 'opinionDocumentType' : ''}
    ${novelFoodFields.includes('opinionTitle') ? 'opinionTitle' : ''}
    ${novelFoodFields.includes('opinionDoi') ? 'opinionDoi' : ''}
    ${novelFoodFields.includes('opinionUrl') ? 'opinionUrl' : ''}
    ${novelFoodFields.includes('opinionPublicationDate') ? 'opinionPublicationDate' : ''}
    ${novelFoodFields.includes('opinionAdoptionDate') ? 'opinionAdoptionDate' : ''}
    ${novelFoodFields.includes('toxStudyRequired') ? 'toxStudyRequired' : ''}
    ${novelFoodFields.includes('genotoxFinalOutcome') ? 'genotoxFinalOutcome' : ''}
    ${novelFoodFields.includes('finalToxicologyRemarks') ? 'finalToxicologyRemarks' : ''}
    ${novelFoodFields.includes('proteinDigestibility') ? 'proteinDigestibility' : ''}
    ${novelFoodFields.includes('antinutritionalFactors') ? 'antinutritionalFactors' : ''}
    ${novelFoodFields.includes('hasNutriDisadvantage') ? 'hasNutriDisadvantage' : ''}
    ${novelFoodFields.includes('nutriDisadvantageExplanation') ? 'nutriDisadvantageExplanation' : ''}
    ${novelFoodFields.includes('sufficientData') ? 'sufficientData' : ''}
    ${novelFoodFields.includes('foodMatrices') ? 'foodMatrices' : ''}
    ${novelFoodFields.includes('instabilityConcerns') ? 'instabilityConcerns' : ''}
    ${novelFoodFields.includes('shelflifeValue') ? 'shelflifeValue' : ''}
    ${novelFoodFields.includes('shelflifeUnit') ? 'shelflifeUnit' : ''}
    ${novelFoodFields.includes('endocrineDisruptProp') ? 'endocrineDisruptProp' : ''}
    ${novelFoodFields.includes('outcome') ? 'outcome' : ''}
    ${novelFoodFields.includes('outcomeRemarks') ? 'outcomeRemarks' : ''}
    ${novelFoodFields.includes('vocabId') ? 'vocabId' : ''}
    `
  }

  let panelsFields = getFields(selectedAttrs, 'panels')
  if (panelsFields.length > 0 && panelsFields.includes('title')) {
    novelFoodQueryPart += `
    panels {
      title
    }
    `
  }

  let sciOfficersFields = getFields(selectedAttrs, 'sciOfficers')
  if (sciOfficersFields.length > 0) {
    novelFoodQueryPart += `
    sciOfficers {
      ${sciOfficersFields.includes('firstName') ? 'firstName' : ''}
      ${sciOfficersFields.includes('middleName') ? 'middleName' : ''}
      ${sciOfficersFields.includes('lastName') ? 'lastName' : ''}
    }
    `
  }

  let allergenicityFields = getFields(selectedAttrs, 'allergenicities')
  if (allergenicityFields.length > 0) {
    novelFoodQueryPart += `
    allergenicities {
      ${allergenicityFields.includes('title') ? 'title' : ''}
    }
    `
  }

  let questionsFields = getFields(selectedAttrs, 'questions')
  if (questionsFields.includes('number')) {
    questioinsQueryPart += `
      number
      `
  }

  let applicantsFields = getFields(selectedAttrs, 'applicants')
  if (applicantsFields.includes('title')) {
    questioinsQueryPart += `
      applicants {
        title
      }
      `
  }

  let mandateFields = getFields(selectedAttrs, 'mandates')
  if (mandateFields.length > 0) {
    questioinsQueryPart += `
      mandates {
        ${mandateFields.includes('mandateTypeTitle') ? 'mandateTypeTitle' : ''}
        ${mandateFields.includes('mandateTypeDefinition') ? 'mandateTypeDefinition' : ''}
        ${mandateFields.includes('regulation') ? 'regulation' : ''}
      }
    `
  }

  if (questioinsQueryPart) {
    novelFoodQueryPart += `
    questions {
      ${questioinsQueryPart}
    }
    `
  }
  const finalQuery = gql`
  query GetNovelFoods($novelFoodTitle: String) {
      novelFoods(titleIcontains: $novelFoodTitle) {
          edges {
      node {
        ${novelFoodQueryPart}
        }
        }
        }
        }`

  return finalQuery
}
