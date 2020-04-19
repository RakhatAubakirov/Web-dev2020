from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Company, Vacancy

from api.serializers import CompanyModelSerializer, CompanyWithVacanciesSerializer, VacancySerializer
from rest_framework import mixins


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    permission_classes = (IsAuthenticated,)

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer

class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyTopAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-salary')[:10]
    serializer_class = VacancySerializer

class CompanyWithVacancies(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacanciesSerializer

