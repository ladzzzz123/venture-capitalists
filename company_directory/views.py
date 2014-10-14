from django.shortcuts import render, render_to_response
from django.http import Http404
from company_directory.models import Company


def index(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'company_directory/index.html', context)


def detail(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404
    return render_to_response('company_directory/detail.html', {'company': company})
