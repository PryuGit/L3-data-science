#numbers of 'a' in list
lst=[]
z=0
c=0
x=int(input('enter range of names:'))
for i in range(x):
    y=input('enter names:')
    lst.append(y)
for z in lst:
    count=z.lower().count('a')
    c+=count
print('the numbers of a in list:',c)