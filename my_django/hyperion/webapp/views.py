from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>Hello World</h2>")
def index(request):
    return render(request, "index.html")

# Create your views here.
