#write code to opened file named file.txt read mode

file= open("file.txt","r")
data=file.read()
print("my data in this file is:",data)
file.close()

#write a program to read a text from given file certificate.txt and find weather it contains a world "live".(read mode)

file= open("certificate.txt","r")
dataOffFile=file.read()
dataOffFile=dataOffFile.lower()
if "live" in dataOffFile:
      print("yes the live word is present in this file")
else:
      print("no")
file.close()


#open a file called report.txt in "write mode"
#if file is not exist then using write mode to creste a file
#in this report1 file is not created seperately.

file=open("report1.txt","w")
file.write("hi!i am prachi more")
file.close()

#append mode

file=open("report1.txt","a")
file.write("hi!i am prachi more")
file.close()

