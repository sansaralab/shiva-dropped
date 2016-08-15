TRIGGER_REACTION_SIDES = {
    'BACKEND': 0,
    'FRONTEND': 1
}


TRIGGER_REACTION_SIDE_CHOICES = (
    (TRIGGER_REACTION_SIDES['BACKEND'], 'Backend trigger'),
    (TRIGGER_REACTION_SIDES['FRONTEND'], 'Frontend trigger'),
)


CONDITION_SEARCH_METHODS = {
    'STARTS': 1,
    'CONTAINS': 2,
    'ENDS': 3,
    'EQUALS': 4,
    'NEQUALS': 5,
    'REGEXP': 6
}


ACTION_TYPES = {
    'EVENT': 1,
    'CONTACT': 2,
    'DATA': 3
}


REACTION_TYPES = {
    'request': 1,
    'js': 2
}


REQUEST_METHODS = {
    'get',
    'post'
}


class HandlerResponse:
    person = None
    javascript = None

    def __init__(self, person, javascript = None):
        self.person = person
        self.javascript = javascript

    def get_javascript_as_string(self):
        return 'alert("hello test!");'
