from django.db import models

# Create your models here.
from django.urls import reverse

# Create your models here.

class course(models.Model):
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="media/courses/images")
    max_grade=models.IntegerField(default=100)


    @classmethod
    def get_all_courses(cls):
        return cls.objects.all()
    
    @classmethod
    def get_one_course(cls,course_id):
        return cls.objects.get(id=course_id)

    @classmethod
    def get_index_url(cls):
        return reverse("courses.index")

    def get_url(self):
        return reverse("course.show" , args=[self.id])
    
    def get_img_url(self):
        return f"/media/{self.image}"

    def __str__(self):
        return f"{self.name}"   
    

    