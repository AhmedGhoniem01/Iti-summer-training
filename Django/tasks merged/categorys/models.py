
from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="media/categorys/images")


    @classmethod
    def get_all_categorys(cls):
        return cls.objects.all()
    
    @classmethod
    def get_one_category(cls,category_id):
        return cls.objects.get(id=category_id)

    @classmethod
    def get_index_url(cls):
        return reverse("categorys.index")

    def get_url(self):
        return reverse("category.show" , args=[self.id])
    
    def get_img_url(self):
        return f"/media/{self.image}"

    def __str__(self):
        return f"{self.name}"   
    

    