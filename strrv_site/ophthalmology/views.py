from django.shortcuts import render


def recomend_list(request):
    return render(request, 'ophthalmology/recomend_list.html')

def recomend_item(request):
    return render(request, 'ophthalmology/recomend_item.html')