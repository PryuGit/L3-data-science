#Count Lowercase and Uppercase
def func(name):
    count=0
    for x in name:
        if x.isupper():
            count+=1
    lower=len(name)-count
    print('Uppercase:', count)
    print('Lowercase:', lower)

n=input("enter a string:")
func(n)