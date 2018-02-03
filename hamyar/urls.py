from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'inbox/(?P<username>\D+)/$', views.inbox, name='inbox'),
    url(r'send_reply/(?P<receiver>\D+)/(?P<sender>\D+)/(?P<subject>\D+)/$', views.send_reply, name='send_reply'),

    url(r'dashboard/(?P<username>\D+)/$', views.show_dashboard, name='hamyar_dashboard'),
    url(r'signup/$', views.signup, name='signup'),

]
