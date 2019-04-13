from django.shortcuts import render

def index(request):
    return render(request, 'main/login/base_page.html')