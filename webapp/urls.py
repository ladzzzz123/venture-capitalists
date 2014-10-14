from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('home.urls')),
    url(r'^companies/', include('company_directory.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
