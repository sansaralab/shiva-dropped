from .types import TRIGGER_ACTION_TYPES, CONDITION_SEARCH_METHODS, CALLER_TYPES, REACTION_TYPES
from .models import Trigger


class TriggerConstructor():
    def __init__(self):
        self._trigger = Trigger()
        self._trigger.conditions['format'] = 1

    def set_active(self, active: bool):
        self._trigger.active = active
        return self

    def set_name(self, name: str):
        self._trigger.name = name
        return self

    def set_online(self, online: bool):
        self._trigger.online = online
        return self

    def set_action_type(self, action_type: int):
        if action_type not in TRIGGER_ACTION_TYPES.values():
            raise InvalidArgumentException('Action type must be in TRIGGER_ACTION_TYPES')

        self._trigger.action_type = action_type
        return self

    def add_caller_type(self, caller_type: str):
        if caller_type not in CALLER_TYPES.values():
            raise InvalidArgumentException('caller_type must be in CALLER_TYPES')
        if 'caller_type' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_type'] = set()
        self._trigger.conditions['caller_type'].add(caller_type)
        return self

    def filter_caller_name(self, name, search_method):
        if search_method not in CONDITION_SEARCH_METHODS.values():
            raise InvalidArgumentException('search_method must be in CONDITION_SEARCH_METHODS')
        if 'caller_names' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_names'] = list()
        self._trigger.conditions['caller_names'].append({
            'name': name,
            'search': search_method
        })
        return self

    def filter_caller_value(self, name, search_method):
        if search_method not in CONDITION_SEARCH_METHODS.values():
            raise InvalidArgumentException('search_method must be in CONDITION_SEARCH_METHODS')
        if 'caller_datas' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_datas'] = list()
        self._trigger.conditions['caller_datas'].append({
            'name': name,
            'search': search_method
        })
        return self

    def add_reaction(self, reaction_type, method=None, url=None, payload=None, parameters=None):
        if reaction_type not in REACTION_TYPES.values():
            raise InvalidArgumentException('reaction_type must be in REACTION_TYPES')
        reaction = dict()
        if reaction_type == REACTION_TYPES['request']:
            if not any((method, url)):
                raise InvalidArgumentException('When reaction type is request then method and url is required')
            reaction['type'] = reaction_type
            reaction['method'] = method
            reaction['url'] = url
        elif reaction_type == REACTION_TYPES['js']:
            if not payload:
                raise InvalidArgumentException('When reaction type is js then payload is required')
            reaction['payload'] = payload
        if isinstance(parameters, list):
            if len(parameters) > 0:
                reaction['parameters'] = list()
                for parameter in parameters:
                    if not hasattr(parameter, 'type'):
                        raise InvalidArgumentException('Type is required in each parameters element')
                    if not hasattr(parameter, 'value'):
                        raise InvalidArgumentException('Value is required in each parameters element')
                    if parameter['type'] == 'static':
                        reaction['parameters'].append({
                            'type': parameter['type'],
                            'value': parameter['value']
                        })
                    elif parameter['type'] == 'context':
                        if not hasattr(parameter, 'name'):
                            raise InvalidArgumentException('Name is required if parameter type is context')
                        reaction['parameters'].append({
                            'type': parameter['type'],
                            'value': parameter['value'],
                            'name': parameter['name']
                        })
        if 'reactions' not in self._trigger.conditions.keys():
            self._trigger.conditions['reactions'] = list()
        self._trigger.conditions['reactions'].append(reaction)
        return self

    def save(self):
        self._trigger.save()
        return self._trigger


class InvalidArgumentException(Exception):
    pass
