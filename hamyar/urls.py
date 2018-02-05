from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'inbox/(?P<username>\D+)/$', views.inbox, name='inbox'),
    url(r'send_reply/(?P<receiver>\D+)/(?P<sender>\D+)/(?P<subject>\D+)/$', views.send_reply, name='send_reply'),
    url(r'dashboard/(?P<username>\D+)/$', views.show_dashboard, name='hamyar_dashboard'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'send_message/(?P<sender>\D+)/$', views.send_message, name='send_message'),
    url(r'notification/(?P<username>\D+)/$', views.get_notif, name='get_notif'),
    url(r'madadjo_list/(?P<username>\D+)/$', views.get_madadjo_list, name='get_madadjo_list'),
    url(r'create_message_madadjo/(?P<username>\D+)/$', views.create_message_madadjo, name='create_message_madadjo'),
    url(r'create_message_madadkar/(?P<username>\D+)/$', views.create_message_madadkar, name='create_message_madadkar'),
    url(r'get_madadjo_list_all/(?P<username>\D+)/$', views.get_madadjo_list_all, name='get_madadjo_list_all'),
    url(r'get_madadkar_list_all/(?P<username>\D+)/$', views.get_madadkar_list_all, name='get_madadkar_list_all'),
    url(r'get_madadkar_list/(?P<username>\D+)/$', views.get_madadkar_list, name='get_madadkar_list'),
    url(r'get_financial_report/(?P<username>\D+)/$', views.get_financial_report, name='get_financial_report'),
    url(r'profile_hamyar/(?P<username>\D+)/$', views.profile_hamyar, name='profile_hamyar'),
]
