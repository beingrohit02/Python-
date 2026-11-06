#this is my first program where i have started learning python language from basic
print("BASIC PROGRAMMING")
print("hello world" , "i am rohit")
print("hello world")
print("i am rohit")

"""here is the use of variable where u can assign any give data types to your line of code"""
#VARIABLE - a variable is a name give to a memory location in programming
name = "Rohit Kumar"
age = 18
print(age)
print(name)
#here is data types
print("DATA TYPES")
print("My Name is =" , name)
print("My Age is =" , age)
"""type of data
1- Integers (-ve,+ve,0)
2- Strings ("rohit","hello")
3- Float (decimal values)
4- Boolean (True and False)
5- None (no value stored in variable)"""

print(type(name)) #string
print(type(age)) #integer

age1=88
old=False

#we have to use capital F and capital T in True and False type of data otherwise it will be considered as syntax error becoz it is a keyword"""

a=None
price=6.669
print(type(a)) #none
print(type(age1)) #integer
print(type(old)) #boolean
print(type(price)) #float

#here's how we use the function of sum in python where can we multiplay,add,substract anything we want"""

print("SUM IN PYTHON")
a=87
b=67
sum=a+b
print(sum)

"""so comment is like ki tum isi apne line of code me use kro and so that you can indentify anything easily"""

print("COMMENT")
#kuch bhi likhdo bhai idhar it doesnt effect the line of your code that is your comment.
#ye to multiline comment hai vese tum isme sirf # laga kr b comment likh skte ho no prob.
#Python is case sensitive language where A is not equal to a.

print("""ARITHMATIC OPERATORS""") #+,-,*,/
a=6
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #we can use this to get output by rounding down the digits 
#also removes the last digit like decimals are removed when observered

a=6
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#modulo operators 
a=5
b=3
print(a%b) #for finding remainder
print(a**b) #for a to the power b a^b



""" RELATIONAL / COMPARISON OPERATORS """ #==,!=,<,>,<=,>=
#in mathematics we use a=b as equality but in programming we use """a==b""" as equality
#also to define inequality we use a/=b but in programming we use """a!=b""" whereas ! is used like to neglete things

a=5
b=7

print(a==b) #False #this is used to check the equality of two values which means that a is equal to b or not
print(a!=b) #True #this is used to check the inequality of two values which means that a is not equal to b
print(a>=b) #False this is used to check the greater than or equal to of two values
print(a<=b) #True this is used to check the less than or equal to of two values
print(a<b) #True
print(a>b) #False


"""ASSIGNMENT OPERATORS""" #=,+=,-=,*=,/=,%=,**=
print("assinghment")
num=10
num=num+10
print(num)

#here we can use num=num+10 as num+=10, both have same meaning

num=9
num+=10
print("answer :", num) #19
num=9
num-=10
print("answer :", num) #-1
num=9
num*=11 #used to multiply the value of num by 11
print("answer :", num) #99
num=9
num/=18
print("answer :", num) #0.5
num=9
num%=27 #used to find the remainder of the value of num divided by 27
print("answer :", num) #9
num=9
num**=3 #used to raise the value of num to the power of 3
print("answer :", num) #729


"""LOGICAL OPERATORS""" #not,and,or
print(not False) #True
print(not True) #False

#for eg not operator
a=50
b=70

print(not (a>b)) #true

#and, or operator
val1=True
val2=True

print("and answer :", val1 and val2) #true

val1=True
val2=False

print("and answer :", val1 and val2)

print("or answer :", val1 or val2)

print("and answer", a==b and a<b)
print("or answer", a==b or a<b)


"""TYPE CONVERSION""" #means to convert the type of a val to other type automatccally by the python
a=4
b=6.57
sum=a+b
print(sum) #10.57 python changes the type of the value

#for example python could not change this

a="5" #string
b=6.78 #float

#print(a+b) #error

"""TYPE CASTING""" #we manually change the type which python could not 
#to use this type of conversion we put int/float/bool/none/str(val)

a=float("9") #it can float or int
b=5.7

print(type(a)) #float
print(a+b)
"""u cannot convert the type of character value to int or float"""

a=9
a=str(a)
print(type(a)) #str



"""INPUT PROGRAMMING"""
#name=input("enter your name:")
#print("you entered - ", name)

#a=input("press any key to continue - ")
#print("WELCOME", name)

