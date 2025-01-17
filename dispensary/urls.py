# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
import django.contrib.staticfiles.urls


admin.site.site_title = u'Кировский спортивный диспансер'
admin.site.site_header = u'Кировский спортивный диспансер'


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^', admin.site.urls),
    url(r'^admin/salmonella/', include('salmonella.urls')),
] + django.contrib.staticfiles.urls.urlpatterns
