from django.shortcuts import render

# Home page with 3D background
def home(request):
    # You can pass dynamic data here if needed
    return render(request, 'index.html')

# About page
def about(request):
    return render(request, 'about.html')

# Features page
def features(request):
    return render(request, 'features.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')
