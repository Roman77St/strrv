from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .functions import save_in_session, summator


def mathematics(request):
    if request.method == "POST":
        # app_summator = Summator(request)
        name = request.POST['name']
        choice_action = request.POST['choice_action']
        choice_level = request.POST['choice_level']
        save_in_session(request, name, choice_action, choice_level)
        return redirect(to=reverse_lazy('math:realisation'))
    return render(request, 'mathematics/math.html')

def realisation(request):
    if request.method == "POST":
        # answer = request.POST['answer']
        data = summator(request)

    else:
        data = summator(request)
    context = {
        "user": request.session['name'],
        'sound': 'sound',
        'points': request.session['points'],
    }

    context = context | data


    return render(request, 'mathematics/realisation.html', context=context)