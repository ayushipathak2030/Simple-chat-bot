# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:17:14 2020

@author: user
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


    

while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)