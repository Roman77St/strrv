from django.shortcuts import render

# Create your views here.
def mathematics(request):
    return render(request, 'mathematics/math.html')