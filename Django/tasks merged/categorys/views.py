from http.client import HTTPResponse
from math import prod
from django.shortcuts import render , redirect , get_object_or_404
from categorys.models import category
# Create your views here.


def indexview(request):
    categs=category.get_all_categorys()   #-----------------------------------------------------
    return render(request,"categorys/index.html",context={"categorys":categs})

def showcategory(request,id):
    c=category.get_one_category(id)
    return render(request,"categorys/showcategory.html",context={"category":c})
    
def createcategory(request):
    if(request.POST):
        c=category()   #----------------------------------------
        c.name=request.POST["name"]
        if(request.FILES["image"]):
            c.image=request.FILES["image"]  #-------------------------------------------------------
        c.save()
        
        url=category.get_index_url()
        return redirect(url)
        # allproducts =product.get_all_products() 
        # return render(request,"products/index.html",context={"products":allproducts })

    return render(request , "categorys/create_category.html")

def deletecategory(request,id):
    c = get_object_or_404(category , pk=id)
    c.delete()
    allcategorys =category.get_all_categorys() 
    return render(request,"categorys/index.html",context={"categorys":allcategorys })

def editcategory(request,id):
    c=category.get_one_category(id)
    if(request.POST):
        c.name=request.POST["name"] 
        if(request.FILES["image"]):
            c.image=request.FILES["image"]   
        c.save()
        
        url=c.get_url()
        return redirect(url)
    return render(request , "categorys/edit_category.html" , context={"category":c})
