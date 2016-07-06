from django.conf.urls import url, include

urlpatterns = [
    url(r'^tracker/', include('tracker.urls')),
]
