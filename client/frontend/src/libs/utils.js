function getInitials(firstName, lastName) {
  let firtsLetter = firstName ? firstName.charAt(0).toUpperCase() : ''
  let secondLetter = lastName ? lastName.charAt(0).toUpperCase() : ''
  return firtsLetter + secondLetter
}

function getUserType(user) {
  return user.isSuperuser ? 'superuser' : user.isStaff ? 'staff' : null
}


import { fields } from './definitions'

function buildVariables(addedFilters) {
  return addedFilters.reduce((acc, { key, qualifier, include, value }) => {
    const djangoLookupField = fields[key].djangoLookupField ? fields[key].djangoLookupField : null
    const fieldType = fields[key].fieldType ? fields[key].fieldType : null
    const valueFields = fields[key].valueFields ? fields[key].valueFields : null
    acc.push({ qualifier, include, value, djangoLookupField, fieldType, valueFields})
    return acc
  }, [])
}

export { getInitials, getUserType, buildVariables }
