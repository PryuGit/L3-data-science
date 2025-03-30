#function for writing the file
def writefile(x):
    fw=open('world.txt','w')
    fw.write(x)
    fw.close()

#reading the contents from the file
fr=open('hello.txt','r')
x=fr.read()
writefile(x)
fr.close()
