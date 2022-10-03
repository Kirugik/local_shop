from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer, AdminSerializer, ClerkSerializer
from .models import Category, Product, Clerk, Admin
# from shop_app import serializers

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, this is local shop index page. Welcome!")

# categories api  
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def category_info(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def remove_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("Category deleted successfully!")





# products api
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request, pk):
    product = Product.objects.get(id=pk)
    serializer = CategorySerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_product_info(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def remove_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product deleted successfully!")




# clerks api
@api_view(['GET'])
def all_clerks(request):
    clerks = Clerk.objects.all().order_by('-id')
    serializer = ClerkSerializer(clerks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_clerk(request):
    serializer = ClerkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




# admins api
@api_view(['GET'])
def all_admins(request):
    admins = Admin.objects.all().order_by('-id')
    serializer = AdminSerializer(admins, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)