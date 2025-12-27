from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def charts(request):
    return render(request, 'home/charts.html')

def tables(request):
    return render(request, 'home/tables.html')

def buttons(request):
    return render(request, 'home/buttons.html')

def cards(request):
    return render(request, 'home/cards.html')

def register(request):
    return render(request, 'home/register.html')

def forgot_password(request):
    return render(request, 'home/forgot_password.html')

def blank(request):
    return render(request, 'home/blank.html')

def page_404(request):
    return render(request,'home/404.html')

def utilities_color(request):
    return render(request, 'home/utilities_color.html')

def utilities_other(request):
    return render(request, 'home/utilities_other.html')

def utilities_border(request):
    return render(request, 'home/utilities_border.html')

def utilities_animation(request):
    return render(request, 'home/utilities_animation.html')