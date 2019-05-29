from django.shortcuts import render

# Create your views here.
def main(request):
    pass

def login(request):
    return render(request, 'website/login.html')