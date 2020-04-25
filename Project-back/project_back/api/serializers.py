from rest_framework import serializers
from api.models import Category, Product, Comment, User

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    img = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', validated_data)
        instance.img = validated_data.get('img', validated_data)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    #category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'img')




class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', validated_data)
        instance.description = validated_data.get('description')
        instance.save()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')




class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')