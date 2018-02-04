from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'signup/', views.madsignup, name='signup'),
    url(r'dashboard/(?P<username>.+)/madadjo_list$', views.madadjo_list, name='madadjo_list'),
    url(r'dashboard/(?P<username>.+)/madadjo_list_madadkar$', views.madadjo_list_madadkar,
        name='madadjo_list_madadkar'),
    url(r'dashboard/(?P<username>.+)/$', views.show_dashboard, name='madadkar_dashboard'),
]
