import os
import time
from progress.bar import ChargingBar
#defy
def clear():
  try:
    os.system( 'clear' )
  except:
    os.system( 'cls' )

def wait():
  time.sleep(2)

def progbar():
  print(name)
  bar = ChargingBar('Loading Afterquiz', max=100)
  for i in range(120):
      time.sleep(0.03)
      bar.next()
  bar.finish()


def qprogbar():
  print(name)
  bar = ChargingBar('Loading next question', max=80)
  for i in range(85):
      time.sleep(0.01)
      bar.next()
  bar.finish()

def answerbar():
  bar = ChargingBar('Loading Answears', max=100)
  for i in range(120):
      time.sleep(0.001)
      bar.next()
  bar.finish()

error = """
█▀▀ █▀█ █▀█ █▀█ █▀█
██▄ █▀▄ █▀▄ █▄█ █▀▄"""

#ostatní lol
name = """
░█████╗░███████╗████████╗███████╗██████╗░  ░██████╗░██╗░░░██╗██╗███████╗
██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ██╔═══██╗██║░░░██║██║╚════██║
███████║█████╗░░░░░██║░░░█████╗░░██████╔╝  ██║██╗██║██║░░░██║██║░░███╔═╝
██╔══██║██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗  ╚██████╔╝██║░░░██║██║██╔══╝░░
██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ░╚═██╔═╝░╚██████╔╝██║███████╗
╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝
© ProgStar Inc. 
________________________________________________________________________"""
ps1 = """Hello. 
  Welcome to Afterquiz. 
  This quiz is made to predict the future of people in 10 to 15 years. 
  We will give you random situations and you will tell us what would you do next in this 
  situation. 
  Based on your answers, we will be able to predict what your life will look like in about
  10 to 15 years. 
  This will also help with our first Afterquiz testing. 
  So take a seat and enjoy your own prediction."""
#1st set of questions
#s1 = "Your close friends went to a nightclub and you don'tave nothing to do"
s1 = "Your close friend want to go to the party tonight and asked you, if you want to go with him"
q1 = """You have nothing planed. what will you do??
 """
a1 = "a) I will stay at home."
a2 = "b) I will go with them but only drink non alkoholic drinks."
a3 = "c) I will go there and drink and party with them."
#2ond set of questions
s2 = "You are going to the bus stop, and you see a wallet laying on the floor."
q2 = "You are in extreme hurry.  what will you do?"
a5 = "i will leave it there."
a4 = "i will take it and pretend that it´s mine."
a6 = "i will just say someone to do something with it."
