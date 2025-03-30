#find and replace
f=input('Find:')
r=input('Replace:')

fr=open('hello.txt','r')
y=fr.read()
fr=open('hello.txt','w')
y=y.replace(f,r)
fr.write(y)
fr.close()
fr.close()