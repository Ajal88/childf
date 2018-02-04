from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'^list/', views.madadjooHa, name='index'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadjoo_dashboard'),
    url(r'^info/(?P<username>.+)/', views.madadjoo, name='index'),
    url(r'report_hamyar/(?P<username>.+)/$', views.report_hamyar, name='report_hamyar'),
]
