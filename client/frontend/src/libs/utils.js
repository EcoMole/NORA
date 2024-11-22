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
    const djangoLookupField = fields[key].djangoLookupField
    acc.push({ qualifier, include, value, djangoLookupField })
    return acc
  }, [])
}

export { getInitials, getUserType, buildVariables }
