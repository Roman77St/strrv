CATALOG_SOUNDS_ROOT = "mathematics/sounds/"
CATALOG_IMAGES_ROOT =  "mathematics/images/"

refresh_rate_images = 5

DEFAULT_NAME = "Anonimus🗿"

sounds = {
    "ok": "ok.mp3",
    "mistake": "mistake.mp3",
    "start": "start.mp3",
    "molodets": "molodets.mp3",
    "oi": "oi.mp3",
}

sounds = {key: CATALOG_SOUNDS_ROOT + value for (key, value) in sounds.items()}

image_animal = [
    "mikrob.png",
    "gusenitsa.png",
    "ulitka.png",
    "juk.png",
    "dragonfly.png",
    "fish.png",
    "shark.png",
    "lagushka.png",
    "yascheritsa.png",
    "crocodile.png",
    "mouse.png",
    "rabbit.png",
    "kapibara.png",
    "dog.png",
    "elephant.png",
    "monkey.png",
    "baby.png",
    "kid.png",
    "student.png",
    "albert_einstein.png",
]

image_animal = [CATALOG_IMAGES_ROOT + animal for animal in image_animal]

levels = {
    'biginner': 'Новичок',
    'pupil': 'Ученик',
    'profi': 'Профессионал',
    'academician': 'Академик'
}
