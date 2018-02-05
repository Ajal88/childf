"""childf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

import karbar.views
import madadjoo.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', karbar.views.home, name='home'),
    url(r'^company_info/', karbar.views.company_inf, name='cmp_info'),
    url(r'^company_inf/activity4', karbar.views.company_act4, name='cmp_info4'),
    url(r'^company_inf/activity5', karbar.views.company_act5, name='cmp_info5'),
    url(r'^auth/', include('karbar.urls')),
    url(r'^search/', madadjoo.views.search, name='search'),
    url(r'^madadjoo/', include('madadjoo.urls')),
    url(r'^hamyar/', include('hamyar.urls')),
    url(r'^madadkar/', include('madadkar.urls')),
    url(r'^modir/', include('modir.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

admin.site.site_header = 'مدیریت وبگاه موسسه‌ی بنیاد کودک'
admin.site.site_title = 'موسسه‌ی بنیاد کودک'
