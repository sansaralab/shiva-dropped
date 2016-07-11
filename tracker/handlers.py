from .models import Trigger
from .types import TRIGGER_ACTION_TYPES


def handle_frontend_event(person_id: str, event_name: str, event_value: str):
    triggers = Trigger.objects.filter(action_type=TRIGGER_ACTION_TYPES['FRONTEND']).all()
    if len(triggers):
        return True
    return False
