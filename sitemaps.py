from django.contrib import sitemaps
from apps.company_directory.models import Company
from django.core.urlresolvers import reverse


class CompanySitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def location(self, item):
        return reverse('apps.company_directory.views.detail', kwargs={'company_id': item.id})

    def items(self):
        return Company.objects.all()

    def lastmod(self, obj):
        return obj.date_modified
