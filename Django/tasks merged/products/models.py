from tkinter import CASCADE
from django.urls import reverse
from django.db import models
from categorys.models import category

# Create your models here.

class product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100 , null=True)
    image= models.CharField(max_length=100)
    price=models.IntegerField(default=10)
    no_of_items=models.CharField(max_length=100 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, null=True , blank=True , on_delete=models.CASCADE, related_name="products_categorys")

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    
    @classmethod
    def get_one_product(cls,product_id):
        return cls.objects.get(id=product_id)
    
    @classmethod
    def get_index_url(cls):
        return reverse("products.index")

    def get_url(self):
        return reverse("product.show" , args=[self.id])
    
    