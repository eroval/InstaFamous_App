# from instapy import InstaPy
from instabot import Bot
import time
import os
import random

people_i_actually_follow={"bellahadid","ralitsa._.s","emchoou","krisgeorgievv","tedtoefoe","alex_gogosheva","dragomir_asamov",
"georgizayakov", "ppatanasov98", "spasivanov98", "__mitranov__", "ympetkov", "z_madzharov", "techo.k", "killtheliver", "iliyanstratiev99",
"rali.zheleva"}


print(people_i_actually_follow)

people_of_similar_content = ["davidlaid", "madisonbeer", "selenagomez"]

username = "zangarovgram"
password = ""

bot = Bot()
bot.login(username = username, password = password)



def follow_people():
    max_follows_per_day = random.randint(150, 250)
    cnt = 0
    for i in range(0,max_follows_per_day):
        person=random.randint(0,2)
        followers = bot.get_user_followers(people_of_similar_content[person])
        name = bot.get_username_from_user_id(followers[5])
        bot.follow(name)

follow_people()
