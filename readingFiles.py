# Reading files :- syntax- 

#a)Read entire file- syntax- with open("notes.txt","r")as f:
#                               data = f.read()
#                               print(data)
with open("newTextfiles.txt","r")as f:
    data=f.read()
    print(data)

#b)Read line by line- syntax= with open("notes.txt","r")as f:
#                               line = f.readline()
#                               print(data)

with open("newTextfiles.txt","r")as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    line4=f.readline()
    print("line1:",line1)
    print("line2:",line2)
    print("line3:",line3)
    print("line4:",line4)






    
