from django.shortcuts import render
from django.http import Http404
from apps.company_directory.models import Company


def index(request):
    companies = Company.objects.all()
    return render(request, 'company_directory/index.html', {'companies': companies})


def detail(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404
    return render(request, 'company_directory/detail.html', {'company': company})
