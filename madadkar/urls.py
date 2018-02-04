from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'dashboard/(?P<username>\D+)/$', views.show_dashboard, name='madadkar_dashboard'),
]
