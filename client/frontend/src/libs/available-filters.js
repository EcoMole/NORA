export const availableFilters = {
  'novel food title': {
    group: 'novel food',
    type: 'text',
    qualifiers: ['is'],
    description:
      'Novel Food title is the name of the product. It is a text field and can be queried using the "is" qualifier.'
  },
  // not working examples bellow
  'production process': {
    group: 'production process',
    type: 'text',
    qualifiers: ['contains', 'is'],
    description:
      'this is more information and explanation about the production process filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
  },
  'opinion regulation': {
    group: 'administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    description:
      'this is more information and explanation about the opinion regulation filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
  },
  'date of publication': {
    group: 'administrative',
    type: 'date',
    qualifiers: ['is', 'is greater than', 'is less than'],
    description:
      'this is more information and explanation about the date of publication filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
  },
  'type mandate': {
    group: 'administrative',
    type: 'text',
    qualifiers: ['contains', 'is'],
    description:
      'this is more information and explanation about the type mandate filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
  }
}
