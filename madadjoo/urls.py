from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'^list/', views.madadjooHa, name='index'),
    url(r'dashboard/(?P<username>.+)/hamyar_list/$', views.hamyar_list, name='hamyar_list'),
    url(r'dashboard/(?P<username>.+)/madadkar_info/$', views.madadkar_info, name='madadkar_info'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadjoo_dashboard'),
    url(r'^info/(?P<username>.+)/', views.madadjoo, name='index'),
    url(r'get_need_report/(?P<username>\.+)/$', views.needSearch, name='need_search'),
    url(r'report_hamyar/(?P<username>.+)/$', views.report_hamyar, name='report_hamyar'),
    url(r'profile_madadjo/(?P<username>.+)/$', views.profile_madadjo, name='profile_madadjo'),
    url(r'get_notif/(?P<username>.+)/$', views.get_notif, name='get_notif'),
    url(r'inbox/(?P<username>.+)/$', views.inbox, name='inbox'),
    url(r'create_message/(?P<username>.+)/$', views.create_message, name='create_message'),
    url(r'send_message/(?P<sender>.+)/$', views.send_message, name='send_message'),
    url(r'send_reply/(?P<receiver>.+)/(?P<sender>.+)/(?P<subject>.+)/$', views.send_reply, name='send_reply'),
]
