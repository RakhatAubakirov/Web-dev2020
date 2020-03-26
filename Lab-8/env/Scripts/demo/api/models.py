from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name

        }


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    count = models.IntegerField()
    description = models.TextField()
    #category_id = models.ForeignKey(Category, on_delete=models.CASCADE)



    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'description': self.description,

        }


# Create your models here.
