class student:
    def __init__(self, passname, information):
        self.passname=passname
        self.information=information
    def marks():
        a=int(input("What is your score for Maths?"))
        b=int(input("What is your score for English?"))
        average=(a+b)/2
        print(average)

class workingstudent(student):
    def __init__(self, pass_salary, passname, information):
        self.pass_salary=pass_salary
        student.__init__(self, passname, information)
    def result(self):
        student.marks()

workingstudent1=workingstudent(1200, "John", "School name")
workingstudent1.result()
print(workingstudent1.passname, workingstudent1.information, workingstudent1.pass_salary)

#---------------------------Assignment----------------------------------
#Write a Python program to create a class representing a Circle with attributes length and width
#. Include methods/functions to calculate its area  and second function to calculate permiter.
#(3.14). take length and width input from user in both functions. create object and call both functions

class circle:
    def __init__(self, radius, diameter):
        self.radius=radius
        self.diameter=diameter
    def area(self):
        radius=int(input("What is the radius of your circle?"))
        print(radius)
        area=(radius*radius)*3.14
        print(area, "Is the area of your circle")
    def circumference(self):
        diameter=int(input("What is the diameter of the circle?"))
        print(diameter)
        circumference=diameter*3.14
        print(circumference,"is the circumference of your circle.")

circle1=circle(460, 920)
circle1.area()
circle1.circumference()