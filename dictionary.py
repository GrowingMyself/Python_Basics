# A dictionery is build in data type in python used to store data in key value pairs.
#each key is unique ,dictionaries are unordered,mutable,and don't allow duplicate keys.
#dictionery are mutable.


#dictionery basics

student={
    "name":"prachi",
    "city":"karad",
    "age":"19",
    "roll no":"32",}
print(type(student))
print(student["name"])
print(student)
student["city"]="Delhi"#if i want to change the name or update this,
student["marks"]=95
student["favsubject"]="english"
print(student)
student.pop("favsubject")#if want to delect  any key
print(student)
print(student.keys())#if want to know which keys
print(student.values())#if wnat to values print in dictionery
print(student.items())#all key value print in tuple


#practice questions

marks={}
marks["maths"]=95
marks["chemistery"]=88
marks["computers"]=98
print(marks)

#sets = A set is a collection of unordered and unique items,sets automaticaly remove duplicate elements,uses{} brackets,cannot print duplicates

food= {"paneer","poha","upma","bhaji"}
print(type(food))
print(food)
food.add("chocolate")#add new food
print(food)
food.remove("paneer")
print(food)


# # You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert list into a set and print how many unique languages Divya knows.

programinglist=["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programinglist))
#how to conver list into set
programingset=set(programinglist)      
print(type(programingset))
print("divya knows these many languages:",len(programingset))






    
