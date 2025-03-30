#count the occurence of the word
count={}
fr=open('hello.txt','r')
x=fr.read().lower()
for i in x.split():
    count[i]=count.get(i,0)+1
fr.close()

for i,c in count.items():
    print(f"'{i}':{c}")