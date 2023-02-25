from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterationForm
# Create your views here.
def userRegister(request):
    if(request.POST):
        form = UserRegisterationForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f"Account Successfully Created For {username}, You can login now")
            return redirect('login')
            
    else:
        form = UserRegisterationForm()
    return render(request , 'users/register.html' , context={"form":form} )










