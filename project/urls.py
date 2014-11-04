from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import django.contrib.sitemaps.views as sitemap_views
from sitemaps import CompanySitemap

admin.autodiscover()

sitemaps = {
    'static': CompanySitemap,
}

urlpatterns = patterns('',
    url(r'^', include('apps.home.urls')),
    url(r'^companies/', include('apps.company_directory.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap_views.index, {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', sitemap_views.sitemap, {'sitemaps': sitemaps}),
    # May not be necessary for production environment?
    # Bridge will be crossed once we get there
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT})
)
