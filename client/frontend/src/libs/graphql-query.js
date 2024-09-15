import gql from 'graphql-tag'
import { query as gqlQuery } from 'gql-query-builder'
import { fields } from './definitions'

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

builds nested format:

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


from flattenedFields format:

"field1.field2" : {},
"field3" : {},
"field4.field5.field6" : {},
"field4.field5.field7" : {},
"field8" : {}

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

Builds the gql-query-builder desired format:
newArray = [
  {field1: ["field2"]},
  "field3",
  {field4:
    {field5: ["field6", "field7"]}},
  "field8"
]

from the nested format

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
    return acc
  }, [])
}



export function buildQueryFromSelectedFields(selectedFields=fields) {
  return buildGraphQLQuery(parseFields(buildNestedFieldsStructure(selectedFields)))
}

// const mappingFile = {
//   "field1.field2": {displayName: "Field 1.2"},
//   "field3": {displayName: "Field 3"},
//   "field4.field5.field6": {displayName: "Field 4.5.6"},
//   "field4.field5.field7": {displayName: "Field 4.5.7"},
//   "field8": {disoplayName: "Field 8"}
// }

// const data = {
//   field1: {
//     field2: "value"
//   },
//   field3: "value",
//   field4: {
//     field5: {
//       field6: "value",
//       field7: "value"
//     }
//   },
//   field8: "value"
//   }
