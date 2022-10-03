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

    path('orders/', views.current_orders, name='orders'),
    path('create-order/', views.create_order, name='create-order'),
    path('order-info/<int:pk>/', views.order_info, name='order-info'),
    path('update-order/<int:pk>/', views.update_order_info, name='update-order'),
    path('remove-order/<int:pk>/', views.remove_order, name='remove-order'),

    path('defective-products/', views.defective_products_list, name='defective-products'),
    path('create-defective-product/', views.create_defective_product, name='create-defective-product'),
    path('defective-product-info/<int:pk>/', views.defective_product_info, name='defective-product-info'),
    path('update-defective-product/<int:pk>/', views.update_defective_product, name='update-defective-product'),
    path('remove-defective-product/<int:pk>/', views.remove_defective_product, name='remove-defective-product'),

    path('clerks/', views.all_clerks, name='clerks'), 
    path('add-clerk/', views.add_clerk, name='add-clerk'), 
    path('clerk-details/<int:pk>/', views.clerk_details, name='clerk-details'),
    path('update-clerk/<int:pk>/', views.update_clerk_details, name='update-clerk'),
    path('remove-clerk/<int:pk>/', views.remove_clerk, name='remove-clerk'),  
    
    path('admins/', views.all_admins, name='admins'), 
    path('add-admin/', views.add_admin, name='add-admin'), 
    path('admin-details/<int:pk>/', views.admin_details, name='admin-details'),
    path('update-admin/<int:pk>/', views.update_admin_details, name='update-admin'), 
    path('remove-admin/<int:pk>/', views.remove_admin, name='remove-admin'),
] 