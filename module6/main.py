
"""import emoji as e
import my_math as m
from m import square

def ssquare(x):
    print(x*x)

result= m.square(5)

print(result)
ssquare(8)
# librarit mund ti therrasim ne emra me te shkurt sipas deshires nepermjet "as ".

print(e.emojize("Python is so nice:snake:"))
"""
#shembull1 me funks
def gpa(g1,g2,g3,g4,g5,g6):
    shuma=g1+g2+g3+g4+g5+g6
    rezultati_final= shuma/6
    print(rezultati_final)
    if rezultati_final >= 3.5:
        print('You can join Harvard')
    else:
        print('Go to xhevedet dota')
gpa(2,4,4,3,5,4)


#sh2

def test(x):
   if x > 0:
       print('its a pozitive number')
   elif x == 0:
       print('its zero')
   else:
      print('its a negative number')

   if x % 2 == 0:
       print(" its an even number")
   else :
       print("its an odd number")
test(25)



import random
import string

colors=['black','yellow','green','blue','purple']
shape=['circle','square','hexagon','diamond']

print ('Welcome to password geerator')

while True:
    ngjyra = random.choice(colors)
    forma = random.choice(shape)
    number = random.randrange(10,100)
    char = random.choice(string.punctuation)

    password = ngjyra + forma + str(number)+ char
    print('Your new pass is: %s' % password)

    response =input('do u like ur password?do u want a new one?type y or n')
    if response== 'n':
        break