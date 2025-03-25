lst1=[]
lst2=[]
lst3=[]
z1=int(input('enter the range for 1:'))
for x in range(z1):
    x=int(input('enter numbers 1:'))
    lst1.append(x)
z2=int(input('enter the range for 2:'))
for y in range(z2):
    y=int(input('enter numbers 2:'))
    lst2.append(y)
print(lst1,lst2)

#if length of sum is same
if (len(lst1)==len(lst2)):
    print('same length')
else:
    print('not same length')

#check if sum is same
if (sum(lst1)==sum(lst2)):
    print('same sum')
else:
    print('not same sum')

#finding common element in list
for x in lst1: 
    if x in lst2:
        lst3.append(x)
print(lst3)
