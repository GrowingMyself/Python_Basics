#write a program that takes name of 3 favourite foods from the user and stores them in a list. then print the list and its length


food1=(input("enter your 1st favourite food:"))
food2=(input("enter your 2nd favourite food:"))
food3=(input("enter your 3rd favourite food:"))


foodlist=[food1,food2,food3]
print(foodlist)
print("length of the food is:",len(foodlist))



#methods in list

#1 indexing
#list is mutable
marks= [99,100,90,95]
print(marks)
marks[1]=98
print(marks)
#strings are immutable

#slicing
print(marks[1:4])

print(max(marks))
print(min(marks))
marks.append(92)
print(marks)
marks.sort()
print(marks)
marks.pop(1)
print(marks)
marks.remove(90)
print(marks)
marks.insert(1,100)
print(marks)

        

        























3
