from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'navigation/index.html')

def contact(request):
    return render(request, 'navigation/contact.html')

def news(request):
    return render(request,'navigation/news.html')

def about(request):
    return render(request, 'navigation/about.html')
