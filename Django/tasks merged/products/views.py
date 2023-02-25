# from http.client import HTTPResponse
# from math import prod
# from unicodedata import category
from django.shortcuts import render , redirect , get_object_or_404
from products.models import product
from categorys.models import category
# Create your views here.


def indexview(request):
    products=product.get_all_products()   #-----------------------------------------------------
    return render(request,"products/index.html",context={"products":products})

def showproduct(request,id):
    p=product.get_one_product(id)
    return render(request,"products/showproduct.html",context={"product":p})
    
def createproduct(request):
    if(request.POST):
        p=product()   
        p.title=request.POST["title"] 
        p.description=request.POST["description"]
        p.image=request.POST["image"]  
        p.price=request.POST["price"]  
        p.no_of_items=request.POST["no_of_items"]  
        if(request.POST["category"]):
            p.category=category.get_one_category(request.POST["category"])
        p.save()
        url=p.get_url()
        return redirect(url)
        # allproducts =product.get_all_products() 
        # return render(request,"products/index.html",context={"products":allproducts })
    allcategorys=category.get_all_categorys()
    return render(request , "products/create_product.html" , context={"categorys":allcategorys})

def deleteproduct(request,id):
    p = get_object_or_404(product , pk=id)
    p.delete()
    allproducts =product.get_all_products() 
    return render(request,"products/index.html",context={"products":allproducts })

def editproduct(request,id):
    p=product.get_one_product(id)
    if(request.POST):

        p.title=request.POST["title"] 
        p.description=request.POST["description"]
        p.image=request.POST["image"]  
        p.price=request.POST["price"]  
        p.no_of_items=request.POST["no_of_items"]  
        if(request.POST["category"]):
            p.category=category.get_one_category(request.POST["category"])        
        p.save()
        
        url=p.get_url()
        return redirect(url)

    allcategorys=category.get_all_categorys()
    return render(request , "products/edit_product.html" , context={"product":p , "categorys":allcategorys})


    

