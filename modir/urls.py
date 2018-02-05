from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadkar_dashboard'),
    url(r'show_message_to_all/(?P<username>.+)/$', views.show_message_to_all, name='show_message_to_all'),
    url(r'send_message_to_all/(?P<username>.+)/$', views.send_message_to_all, name='send_message_to_all'),
]
