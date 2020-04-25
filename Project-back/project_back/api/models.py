from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,

        }


class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img,
        }






class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.FloatField()
    #category = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='products', null=True)
    img = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'img': self.img,

        }




class Comment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

