from django.contrib import admin
from django.forms.widgets import FileInput
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from company_directory.models import Company
from company_directory.models import State


class ImageWidget(FileInput):
    """
    A ImageField Widget that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a rel="facebox" target="_blank" href="%s">'
                           '<img class="photo" src="%s" style="height: 100px;" /></a> <br/>'
                           % (value.url, value.url)))
        output.append(super(ImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class CompanyAdminForm(ModelForm):
    class Meta:
        model = Company
        widgets = {
            'logo': ImageWidget(),
        }


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    fields = ['logo', 'name', 'email', 'phone', 'address', 'city', 'state', 'zip']

admin.site.register(Company, CompanyAdmin)
admin.site.register(State)
