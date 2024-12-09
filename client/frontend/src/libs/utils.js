function getInitials(firstName, lastName) {
  let firtsLetter = firstName ? firstName.charAt(0).toUpperCase() : ''
  let secondLetter = lastName ? lastName.charAt(0).toUpperCase() : ''
  return firtsLetter + secondLetter
}

function getUserType(user) {
  return user.isSuperuser ? 'superuser' : user.isStaff ? 'staff' : null
}

import { coupledFilterFields, simpleFilterFields } from './definitions'

const allFields = { ...coupledFilterFields, ...simpleFilterFields }

function buildVariables(addedFilters) {
  return addedFilters.reduce(
    (acc, { djangoLookupFilter, include, djangoApp, djangoModel, coupledFilters }) => {
      acc.push({
        djangoLookupFilter,
        include,
        djangoApp,
        djangoModel,
        coupledFilters: coupledFilters.map(({ key, qualifier, value }) => {
          const djangoLookupField = allFields[key].djangoLookupField
            ? allFields[key].djangoLookupField
            : null
          const fieldType = allFields[key].fieldType ? allFields[key].fieldType : null
          const valueFields = allFields[key].valueFields ? allFields[key].valueFields : null

          return { qualifier, value, djangoLookupField, fieldType, valueFields }
        })
      })

      return acc
    },
    []
  )
}

export { getInitials, getUserType, buildVariables }
