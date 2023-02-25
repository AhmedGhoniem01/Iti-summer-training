from django.shortcuts import render , redirect , get_object_or_404
from courses.models import course
from courses.forms import CourseModelForm
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.contrib.auth.decorators import login_required

# def indexview(request):
#     allcourses=course.get_all_courses()   
#     return render(request,"courses/index.html",context={"courses":allcourses})
# @login_required
class CourseListView(ListView):
    model = course
    template_name = "courses/index.html"

# def showcourse(request,id):
#     selected_course=course.get_one_course(id)
#     return render(request,"courses/showcourse.html",context={"course":selected_course})

class CourseDetailView(DetailView):
    model = course
    template_name = "courses/showcourse.html"
    
# def createcourse(request):
#     if(request.POST):
#         form=CourseModelForm(request.POST , request.FILES)
#         form.save()
#         url=course.get_index_url()
#         return redirect(url)
 
#     form=CourseModelForm()
#     return render(request , "courses/createcourse.html" , context={"form":form})

class CourseCreateView(CreateView):
    model = course
    form_class = CourseModelForm
    template_name = 'courses/createcourse.html'
    success_url ='/courses/index'   

# def editcourse(request,id):
#     selected_course=course.get_one_course(id)
#     if(request.POST):
#         form=CourseModelForm(request.POST , request.FILES , instance=selected_course)
#         form.save()
#         url=selected_course.get_url()
#         return redirect(url)
    
#     form=CourseModelForm(instance=selected_course)
#     return render(request , "courses/editcourse.html" , context={"form":form , "selected_course":selected_course})

class CourseUpdateView(UpdateView):
    model = course
    template_name = 'courses/editcourse.html'
    success_url ='/courses/index' 
    form_class = CourseModelForm

class CourseDeleteView(DeleteView):
    model = course
    success_url ='/courses/index' 
    template_name = 'courses/deletecourse.html'

