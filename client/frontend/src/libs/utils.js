function getInitials(firstName, lastName) {
  let firtsLetter = firstName ? firstName.charAt(0).toUpperCase() : ''
  let secondLetter = lastName ? lastName.charAt(0).toUpperCase() : ''
  return firtsLetter + secondLetter
}

function getUserType(user) {
  return user.isSuperuser ? 'superuser' : user.isStaff ? 'staff' : null
}

// might be unnecessary
// const mappingObj = {
//   contains: 'Icontains',
//   is: 'Exact',
//   'is None': 'Isnull',
//   'must have': 'Include',
//   'must not have': 'Exclude',
//   'is before': 'Lt',
//   'is after': 'Gt'
// }
// might be unnecessary
// const mappingObj = {
//   contains: 'Icontains',
//   is: 'Exact',
//   'is None': 'Isnull',
//   'must have': 'filter',
//   'must not have': 'exclude',
//   'is before': 'Lt',
//   'is after': 'Gt'
// }

import { fields } from './definitions'

function buildVariables(addedFilters) {
  return addedFilters.reduce((acc, { key, qualifier, include, value }) => {
    if (qualifier === 'is None') {
      value = include === 'must have' ? true : false
      include = null
    }
    const djangoLookupField = fields[key].djangoLookupField
    acc.push({ qualifier, include, value, djangoLookupField })
    return acc
  }, [])
}

export { getInitials, getUserType, buildVariables }
