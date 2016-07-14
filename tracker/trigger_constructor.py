from .types import TRIGGER_ACTION_TYPES, CONDITION_SEARCH_METHODS, CALLER_TYPES
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
        if caller_type not in CALLER_TYPES:
            raise InvalidArgumentException('caller_type must be in CALLER_TYPES')
        if 'caller_type' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_type'] = set()
        self._trigger.conditions['caller_type'].append(caller_type)
        return self

    def filter_caller_name(self, name, search_method):
        if search_method not in CONDITION_SEARCH_METHODS:
            raise InvalidArgumentException('search_method must be in CONDITION_SEARCH_METHODS')
        if 'caller_names' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_names'] = list()
        self._trigger.conditions['caller_names'].append({
            'name': name,
            'search': search_method
        })
        return self

    def filter_caller_value(self, name, search_method):
        if search_method not in CONDITION_SEARCH_METHODS:
            raise InvalidArgumentException('search_method must be in CONDITION_SEARCH_METHODS')
        if 'caller_datas' not in self._trigger.conditions.keys():
            self._trigger.conditions['caller_datas'] = list()
        self._trigger.conditions['caller_datas'].append({
            'name': name,
            'search': search_method
        })
        return self

    def add_reaction(self):
        return self


class InvalidArgumentException(Exception):
    pass
