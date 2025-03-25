#display list of numbers between 1-100
lst=[]
n=int(input('enter range:'))
x=0
for x in range(n):
    y=int(input('enter number for list:'))
    if 1<y<100:
        lst.append(y)
print(lst)
