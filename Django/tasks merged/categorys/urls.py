from django.urls import path
from . import views

from categorys.views import indexview , showcategory , createcategory , deletecategory , editcategory

urlpatterns = [
    path('index/' , indexview , name="categorys.index"),
    path('show/<int:id>/' , showcategory , name="category.show"),
    path("create" , createcategory , name="category.create"),
    path('delete/<int:id>/' , deletecategory , name="category.delete"),
    path('edit/<int:id>/' , editcategory , name='category.edit'),

]

