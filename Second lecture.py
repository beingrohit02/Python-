print("""'String and Conditional Statements'""")

#for example 
str1="i am a string. using in python"
print(str1)
#here if we want to move the second line down we cant
#here we use "\n" which moves the second line to the next line
#here
str2="Hi I am Rohit. \nLearning python" #\n is used for changing the line
print(str2)

print("'concatenation'") #adding two words
str1= "hello"
str2= " world"
print(str1+str2)

print("'length of string'") #finding length of string
str3="touch some grass"
len1=len(str3)
str4="banana"
len2=len(str4)
print(len1)
print(len2)

print("""'INDEXING'""")
#helps to access characters 
#for example we have a string      R O H I T   K U M A R
#_____________________________     0 1 2 3 4 5 6 7 8 9 10
# here how it is number assigned to each other
str="Rohit Kumar"
print(str[7]) #use sqaure brackets to find string

print("""'SLICING'""") #accessing parts of a string
#str=rohit kumar
#str[starting idx : ending idx] 
'ending idx is not included'

str="Rohit Kumar"
toslice=str[0:5]
print(toslice)

#to at the last index
toslice1=str[0:] #leaving the ending idx empty 
print(toslice1)

print('"negative index"')
#for example we have R  O  H  I  T
#                   -5 -4 -3 -2 -1
str="Rohit"
print(str[-5:-3])

print("""'String Function'""")

str="i am a Vibe Coder and learning python."

print(str.endswith("python.")) #return true if string ends with it

print(str.capitalize()) #capatalizes first character

#if we want to make changes in string value then we can do 
str="i am a Vibe Coder and learning python."
str=str.capitalize()
print(str)

str="i am a Vibe Coder and learning python."
#print(str.replace("old","new"))

print(str.replace("python","javascript"))  #replaces the word

print(str.find("Vibe")) #returns first index to the first occurer

print(str.count("a")) #counts the occurence of the substract

print("'Conditional Statements'")
#if(condition)
#statement1
#elif(condtion)
#statement2
#else:
#statementN

print('"if statements"')
age=21
if(age >= 18):
    print("You can vote \nand drive")

print('"if and elif statements"')
light = "red"
if(light=="green"):
    print("GO AHEAD")
elif(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("LOOK THEN GO")
#you can use if and elif how much you want but you can only use elif after using if

print('"if,elif and else statement"')
light = "blue"
if(light=="green"):
    print("GO AHEAD")
elif(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("LOOK THEN GO")
else:
    print("not possible")


#example of marks and grade
#marks=int(input("ENTER YOUR MARKS TO CALCULATE GRADE = "))
marks=89
if(marks>=90):
    print("GRADE : A")
elif(marks>=80 and marks<90):
    print("GRADE : B")
elif(marks>=70 and marks<80):
    print("GRADE : C")
elif(marks>=60 and marks<70):
    print("GRADE : D")
else:
    print("GRADE : E")

print("'Nesting is so much important'")

age1=9
if(age1>=18):
    if(age1<18):                                 #NESTING
        print("YOUR ARE CHILD GO PLAY")
    else:
        print("YOU CAN VOTE")
else:
    print("YOUR ARE CHILD GO PLAY")        

#whenever we have to find any multiple or something like odd or even
# we can use % to find thier remainder particularly
'for eg'
'let some number is odd or even. how can we prove it in python'
a=int(input("ENTER YOUR NUMBER"))

value=a%2 #see carefully here i have used 2 as to find remainder as for even number the all are divisible by 2 and we can prove it even
if(value==0):
    print("EVEN")
else:
    print("ODD")
