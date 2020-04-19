from django.urls import path

from api.views.view_generic import CompanyListAPIView, CompanyDetailAPIView, \
                                    VacancyListAPIView, VacancyDetailAPIView, \
                                    VacancyTopAPIView, CompanyWithVacancies

from api.views.views import top_vacancy

from api.views.views import vacancies_list



from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # FUNCTION BASED VIEW
    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_detail),



    # CLASS BASED VIEW
    # path('companies/', CompanyListAPIView.as_view()),
    # path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),


    path('login/', obtain_jwt_token),

    # GENERIC VIEW
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),

    path('companies/<int:company_id>/vacancies/', vacancies_list),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('vacancies/top/', top_vacancy),
]