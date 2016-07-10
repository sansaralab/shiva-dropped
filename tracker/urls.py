from django.conf.urls import url
from .views import tracker_serve, track, attach_info, send_event


urlpatterns = [
    url(r'shiva.js$', tracker_serve),
    url(r'track$', track),
    url(r'attach$', attach_info),
    url(r'event$', send_event),
]
