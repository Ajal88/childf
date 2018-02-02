from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'inbox/(?P<username>\D+)/$', views.inbox, name='inbox'),
    url(r'inbox/sendmail/$', views.sendmail, name='sendmail'),
]
