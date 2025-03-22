#calculate the euclidean distance 
x1=float(input("Enter the coordinates of the first point(x1):"))
y1=float(input("Enter the coordinates of the first point(y1):"))
x2=float(input("Enter the coordinates of the second point(x2):"))
y2=float(input("Enter the coordinates of the second point(y2):"))
d=((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f"The Euclidean distance between the points is {d:.2f}")
