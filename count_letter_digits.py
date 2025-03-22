#Count digit and alphabet in string
s=input("Enter a string: ")
l=0
d=0
for char in s:
    if char.isalpha():  
        l+=1
    elif char.isdigit():
        d+=1
print(f"Number of letters:",l)
print(f"Number of digits:",d)
