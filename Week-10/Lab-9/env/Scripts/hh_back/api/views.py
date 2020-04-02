from django.shortcuts import render
from django.http import JsonResponse
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

def vacancy_company(request, category_id):
    try:
        category = Company.objects.get(id=category_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.products.all()
    products_json = [product.full() for product in products]

    return JsonResponse(products_json, safe=False)