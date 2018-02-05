from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='modir_dashboard'),
    url(r'show_message_to_all/(?P<username>.+)/$', views.show_message_to_all, name='show_message_to_all'),
    url(r'send_message_to_all/(?P<username>.+)/$', views.send_message_to_all, name='send_message_to_all'),
    url(r'notification/(?P<username>.+)/$', views.get_notif, name='get_notif'),
    url(r'create_message/(?P<username>.+)/$', views.create_message, name='create_message'),
    url(r'send_message/(?P<sender>.+)/$', views.send_message, name='send_message'),
    url(r'send_reply/(?P<receiver>.+)/(?P<sender>.+)/(?P<subject>.+)/$', views.send_reply, name='send_reply'),
    url(r'change_profile/(?P<username>.+)/$', views.change_profile, name='change_profile'),
    url(r'send_change_profile/(?P<username>.+)/$', views.send_change_profile, name='send_change_profile'),
]
