from django.urls import path
from . import views

urlpatterns = [ 
    # path('', views.index, name='home'), 
    path('categories/', views.category_list, name='category-list'),
    path('create-category/', views.create_category, name='create-category'), 
    path('category-info/<int:pk>/', views.category_info, name='category-info'),
    path('update-category/<int:pk>/', views.update_category, name='update-category'), 
    path('remove-category/<int:pk>/', views.remove_category, name='remove-category'),


    path('products/', views.product_list, name='product-list'), 
    path('new-product', views.new_product, name='new-product'),
    path('product-info/<int:pk>', views.product_info, name='product-info'),
    path('update-product/<int:pk>/', views.update_product_info, name='update-product'), 
    path('remove-product/<int:pk>/', views.remove_product, name='remove-product'),
] 