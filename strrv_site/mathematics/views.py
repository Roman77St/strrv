from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .functions import save_in_session, summator
from .functions import DEFAULT_NAME



def mathematics(request):

    if request.method == "POST":
        name = request.POST['name']
        choice_action = request.POST['choice_action']
        choice_level = request.POST['choice_level']
        save_in_session(request, name, choice_action, choice_level)
        return redirect(to=reverse_lazy('math:realisation'))
    
    name = request.session.get('name')
    name = name.strip().replace(' ', '\xa0')
    if name == DEFAULT_NAME:
        name = ''

    context = {
        'name': name
    }
    return render(request, 'mathematics/math.html', context)

def realisation(request):

    data = summator(request)

    context = {
        "user": request.session['name'],
        'points': request.session['points'],
    }

    context = context | data


    return render(request, 'mathematics/realisation.html', context=context)