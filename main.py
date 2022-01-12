import items
import os
import time

def clear():
  try:
    os.system( 'clear' )
  except:
    os.system( 'cls' )

def wait():
  time.sleep(2)

def answer():
  answer = input("What do you chose")


print('TGFS')
clear()

#example question
# print(items.name)
# print('q1')
# print('1 answer')
# print('2 answer')
# print('3 answer')

#answer = input("What do you chose")
#clear()

print(items.s1)
wait()
print(items.a1)
wait()
print(items.a2)
wait()
print(items.a3)
wait()
answer()


# if answer1 == "1":
#   a1 = "1"
#   print('user chose 1')
# elif answer1 == "2":
#   print('user chose 2')
#   a1 = "2"
# elif answer1 == "3":
#   print('user chose 3')
#   a1 = "3"
# else:
#   clear()
#   print('That is not an option')

#teleport system example
# if a1 == 1:
#   print('')

