from django.urls import path
from api.views.views_generic import CategoryListAPIView, CategoryDetailAPIView, \
                                    ProductListAPIView, ProductDetailAPIView, \
                                    ProductTopAPIView, CategoryWithProducts

from api.views.views_cbv import CategoryListAPIView, CategoryDetailAPIView
from api.views.views_fbv import category_list, category_detail, product_by_category, top_product, product_by_category

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
path('login/', obtain_jwt_token),

path('categories/', category_list),
path('categories/<int:category_id>/', category_detail),
path('categories/<int:pk>/products/', product_by_category),
path('products/', ProductListAPIView.as_view()),
path('products/<int:pk>/', ProductDetailAPIView.as_view()),
path('products/top/', top_product),
]