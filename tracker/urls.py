from django.conf.urls import url
from .views import tracker_serve, track, attach_contact, send_event, attach_data


urlpatterns = [
    url(r'shiva.js$', tracker_serve),
    url(r'track$', track),
    url(r'attach$', attach_contact),
    url(r'data$', attach_data),
    url(r'event$', send_event),
]
