from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import crname
# Create your views here.
def inm(request):
    obj=place.objects.all()
    obj2=crname.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj2})
