from django.conf.urls import patterns, url

from company_directory import views

urlpatterns = patterns('',
    # ex: /companies/
    url(r'^$', views.index, name='index'),
    # ex: /companies/5/
    url(r'^(?P<company_id>\d+)/$', views.detail, name='detail'),
)
