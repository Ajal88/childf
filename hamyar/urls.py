from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'get_madadjo_list_all/(?P<hamyarusername>.+)/info/(?P<madadjoousername>.+)/$', views.madadjoo,
        name='madadjo'),
    url(r'get_madadkar_list_all/(?P<hamyarusername>.+)/info/(?P<madadkarusername>.+)/$', views.madadkar_info,
        name='madadkar'),
    url(r'inbox/(?P<username>.+)/$', views.inbox, name='inbox'),
    url(r'send_reply/(?P<receiver>.+)/(?P<sender>.+)/(?P<subject>.+)/$', views.send_reply, name='send_reply'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='show_dashboard'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'send_message/(?P<sender>.+)/$', views.send_message, name='send_message'),
    url(r'notification/(?P<username>.+)/$', views.get_notif, name='get_notif'),
    url(r'madadjo_list/(?P<username>.+)/$', views.get_madadjo_list, name='get_madadjo_list'),
    url(r'create_message_madadjo/(?P<username>.+)/$', views.create_message_madadjo, name='create_message_madadjo'),
    url(r'create_message_madadkar/(?P<username>.+)/$', views.create_message_madadkar, name='create_message_madadkar'),
    url(r'get_madadjo_list_all/(?P<username>.+)/$', views.get_madadjo_list_all, name='get_madadjo_list_all'),
    url(r'get_madadkar_list_all/(?P<username>.+)/$', views.get_madadkar_list_all, name='get_madadkar_list_all'),
    url(r'get_madadkar_list/(?P<username>.+)/$', views.get_madadkar_list, name='get_madadkar_list'),
    url(r'get_financial_report/(?P<username>.+)/$', views.get_financial_report, name='get_financial_report'),
    url(r'profile_hamyar/(?P<username>.+)/$', views.profile_hamyar, name='profile_hamyar'),
    url(r'change_profile/(?P<username>.+)/$', views.change_profile, name='change_profile'),
    url(r'send_change_profile/(?P<username>.+)/$', views.send_change_profile, name='send_change_profile'),
]
