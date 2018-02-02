from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/', views.madadjooHa, name='index'),
    url(r'^(?P<username>.+)/', views.madadjoo, name='index'),
]
