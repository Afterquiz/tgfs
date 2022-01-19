from items import *
import os
import time
from progress.bar import ChargingBar

clear()

score = int(0)

print(name)
input("")
print(ps1)
input("")
clear()
progbar()
clear()

print(name)
print(s1)
wait()
print(q1)
wait()
print(a1)
wait()
print(a2)
wait()
print(a3)
wait()
print("")
answer = input('what will you choose? ')

if answer.upper() == "A":
  score = int(score) + 1
elif answer.upper() == "B":
  score = int(score) + 2
elif answer.upper() == "C":
  score = int(score) + 3
else:
  clear()
  print(name)
  print(error)
  print("Problem:")
  print('Unvalid input error')
  time.sleep(999999)
  
clear()
qprogbar()
clear()

print(name)
print(s2)
wait()
print(q2)
wait()
print(a4)
wait()
print(a5)
wait()
print(a6)
wait()
print("")
answer = input('what will you choose? ')

if answer.upper() == "A":
  score = int(score) + 3
elif answer.upper() == "B":
  score = int(score) + 1
elif answer.upper() == "C":
  score = int(score) + 2
else:
  clear()
  print(name)
  print(error)
  print("Problem:")
  print('Valid input error')
  time.sleep(999999)

clear()
qprogbar()
clear()

print(name)
print(s3)
wait()
print(q3)
wait()
print(a7)
wait()
print(a8)
wait()
print(a9)
wait()
print("")
answer = input('what will you choose? ')

if answer.upper() == "A":
  score = int(score) + 2
elif answer.upper() == "B":
  score = int(score) + 1
elif answer.upper() == "C":
  score = int(score) + 3
else:
  clear()
  print(name)
  print(error)
  print("Problem:")
  print('Valid input error')
  time.sleep(999999)

clear()
qprogbar()
clear()

print(name)
print(s4)
wait()
print(q4)
wait()
print(a10)
wait()
print(a11)
wait()
print(a12)
wait()
print("")
answer = input('what will you choose? ')

if answer.upper() == "A":
  score = int(score) + 2
elif answer.upper() == "B":
  score = int(score) + 1
elif answer.upper() == "C":
  score = int(score) + 3
else:
  clear()
  print(name)
  print(error)
  print("Problem:")
  print('Valid input error')
  time.sleep(999999)

clear()
qprogbar()
clear()

print(name)
print(s5)
wait()
print(q5)
wait()
print(a13)
wait()
print(a14)
wait()
print(a15)
wait()
print("")
answer = input('what will you choose? ')

if answer.upper() == "A":
  score = int(score) + 2
elif answer.upper() == "B":
  score = int(score) + 1
elif answer.upper() == "C":
  score = int(score) + 3
else:
  clear()
  print(name)
  print(error)
  print("Problem:")
  print('Valid input error')
  time.sleep(999999)

clear()
progbar()
clear()

if score == 3 and score <8 :
  print(name)
  print (end1)
elif score >= 8 and score <=11 :
  print(name)
  print (end2)
else :
  print(name)
  print (end3)