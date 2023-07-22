import telebot
import random
import rand

bot = telebot.TeleBot('token');

# random.randint(a, b)

color_like = "color_like"
color_dislike = "color_dislike"
music_like = "music_like"
music_dislike = "music_dislike"
says_like = "says_like"
says_dislike = "says_dislike"
theme_like = "theme_like"
theme_dislike = "theme_dislike"
fashion_like = "fashion_like"
fashion_dislike = "fashion_dislike"
hobby_like = "hobby_like"
hobby_dislike = "hobby_dislike"
decor_like = "decor_like"
decor_dislike = "decor_dislike"

text_color = "Цвета: \nок: " + color_like + "\nфу: " + color_dislike
text_music = "\n\nЖанр музыки:\nок: " + music_like + "\nфу: " + music_dislike
text_says = "\n\nКачества персонажа:\nок: " + says_like + "\nфу: " + says_dislike
text_theme = "\n\nТемы разговора:\nок: " + theme_like + "\nфу: " + theme_dislike
text_fashion = "\n\nМода:\nок: " + fashion_like + "\nфу: " + fashion_dislike
text_hobby = "\n\nУвлечения:\nок: " + hobby_like + "\nфу: " + hobby_dislike
text_decor = "\n\nДекор:\nок: " + decor_like + "\nфу: " + decor_dislike

text = text_color + text_music + text_says + text_theme + text_fashion + text_hobby + text_decor

@bot.message_handler(commands=['start'])
def get_text_messages(message):
    text_color = rand.get_color(11)
    text_music = rand.get_music(38)
    text_says = rand.get_says(18)
    text_theme = rand.get_theme(18)
    text_fashion = rand.get_fashion(9)
    text_hobby = rand.get_hobby(35)
    text_decor = rand.get_decor(21)
    text = text_color + text_music + text_says + text_theme + text_fashion + text_hobby + text_decor
    bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    bot.polling(none_stop=True)