from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer, AdminSerializer, ClerkSerializer, OrderSerializer, DefectiveProductSerializer
from .models import Category, Product, Clerk, Admin, Order, DefectiveProduct
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




# orders api
@api_view(['GET'])
def current_orders(request):
    orders = Order.objects.all().order_by('-id')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def order_info(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_order_info(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def remove_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response("Order deleted successfully!")




# defective products api
@api_view(['GET'])
def defective_products_list(request):
    defective_products = DefectiveProduct.objects.all().order_by('-id')
    serializer = DefectiveProductSerializer(defective_products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_defective_product(request):
    serializer = DefectiveProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def defective_product_info(request, pk):
    defective_product = DefectiveProduct.objects.get(id=pk)
    serializer = DefectiveProductSerializer(defective_product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_defective_product(request, pk):
    defective_product = DefectiveProduct.objects.get(id=pk)
    serializer = ProductSerializer(instance=defective_product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def remove_defective_product(request, pk):
    defective_product = DefectiveProduct.objects.get(id=pk)
    defective_product.delete()
    return Response("Defective product deleted successfully!")




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

@api_view(['GET'])
def clerk_details(request, pk):
    clerk = Clerk.objects.get(id=pk)
    serializer = ClerkSerializer(clerk, many=False)
    return Response(serializer.data) 

@api_view(['PUT'])
def update_clerk_details(request, pk):
    clerk = Clerk.objects.get(id=pk)
    serializer = ClerkSerializer(instance=clerk, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['DELETE'])
def remove_clerk(request, pk):
    clerk = Clerk.objects.get(id=pk)
    clerk.delete()
    return Response("Clerk removed successfully!")




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

@api_view(['GET'])
def admin_details(request, pk):
    admin = Admin.objects.get(id=pk)
    serializer = AdminSerializer(admin, many=False)
    return Response(serializer.data) 

@api_view(['PUT'])
def update_admin_details(request, pk):
    admin = Admin.objects.get(id=pk)
    serializer = AdminSerializer(instance=admin, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def remove_admin(request, pk):
    admin = Admin.objects.get(id=pk)
    admin.delete()
    return Response("Admin removed successfully!")




