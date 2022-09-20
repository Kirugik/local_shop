from rest_framework import serializers
from .models import Admin, Clerk, Product, Category, Order, DefectiveProduct

class AdminSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Admin
		fields ='__all__'

class ClerkSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Clerk
		fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Product
		fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta: 
		model = Category
		fields ='__all__'

class OrderSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Order
		fields ='__all__'

class DefectiveProductSerializer(serializers.ModelSerializer):
	class Meta: 
		model = DefectiveProduct
		fields ='__all__' 