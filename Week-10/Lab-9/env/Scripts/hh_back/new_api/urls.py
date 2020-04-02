from django.urls import path

from new_api.views import company_list, company_detail, vacancies_list,vacancy_list, vacancy_detail, top_vacancy
urlpatterns= [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', vacancies_list),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top_vacancy),

]