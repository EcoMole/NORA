import gql from 'graphql-tag'
import { query as gqlQuery } from 'gql-query-builder'
import { fields } from './definitions'

function toDesiredVariablesStructure(variables) {
  return Object.entries(variables).reduce((acc, [key, value]) => {
    acc[key] = { value: value, required: false }
    return acc
  }, {})
}

export function buildGraphQLQuery(variables, fields) {
  const { query } = gqlQuery({
    operation: 'novelFoods',
    fields: [
      {
        edges: [
          {
            node: fields
          }
        ]
      }
    ],
    variables: toDesiredVariablesStructure(variables)
  })
  return gql`
    ${query}
  `
}

function toNestedStructure(flattenedFields) {
  /*

builds nested format:
{
field1: {
 		field2: {}
  },
field3: {},
field4: {
    field5: {
        field6: {},
        field7: {}
      }
    },
field8: {}
}

from the flattenedFields format:
{
"field1.field2" : {},
"field3" : {},
"field4.field5.field6" : {},
"field4.field5.field7" : {},
"field8" : {}
}
*/
  const result = {}

  for (const fieldPath in flattenedFields) {
    const pathArray = fieldPath.split('.')
    let currentObject = result

    pathArray.forEach((part) => {
      if (!currentObject[part]) {
        currentObject[part] = {}
      }
      currentObject = currentObject[part]
    })
  }
  return result
}

function toGqlQueryDesiredStructure(fields) {
  /*

Builds the gql-query-builder desired format:
newArray = [
  {field1: ["field2"]},
  "field3",
  {field4:
    {field5: ["field6", "field7"]}},
  "field8"
]

from the nested format
{
field1: {
 		field2: {}
  },
field3: {},
field4: {
    field5: {
        field6: {},
        field7: {}
      }
    },
field8: {},
}
*/
  return Object.entries(fields).reduce(
    (acc, [fieldName, fieldData]) => {
      if (fieldData && typeof fieldData === 'object' && Object.keys(fieldData).length > 0) {
        acc.push({
          [fieldName]: toGqlQueryDesiredStructure(fieldData)
        })
      } else {
        acc.push(fieldName)
      }
      return acc
      // we need to fetch IDs for the exporting feature
    },
    ['id']
  )
}

export function buildQueryFromSelectedFields(variables, selectedFields = fields) {
  const formattedFields = toGqlQueryDesiredStructure(toNestedStructure(selectedFields))
  // we need the novelFoodId for the exporting feature
  formattedFields.push('novelFoodId')
  return buildGraphQLQuery(variables, formattedFields)
}
