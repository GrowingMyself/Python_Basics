#  Write a program that takes your favourite food name as input and print

# the middle 3 charters

# last 2characters mango

favouritefood = input("Enter your favourite food : ")

middle = favouritefood[1:4]

last = favouritefood[-2:]

print("middle character:",middle)

print("last character:",last)

print("length of your favourite foos is:",len(favouritefood))


# Write a program that :

# take a sentance as input
# converts it to lower case
# replace all spaces " " with underscore "_"
# prints the new string
# prachi more

sentence = input(" a sentence:")

sentence=sentence.lower()
sentence = sentence.replace(" ","_")
print(sentence)





