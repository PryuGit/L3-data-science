#check if the number is armstrong
def arm(n):
    a=n
    b=n
    s=0
    count=0
    while b!=0:
        count+=1
        b//=10
    while n!=0:
        r=n%10
        s+=r**count
        n//=10
    if a==s:
        print('armstrong')
    else:
        print('not armstrong')
n=int(input('Enter a number:'))
arm(n)