file = open("G:\\test.txt",'w')
file.write("This is working,pyhton file handling exercise")
file.close()

file = open("G:\\test.txt",'r')
content = file.read()
print(content)
file.close()
