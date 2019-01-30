from math import *
'''jsut learnning python'''

print(round(22/7))
string = input("Give me a string : ")
print("The string u used was : " +string)
l = len(string)
#need to reverse inputed string
print(string [::-1])

num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = float(num1) + float(num2) #can also cast at intpur but too crowdy
print("%s + %s = %0.2f" %(num1, num2, result)) #formatted printing

array = [1,2,3] #list fns
print(array[2])
array[2] = "99"
print(array[-1])
