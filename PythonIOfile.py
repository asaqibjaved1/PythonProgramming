# # # Python file Input/Output 
# a = open("textfile.txt", "r")
# data = a.read()
# print(data)
# a.close()

# a = open("textfile.txt", "r")
# data = a.read(12) #reading first 12 character of file
# print(data)
# a.close()

# a = open("textfile.txt", "r")
# line = a.readline() #reading the file line by line
# print(line)
# a.close()

# a = open("textfile.txt", "r")
# line2 = a.read()
# print(line2)
# a.close()

# # Python Writing(Over writing) in a file
# b = open("textfile.txt", "w")
# data = b.write("I am Amir and i am learning web development")
# b.close()

# # Python Appending the file 
# b = open("textfile.txt", "a")
# data = b.write("\nI am Ehtisham and i am learning AI")
# b.close()

# deleting any file through python code 
import os #import os modeule in which remove function is saved

os.remove("sample.txt")

