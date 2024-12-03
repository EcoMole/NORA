function getInitials(firstName, lastName) {
  let firtsLetter = firstName ? firstName.charAt(0).toUpperCase() : ''
  let secondLetter = lastName ? lastName.charAt(0).toUpperCase() : ''
  return firtsLetter + secondLetter
}

function getUserType(user) {
  return user.isSuperuser ? 'superuser' : user.isStaff ? 'staff' : null
}

import { fields, novelFoodAndOpinionFields } from './definitions'

const allFields = { ...fields, ...novelFoodAndOpinionFields }

function buildVariables(addedFilters) {
  return addedFilters.reduce(
    (acc, { djangoLookupFilter, include, djangoApp, djangoModel, coupledFilters }) => {
      const djangoLookupField = allFields[coupledFilters[0].key].djangoLookupField
        ? allFields[coupledFilters[0].key].djangoLookupField
        : null
      const fieldType = allFields[coupledFilters[0].key].fieldType
        ? allFields[coupledFilters[0].key].fieldType
        : null
      const valueFields = allFields[coupledFilters[0].key].valueFields
        ? allFields[coupledFilters[0].key].valueFields
        : null
      acc.push({
        djangoLookupFilter,
        include,
        djangoApp,
        djangoModel,
        coupledFilters: coupledFilters.map(({ qualifier, value }) => {
          return { qualifier, value, djangoLookupField, fieldType, valueFields }
        })
      })

      return acc
    },
    []
  )
}

export { getInitials, getUserType, buildVariables }
