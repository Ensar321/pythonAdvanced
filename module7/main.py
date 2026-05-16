age = 20 #data tpye int
print(age)
after_one_year=age +1
print(after_one_year)
age_to_str=str(age)
print(age_to_str) #this will give an error cuz u cant sum a str and int

#int to float

mosha =21
mosha_float=float(mosha)
print(mosha_float)

#implicit type conversion

num1=10
num2=13.4
rezultati=num1+num2
print(rezultati)


vjetet=20
message= "une jam "+ str(vjetet) +" vjeq"
print(message)


rroga1=input(" shkruani rrogen e par ")
rroga2=input(" shkrunai rrogen e dyt ")
rroga1_float=float(rroga1)
rroga2_float = float(rroga2)
rroga_finale= rroga1_float + rroga2_float
print(rroga_finale)



try :
    rezult= 10/0
except ZeroDivisionError:
    print("Nuk mund te pjestoni me 0")


num1=input("shkruani numrin e par ")
num2 =input ("shkruani numrin e dyt ")
num1_int=int(num1)
num2_int=int(num2)

try:
    final_num = num1_int / num2_int
except ZeroDivisionError:
    print("nuk  mund te ndani me zero")
else:
    print(final_num)


fruits = {"apples":5,"banana":4,"orange":3}
try:
    print(fruits["grape"])
except:
    print("ky frut nuk eshte ne list")



name= "john"
age=20

try:
    biografia = name+ age
except Exception as e :
    print("ka ndodhur nje gabim :"+ str(e))

