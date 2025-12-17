from django.http import HttpResponse
from django.shortcuts import render
items={
    "iphone":"apple",
    "samsung":"samsung korea",
}
def index(request):
    return HttpResponse("I am home page")
def products(request):
    return render(request,'products.html',
                  {
                      "data":items,
                  })
def productsdetails(request,p):
    value=items.get(p)
    return render(request,'productsdetails.html',{
        "maker":value,
    })