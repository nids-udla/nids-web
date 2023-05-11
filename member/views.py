from django.shortcuts import render

# Create your views here.
def slogin(request):
    return render(request, 'slogin.html')