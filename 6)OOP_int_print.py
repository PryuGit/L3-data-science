class Student:
    #instantiate object
    def __init__(self,id,name,address,admission,level,section):
        self.id=id
        self.name=name
        self.address=address
        self.admission=admission
        self.level=level
        self.section=section
    #display objects
    def display(self):
        print('ID:',self.id)
        print('Name:',self.name)
        print('Address:',self.address)
        print('Admission:',self.admission)
        print('Level:',self.level)
        print('Section:',self.section)


id=int(input('Enter ID:'))
name=input('Enter name:')
address=input('Enter address:')
admission=input('Enter admission:')
level=int(input('Enter level:'))
section=input('Enter section:')
st=Student(id,name,address,admission,level,section)
st.display()