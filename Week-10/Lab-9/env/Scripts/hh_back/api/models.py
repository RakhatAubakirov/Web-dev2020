from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    city = models.CharField(max_length=200)
    address = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,

        }









class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')

    company = models.ForeignKey(Company,  on_delete=models.CASCADE,
                                 related_name='vacancy')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,

        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }








# Create your models here.
