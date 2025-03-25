#Check if the number is prime or not
def func(prime):
    if prime<=1:
        print('Composite')
        return
    for x in range(2,prime):
        if prime%x==0:
            print("Composite")
            return
    else:
        print("prime")    
n=int(input("enter a number:"))
func(n)    