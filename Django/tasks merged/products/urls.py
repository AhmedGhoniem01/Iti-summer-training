from django.urls import path
from . import views

from products.views import indexview , showproduct , createproduct , deleteproduct ,editproduct

urlpatterns = [
    path('index/' , indexview , name="products.index"),
    path('show/<int:id>/' , showproduct , name="product.show"),
    path("create" , createproduct , name="product.create"),
    path('delete/<int:id>/' , deleteproduct , name="product.delete"),
    path('edit/<int:id>/' , editproduct , name='product.edit'),

]

