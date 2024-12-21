import random
# from summator import play_sound, image_animal

levels = {
    'biginner': 'Новичок',
    'pupil': 'Ученик',
    'profi': 'Профессионал',
    'academician': 'Академик'
}

def set_max_value(request):

    match request.session['choice_action']:
        case 'plus': factor = 1
        case 'minus': factor = 2
        case 'mult': factor = 1
        case 'divide': factor = 10

    match request.session['choice_level']:
        case 'biginner': max_value = 10 * factor
        case 'pupil': max_value = 20 * factor
        case 'profi': max_value = 100 * factor
        case 'academician': max_value = 1000 * factor

    return max_value



    



def save_in_session(request, name, choice_action, choice_level):
    if name == '':
        request.session['name'] = "Anonimus🗿"
    else:
        request.session['name'] = name
    request.session['choice_action'] = choice_action
    request.session['choice_level'] = choice_level
    request.session['first_round'] = True
    



def summator(request):
    max_value = set_max_value(request)
    print(max_value)
    if request.method == 'GET':
        request.session['a'] = random.randint(1, max_value)
        request.session['b'] = random.randint(1, max_value)
        request.session['points'] = 0
        message = '❓'

    if request.method == 'POST':
        answer = request.POST['answer']
        result = str(request.session['a'] + request.session['b'])
        print(answer)
        
        if answer == result:
            request.session['points'] += 1
            message = "Молодец!"
            print('all write', answer)
        else:
            request.session['points'] -= 1
            print('wrong', answer)
            message = f"Не правильно🤔 Правильный ответ: {result}"

        request.session['a'] = random.randint(1, max_value)
        request.session['a'] = random.randint(1, max_value)

    task = f'{request.session['a']} + {request.session['b']}'
    data = {
        'sound': 'sound',
        'task': task,
        'image': 'image',
        'message': message,
        'level': levels[request.session['choice_level']]
    }
    return data
    
    # name = request.session['name']
    # choice_action = request.session['choice_action']
    # choice_level = request.session['choice_level']
    # first_round = request.session['first_round']



    # if first_round:
    #     print('!!!')
    #     points = 0
    #     image = "mathematics/images/fish.png"
    #     request.session['first_round'] = False




