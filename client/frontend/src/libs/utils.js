function getInitials(firstName, lastName) {
  let firtsLetter = firstName ? firstName.charAt(0).toUpperCase() : ''
  let secondLetter = lastName ? lastName.charAt(0).toUpperCase() : ''
  return firtsLetter + secondLetter
}

function getUserType(user) {
  return user.isSuperuser ? 'superuser' : user.isStaff ? 'staff' : null
}

const mappingObj = {
  contains: 'Icontains',
  is: 'Exact',
  'is None': 'Isnull',
  'must have': 'Include',
  'must not have': 'Exclude',
  'is before': 'Lt',
  'is after': 'Gt'
}

function buildVariables(addedFilters) {
  return addedFilters.reduce((acc, { key, qualifier, include, value }) => {
    if (qualifier === 'is None') {
      value = include === 'must have' ? true : false
      include = null
    }
    const mappedKey = `${key}${mappingObj[qualifier]}${include ? mappingObj[include] : ''}`
    acc[mappedKey] = value
    return acc
  }, {})
}

export { getInitials, getUserType, buildVariables }
