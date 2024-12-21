import random
from .catalog import image_animal, sounds, levels, refresh_rate_images

def save_in_session(request, name, choice_action, choice_level):
    if name == '':
        request.session['name'] = "Anonimus🗿"
    else:
        request.session['name'] = name
    request.session['choice_action'] = choice_action
    request.session['choice_level'] = choice_level
    request.session['first_round'] = True


def set_max_value(request):
    match request.session['choice_action']:
        case 'plus': factor = 1
        case 'minus': factor = 2
        case 'mult': factor = 0.5
        case 'divide': factor = 0.5

    match request.session['choice_level']:
        case 'biginner': max_value = 10 * factor
        case 'pupil': max_value = 20 * factor
        case 'profi': max_value = 100 * factor
        case 'academician': max_value = 1000 * factor
    return int(max_value)

def set_symbol(request):
    match request.session['choice_action']:
        case 'plus': symbol = '+'
        case 'minus': symbol = '-'
        case 'mult': symbol = '*'
        case 'divide': symbol = ':'
    return symbol

def get_result(request):
    a = request.session['a']
    b = request.session['b']
    match request.session['choice_action']:
        case 'plus': result =  a + b
        case 'minus': result = a - b
        case 'mult': result = a * b
        case 'divide': result = int(a / b)
    return str(result)

def set_variables(request):
    max_value = set_max_value(request)
    a = random.randint(1, max_value)
    b = random.randint(1, max_value)
    if request.session['choice_action'] == 'minus':
        if a < b:
            a, b = b, a
    if request.session['choice_action'] == 'divide':
        a = a * b

    request.session['a'] = a
    request.session['b'] = b


def summator(request):

    

    if request.method == 'GET':
        request.session['points'] = 0
        message = '❓'
        set_variables(request)
        sound = sounds['start']

    if request.method == 'POST':

        answer = request.POST['answer']
        result = get_result(request)
        
        if answer == result:
            request.session['points'] += 1
            message = "Молодец!"
            sound = sounds['molodets']
        else:
            request.session['points'] -= 1
            message = f"Не правильно🤔 Правильный ответ: {result}"
            sound = sounds['oi']

        set_variables(request)

    symbol = set_symbol(request)

    task = f'{request.session['a']} {symbol} {request.session['b']}'

    position_image = request.session['points'] // refresh_rate_images

    if position_image < 0:
        image = image_animal[0]
    elif 0 <= position_image < len(image_animal):
        image = image_animal[position_image]
    else:
        image = image_animal[len(image_animal)-1]
    
    data = {
        'sound': sound,
        'task': task,
        'image': image,
        'message': message,
        'level': levels[request.session['choice_level']]
    }
    return data
