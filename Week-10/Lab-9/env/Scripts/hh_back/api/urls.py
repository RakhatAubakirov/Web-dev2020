from django.urls import path

from api.views import company_list, company_detail
urlpatterns= [
    path('companies/', company_list),
    path('companies/<int:company_id>', company_detail)
]