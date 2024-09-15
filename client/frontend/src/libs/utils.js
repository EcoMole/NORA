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
  'must have': 'Filter',
  'must not have': 'Exclude'
}

function buildVariables(addedFilters) {
  console.log('addedFilters', addedFilters)
  return addedFilters.reduce((acc, { key, qualifier, include, value }) => {
    const mappedKey = `${key}${mappingObj[qualifier]}${mappingObj[include]}`
    acc[mappedKey] = value
    return acc
  }, {})
}

export { getInitials, getUserType, buildVariables }
