TRIGGER_ACTION_TYPES = {
    'BACKEND': 0,
    'FRONTEND': 1
}

TRIGGER_ACTION_TYPE_CHOICES = (
    (TRIGGER_ACTION_TYPES['BACKEND'], 'Backend trigger'),
    (TRIGGER_ACTION_TYPES['FRONTEND'], 'Frontend trigger'),
)

CONDITION_SEARCH_METHODS = {
    'STARTS': 1,
    'CONTAINS': 2,
    'ENDS': 3,
    'EQUALS': 4,
    'NEQUALS': 5,
    'REGEXP': 6
}

CALLER_TYPES = {
    'EVENT': 1,
    'CONTACT': 2,
    'DATA': 3
}
