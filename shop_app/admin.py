from django.contrib import admin
from .models import Admin, Clerk, Product, Category, Order, DefectiveProduct

# Register your models here.
admin.site.register(Admin)
admin.site.register(Clerk)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(DefectiveProduct) 
