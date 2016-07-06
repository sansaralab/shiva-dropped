from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'shiva.js$', tracker_serve),
    url(r'track$', track)
]
