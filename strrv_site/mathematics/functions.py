import random
# from summator import play_sound, image_animal



def save_in_session(request, name, choice_action, choice_level):
    request.session['name'] = name
    request.session['choice_action'] = choice_action
    request.session['choice_level'] = choice_level
    request.session['first_round'] = True


a = 0
b = 0
points = 0

def summator(request):
    global a
    global b
    global points

    if request.method == 'GET':
        a = random.randint(1, 10)
        b = random.randint(1, 10)

    if request.method == 'POST':
        answer = request.POST['answer']
        print(answer)
        points += 1
        if answer == str(a + b):
            print('all write', answer)
        else:
            print('wrong', answer)

        a = random.randint(1, 10)
        b = random.randint(1, 10)

    task = f'{a} + {b}'
    data = {
        "points": points,
        'sound': 'sound',
        'task': task,
        'image': 'image'
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




