from django.shortcuts import render

# Create your views here.
def steam(request):
    return render(request, 'steam.html')