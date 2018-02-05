from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'^list/', views.madadjooHa, name='index'),
    url(r'dashboard/(?P<username>.+)/hamyar_list/$', views.hamyar_list, name='hamyar_list'),
    url(r'dashboard/(?P<username>.+)/madadkar_info/$', views.madadkar_info, name='madadkar_info'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadjoo_dashboard'),
    url(r'^info/(?P<username>.+)/', views.madadjoo, name='index'),
    url(r'get_need_report/(?P<username>\D+)/$', views.needSearch, name='need_search'),
    url(r'report_hamyar/(?P<username>.+)/$', views.report_hamyar, name='report_hamyar'),
]
