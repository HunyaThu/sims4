import random
import prefence

def random_preference(a,b):
    if a == 1:
        preference = prefence.color(b)
    elif a == 2:
        preference = prefence.music(b)
    elif a == 3:
        preference = prefence.says(b)
    elif a == 4:
        preference = prefence.theme(b)
    elif a == 5:
        preference = prefence.fashion(b)
    elif a == 6:
        preference = prefence.hobby(b)
    elif a == 7:
        preference = prefence.decor(b)
    return preference


def random_like(all,a):
    b = str(random.randint(1,all))
    like =  random_preference(a,b)
    return like

def random_dislike(all,a):
    b = str(random.randint(1,all))
    dislike = random_preference(a,b)
    return dislike

def get_color(all):
    color_like = random_like(all,1)
    color_dislike = random_dislike(all,1)
    text_color = "Цвета: \nок: " + color_like + "\nфу: " + color_dislike
    return text_color

def get_music(all):
    music_like =  random_like(all,2)
    music_dislike = random_dislike(all,2)
    text_music = "\n\nЖанр музыки:\nок: " + music_like + "\nфу: " + music_dislike
    return text_music

def get_says(all):
    says_like = random_like(all,3)
    says_dislike = random_dislike(all,3)
    text_says = "\n\nКачества персонажа:\nок: " + says_like + "\nфу: " + says_dislike
    return text_says

def get_theme(all):
    theme_like = random_like(all,4)
    theme_dislike = random_dislike(all,4)
    text_theme = "\n\nТемы разговора:\nок: " + theme_like + "\nфу: " + theme_dislike
    return text_theme

def get_fashion(all):
    fashion_like = random_like(all,5)
    fashion_dislike = random_dislike(all,5)
    text_fashion = "\n\nМода:\nок: " + fashion_like + "\nфу: " + fashion_dislike
    return text_fashion

def get_hobby(all):
    hobby_like = random_like(all,6)
    hobby_dislike = random_dislike(all,6)
    text_hobby = "\n\nУвлечения:\nок: " + hobby_like + "\nфу: " + hobby_dislike
    return text_hobby

def get_decor(all):
    decor_like = random_like(all,7)
    decor_dislike = random_dislike(all,7)
    text_decor = "\n\nДекор:\nок: " + decor_like + "\nфу: " + decor_dislike
    return text_decor






