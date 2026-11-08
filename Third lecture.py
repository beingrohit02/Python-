print("""LISTS IN PYTHON""")
#A built it data type that stores set of values
#It can store elements of different types (integers,float,str,etc.)

marks=[43.56,12.67,55,123,124.55,0] #marks[0] , marks[1]...............
print(marks[0]) #43.56
print(len(marks)) #returns lengths of the set
print(type(marks)) #type is "list"

#we can also use the lists like this
student=["Rohit",18,90,"Noida"]
print(student)

#in python we strings are inmutable which means we can access them but cannot change them
str="rohit"
print(str[0])
#str[0]=y
#but in lists it is mutable which means we can access and change them both
student=["Rohit",18,90,"Noida"]
print(student)
student[0]="Kumar" 
print(student) #changes the list

print("""LIST SLICING""")
#similar to string slicing
#list_name[Starting_idx : ending_idx] #where ending _idx is not included
marks=[76,34.345,77,11,34,24,56,79,43,10]
print(marks[1:5]) #[34.345, 77, 11, 34]
print(marks[0:]) #[76, 34.345, 77, 11, 34, 24, 56, 79, 43, 10]
print(marks[:len(marks)]) #[76, 34.345, 77, 11, 34, 24, 56, 79, 43, 10]
print(marks[:-1]) #[76, 34.345, 77, 11, 34, 24, 56, 79, 43]

print('LIST METHODS/FUNCTION')
list=[1,3,7,11,76,12]
list.append(325) #Adds the element to the list
print(list) 
list.sort() #sorts the list in ascending order
print(list)
list.sort(reverse=True) #sorts the list in descending order
print(list)
list.reverse() #reverses the list
print(list)
list.insert(3,56) #inserts the element to the given index number (idx,element
print(list)
list.remove(3) #removes the first occurence of element #it removes the number not from the index
print(list)
list.pop(2) #removes the element from the given index




print("TUPLES in Python")
#A built in data type that lets us create immutable sequences of value
tup = (41,5,3,1,8,99,44,76) #this is became a tuple now
print(type(tup)) #class=tuple
print(tup[0]) #41
print(tup[1]) #5

"tup[0]= 0" #return 'tuple' object does not support item assignment

tup1 = () #empty tuple
print(tup1) #returns "()"

tup2 = (1) #returns type integer 
tup3 = (1.0) #returns type float
tup4 = ("rohit") #returns type string

#but if we want to percieve the output as tuple we need to put coma after the data types to percieve it
tup5 = (1,) #returns type tuple
tup6 = (1.0,) #returns type tuple
tup7 = ("string",) #returns type tuple
print(type(tup7))

"""TUPLE SLICING (same as list)"""
tup=(1,2,3,4,5,6,7,8,9,0)
print(tup[3:9])

"""TUPLE METHODS"""
tup=(1,2,3,4,5,6,7,8,9,0,4,2,1,2,4,6,8,9,0,3,2,4,5,8)
print(tup.index(7)) #returns first index of the value
print(tup.count(2)) #returns number of occurence of the value


"""AN IMPORTANT POINT"""
"PALINDROME" #in programming palindrome of elements means the list is same from the back and front side both
#for eg [1,2,1]           [1,2,2,1]             [racecar]             [ma'am]

#to prove this

list1=[1,2,1] #palindrome
list2=[1,2,3] #non-palindrome

copy_list1= list1.copy()
copy_list1.reverse()
print(copy_list1) #hence it has been proved it is a palindrome

copy_list2 = list2.copy()
copy_list2.reverse()
print(copy_list2) #hence it has been proved it is a non-palindrome




