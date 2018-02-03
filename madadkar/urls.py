from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dashboard/(?P<username>\D+)/$', views.show_dashboard, name='madadkar_dashboard'),
]
