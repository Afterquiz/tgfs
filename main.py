from items import *
import items
import os
import time

#main defs

#example question
# print(items.name)
# print('q1')
# print('1 answer')
# print('2 answer')
# print('3 answer')

#answer = input("What do you chose")
#clear()

score = int(0)

print(s1)
wait()
print(a1)
wait()
print(a2)
wait()
print(a3)
wait()
answer = input("What do you chose?  ")

if answer == "1":
  score = int(score) + 1
elif answer == "2":
  score = int(score) + 2
elif answer == "3":
  score = int(score) + 3
else:
  af1 = "nothing"
  clear()
  print('That is not an option')
print(score)