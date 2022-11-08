from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'kelsioportfolio/index.html')

def projects(request):
    return render (request, 'kelsioportfolio/projects.html')

def services(request):
    return render (request, 'kelsioportfolio/services.html')

def about(request):
    return render (request, 'kelsioportfolio/about.html')