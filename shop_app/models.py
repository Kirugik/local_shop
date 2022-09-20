from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['username']
    def __str__(self):
        return self.username



class Clerk(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100) 
    # password = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name'] 

    def __str__(self):
        return self.first_name 


        
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['category_name']
    def __str__(self):
        return self.category_name  



class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    unit_cost = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        ordering = ['product_name'] 
    def __str__(self):
        return self.product_name 



class Order(models.Model):
    ordered_product = models.CharField(max_length=50) 
    quantity = models.IntegerField() 
    clerk = models.ForeignKey(Clerk, on_delete=models.CASCADE) 
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['ordered_product'] 
    def __str__(self):
        return self.ordered_product 



class DefectiveProduct(models.Model):
    defective_product_name = models.CharField(max_length=50) 
    categorization = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['defective_product_name'] 
    def __str__(self):
        return self.defective_product_name  
    
    

