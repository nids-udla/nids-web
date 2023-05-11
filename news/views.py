from django.shortcuts import render

# Create your views here.
def smnews(request):
    return render(request, 'smnews.html')