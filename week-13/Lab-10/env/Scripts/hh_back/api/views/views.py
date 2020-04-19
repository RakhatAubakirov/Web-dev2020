from django.http.response import JsonResponse
from api.models import Company
from api.models import Vacancy



def company_list(request):
    products = Company.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
# Create your views here.

def company_detail(request, company_id):
    try:
        product = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())

def vacancies_list(request, company_id):
    vacancies = Vacancy.objects.filter(company_id=company_id)
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(list_json, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    products_json = [product.to_json() for product in vacancies]
    return JsonResponse(products_json, safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        product = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())

def top_vacancy(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(list_json, safe=False)

# Create your views here.
