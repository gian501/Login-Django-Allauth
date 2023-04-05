from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'Registro/home.html')

def profile(request):
    return render(request, 'account/profile.html')