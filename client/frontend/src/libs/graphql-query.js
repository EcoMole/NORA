import gql from 'graphql-tag'
import { query as gqlQuery } from 'gql-query-builder'
import { availableFields } from './available-fields'

export function buildGraphQLQuery(fields) {
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
    ]
  })
  return gql`
    ${query}
  `
}

function buildNestedFieldsStructure(flattenedFields) {
  /*

builds the availbleFields format

field1: {
  fields: {
 		field2: {
 		}
  },
field3: {},
field4: {
  fields: {
    field5: {
      fields: {
        field6: {},
        field7: {}
      }
    }
  }
},
field8: {}


from flattenedFields format

flattenedFields = {
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
    // reference to the `result` object
    // any changes made to currentObject will directly affect the `result` object
    let currentObject = result

    pathArray.forEach((part, i) => {
      // If it's the last part, add the record without "fields" object
      if (i === pathArray.length - 1) {
        if (!currentObject[part]) {
          currentObject[part] = {}
        }
      } else {
        // If the part doesn't exist yet, create a "fields" object
        if (!currentObject[part]) {
          currentObject[part] = { fields: {} }
        }

        // Move deeper into the structure
        currentObject = currentObject[part].fields
      }
    })
  }
  return result
}

function parseFields(fields) {
  /*
Builds the desired format:
newArray = [
  {field1: ["field2"]},
  "field3",
  {field4:
    {field5: ["field6", "field7"]}},
  "field8"
]

from the availbleFields format

field1: {
  fields: {
 		field2: {
 		}
  },
field3: {},
field4: {
  fields: {
    field5: {
      fields: {
        field6: {},
        field7: {}
      }
    }
  }
},
field8: {}
 */
  return Object.entries(fields).reduce((acc, [fieldName, fieldData]) => {
    if (fieldData.fields) {
      acc.push({
        [fieldName]: parseFields(fieldData.fields)
      })
    } else {
      acc.push(fieldName)
    }
    console.log('acc', acc)
    return acc
  }, [])
}

export function buildQueryFromAllAvailableFields() {
  return buildGraphQLQuery(parseFields(availableFields.novelFoods.fields))
}

export function buildQueryFromSelectedFields(selectedFields) {
  return buildGraphQLQuery(parseFields(buildNestedFieldsStructure(selectedFields)))
}
