#create a tuple of your favourite 5 foods
#the total numbers of fruit
#the index of one selected fruit

foodTuple= ("mango","apple","banana","papaya","chery")
print("the total numbers of fruite:",len(foodTuple))
print("the index of one selected fruite:",foodTuple.index("apple"))


#practice question
#ask the user for their 3 favorite movies and store them in a list
#create a tuple of marks(87,64,33,95,76)and print the highest and lowest marks using max(),min()
#write a program to check grads based on the marks(A,B,C,D)usingif-elif-else

movie1= (input("enter your 1st favorite movies:"))
movie2= (input("enter your 2nd favorite movies:"))
movie3= (input("enter your 3rd favorite movies:"))

movie=[movie1,movie2,movie3]
print("my favorite movies are:",movie)

marks= int(input("Enter your marks:"))
marksTuple=(87,64,33,95,76)
print=("highest marks:",max(marksTuple))
print=("lowest marks:",min(marksTuple))



