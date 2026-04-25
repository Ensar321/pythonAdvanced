def greet():
    print("hello world")
greet()

def shuma(num1,num2):
    rezultati=num1+num2
    print(rezultati)
shuma(20,40)

def pershendetja(name):
        print(f"Hello",name)
pershendetja('ensar')

hello="pershendetje"
def pershendetje(name,age):
    print(f'{hello} dear {name},you re {age}years old')
pershendetje("ensar",17)


#default arguments ,argumente qe marrin

def welcome( name,mesazhi="Hello"):
    print(f'{mesazhi} dear {name}')

welcome('Ensar' ,'Kujebre')