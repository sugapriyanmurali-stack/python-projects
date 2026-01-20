class Student:
    def __init__(self,name,rollno,status):
        self.name=name
        self.rollNo=rollno
        self.status=status
    def details(self):
        print(self.name,"have",self.status)

S1=Student("Mike",12,"Pass")
S2=Student("Will",13,"Pass")
S3=Student("Max",14,"Fail")
S1.details()
S2.details()
S3.details()