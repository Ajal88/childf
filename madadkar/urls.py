from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'dashboard/(?P<madadkarusername>.+)/info/(?P<madadjoousername>.+)/$', views.madadjoo,
        name='madadjo'),
    url(r'dashboard/(?P<username>.+)/madadjo_list$', views.madadjo_list, name='madadjo_list'),

    url(r'dashboard/(?P<username>.+)/madadjo_list_madadkar/$', views.madadjo_list_madadkar,
        name='madadjo_list_madadkar'),
    url(r'dashboard/(?P<username>.+)/madadjo_list_poshesh/$', views.madadjo_list_pooshesh,
        name='madadjo_list_pooshesh'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadkar_dashboard'),
    url(r'get_mkfinancial_report/(?P<username>\D+)/$', views.get_mkfinancial_report, name='get_mkfinancial_report'),
]
