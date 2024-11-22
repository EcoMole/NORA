import gql from 'graphql-tag'


export const attrsMandatoryForExport = {
  endpointstudies: 'endpointstudyId',
  endpoints: 'endpointId',
  novelFoodVariants: 'novelfoodvariantId'
}

export function formatGraphQLQuery(data) {
  // Create a tree structure to manage nested fields
  // each query needs to have the novelFoodId for the exporting feature
  const tree = { novelFoodId: {} }

  // Function to insert each key into the tree structure
  function insertIntoTree(parts) {
    let current = tree
    parts.forEach((part) => {
      if (!current[part]) {
        current[part] = {}
        // we need to add the mandatory id fields for exporting feature
        if (part in attrsMandatoryForExport) {
          current[part][attrsMandatoryForExport[part]] = {}
        }
      }
      current = current[part]
    })
  }

  // Build the tree from the dot notation
  Object.keys(data).forEach((key) => {
    const parts = key.split('.')
    insertIntoTree(parts)
  })

  // Function to format the tree into the GraphQL query string
  function formatTree(node, depth = 0) {
    return Object.entries(node)
      .map(([key, value]) => {
        const indent = '  '.repeat(depth)
        const children = formatTree(value, depth + 1)
        return `${indent}${key}${children ? ' {\n' + children + '\n' + indent + '}' : ''}`
      })
      .join('\n')
  }

  // Wrap the output with the `query` block
  return gql`
  query GetNovelFoods($filters: [NovelFoodFilterInput]) {
    novelFoods(filters: $filters) {
      edges {
        node {
          ${formatTree(tree, 1)}
        }
      }
    }
  }
  `
}
