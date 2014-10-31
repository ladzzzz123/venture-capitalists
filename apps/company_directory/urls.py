from django.conf.urls import patterns, url

from apps.company_directory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<company_id>\d+)/$', views.detail, name='detail'),
)
