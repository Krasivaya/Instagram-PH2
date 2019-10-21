from django.shortcuts import render

def signup(request):
    return render(request, 'registration/signup.html')
