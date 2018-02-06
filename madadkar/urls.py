from django.conf.urls import url

from . import views
from madadjoo.views import need_pays

urlpatterns = [
    url(r'notification/(?P<username>.+)/$', views.get_notif, name='get_notif'),
    url(r'signup/', views.madsignup, name='signup'),
    url(r'dashboard/(?P<madadkarusername>.+)/info/(?P<madadjoousername>.+)/$', views.madadjoo,
        name='madadjo'),
    url(r'dashboard/(?P<username>.+)/madadjo_list$', views.madadjo_list, name='madadjo_list'),

    url(r'dashboard/(?P<username>.+)/madadjo_list_madadkar/$', views.madadjo_list_madadkar,
        name='madadjo_list_madadkar'),
    url(r'dashboard/(?P<username>.+)/madadjo_list_poshesh/$', views.madadjo_list_pooshesh,
        name='madadjo_list_pooshesh'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadkar_dashboard'),
    url(r'get_mkfinancial_report/(?P<username>.+)/$', views.get_mkfinancial_report, name='get_mkfinancial_report'),
    url(r'send_message/(?P<sender>.+)/$', views.send_message, name='send_message'),
    url(r'create_message/(?P<username>.+)/$', views.create_message, name='create_message_madadkar'),
    url(r'send_reply/(?P<receiver>.+)/(?P<sender>.+)/(?P<subject>.+)/$', views.send_reply, name='send_reply'),
    url(r'profile/(?P<username>.+)/$', views.profile_madadkar, name='profile_madadkar'),
    url(r'change_profile/(?P<username>.+)/$', views.change_profile, name='change_profile'),
    url(r'send_change_profile/(?P<username>.+)/$', views.send_change_profile, name='send_change_profile'),
    url(r'need_pays/(?P<username>.+)/$', need_pays, name='need_pay')
]
