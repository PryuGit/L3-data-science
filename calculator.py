#Calculator
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    d=a-b
    return d
def mul(a,b):
    e=a*b
    return e
def div(a,b):
    f=a/b
    return f
def trun(a,b):
    g=a//b
    return g
def mod(a,b):
    h=a%b
    return h  
def exo(a,b):
    i=a**b
    return i
a=float(input('enter a first number:'))
b=float(input('enter a second number:'))
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(trun(a,b))
print(mod(a,b))
print(exo(a,b))