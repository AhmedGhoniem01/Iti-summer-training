from django.urls import path
from . import views

# from courses.views import indexview , showcourse , createcourse , editcourse
from courses.views import CourseListView , CourseDetailView , CourseCreateView , CourseUpdateView , CourseDeleteView

urlpatterns = [
    # path('index/' , indexview , name="courses.index"),
    path('index/' , CourseListView.as_view() , name="courses.index"),

    # path('show/<int:id>/' , showcourse , name="course.show"),
    path('show/<int:pk>' , CourseDetailView.as_view() , name="course.show"),

    # path("create" , createcourse , name="course.create"),
    path('create' , CourseCreateView.as_view() , name="course.create"),

    # path('edit/<int:id>/' , editcourse , name='course.edit'),
    path('edit/<int:pk>' , CourseUpdateView.as_view() , name="course.edit"),

    path('delete/<int:pk>' , CourseDeleteView.as_view() , name="course.delete"),
]

