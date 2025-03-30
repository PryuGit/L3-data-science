#Employee Record Management System
import csv
import pandas as pd
class Employee:
    def __init__(self,empid,name,add,num,spo,child,sal):    
        self.empid=empid
        self.name=name
        self.add=add
        self.num=num
        self.spo=spo
        self.child=child
        self.sal=sal
    
    def append(self):
        fa=open('employees.csv','a',newline='')
        writer=csv.writer(fa)
        data=[self.empid,self.name,self.add,self.num,self.spo,self.child,self.sal]
        writer.writerow(data)
        fa.close()

fw=open('employees.csv','w',newline='')
title=["EmployeeID",'Name',"Address","Contact_Number","Spouse's_Name","Number_of_child","Salary"]
writer=csv.writer(fw)
writer.writerow(title)
fw.close()
    
n=int(input('enter the number of employees:'))
for i in range(n):
    empid=int(input('enter employee id:'))
    name=input('enter name:')
    add=input('enter address:')
    num=int(input('enter contact number:'))
    spo=input("enter spouse's name:")
    child=int(input('enter number of child:'))
    sal=int(input('enter salary:'))

    emp=Employee(empid,name,add,num,spo,child,sal)
    emp.append()

employ=pd.read_csv('employees.csv')
print('\nEmployee Records:')
print(employ)
    

