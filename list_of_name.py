#sort list
lst=[]
z=0
x=int(input('enter range of names:'))
for i in range(x):
    y=input('enter names:')
    lst.append(y)
for z in lst:
    lst.sort()
print(lst)
