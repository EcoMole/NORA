import gql from 'graphql-tag'

export function buildQraphQLQuery() {
  let novelFoodQueryPart = ''
  let questioinsQueryPart = ''

  let novelFoodFields = this.getFields('novelFoods')
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
  `
  }

  let panelsFields = this.getFields('panels')
  if (panelsFields.length > 0 && panelsFields.includes('title')) {
    novelFoodQueryPart += `
  panels {
    title
  }
  `
  }
  let sciOfficersFields = this.getFields('sciOfficers')
  if (sciOfficersFields.length > 0) {
    novelFoodQueryPart += `
  sciOfficers {
    ${sciOfficersFields.includes('firstName') ? 'firstName' : ''}
    ${sciOfficersFields.includes('middleName') ? 'middleName' : ''}
    ${sciOfficersFields.includes('lastName') ? 'lastName' : ''}
  }
  `
  }

  let questionsFields = this.getFields('questions')
  if (questionsFields.includes('number')) {
    questioinsQueryPart += `
    number
    `
  }

  let applicantsFields = this.getFields('applicants')
  if (applicantsFields.includes('title')) {
    questioinsQueryPart += `
    applicants {
      title
    }
    `
  }

  let mandateFields = this.getFields('mandates')
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

  console.log('novelFoodQueryPart', novelFoodQueryPart)
  const finalQuery = gql`
query {
    novelFoods {
        ${novelFoodQueryPart}
    }
}`

  return finalQuery
}
