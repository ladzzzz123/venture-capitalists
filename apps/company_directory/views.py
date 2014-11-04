from django.shortcuts import render
from django.http import Http404
from apps.company_directory.models import Company


def index(request):
    city = request.GET.get('city', '')
    state = request.GET.get('state', '')
    capital = request.GET.get('capital', '')

    # get all of the companies then filter those companies based on the query made
    companies = Company.objects.all()
    if(city != ''):
        companies = companies.filter(city=city)
    if(state != ''):
        companies = companies.filter(state__name=state)
    if(capital != ''):
        companies = companies.filter(capital__gte=capital)

    return render(request, 'company_directory/index.html', {'companies': companies})


def detail(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404
    return render(request, 'company_directory/detail.html', {'company': company})
