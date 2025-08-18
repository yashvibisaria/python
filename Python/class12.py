# Inheritance
# Generally, inheritance means when children takes something from parents. Lets say we have a class where we need to create functions which are
# already created in a different class. One option is that you can create those functions again in a new class which will make our code bigger
# plus, it will waste our time. Second option is we use those functions from the previous class rather than creating a new one. To do this, 
# Two classes need to have a relationship, and that relationship we give is of a parent and child. The class which takes the function will 
# be called as the child class and the class that gives the function is called as the parent class. After this, once you tell that this is the
# parent and child class, than child class can take anything from the parent class.
# Advtanges of inheritance
# 1. Makes the code shorter as we don't have to create the same functions again and class can use the previous ones.
# 2. Saves time  

#----------------------------to connect child class with parent class-----------------------
# class childclass(parentclassname):
#write the name of first class in second class () to connect

#-----------------------call variables and function in second class or use it second class----------
#variables call or using first class variable in second class: inside init of second class we first class init
#eg : parentclassname.__init__(self, name, class1)
#these  two varoables will go to second class

#call function or transfer function in secon dclass
#parentclassname.functioname()

#--------------------------------objects------------------------------------------
#objects are always created of child class as child class has taken variables and functions from parent class and along wit that
# it has its own data too.

#-----------------------------createing obejcts and calling function-------------------------------
#objectame=classname(value1, value2......)
#objectname.functioname()

# parent class

class student:
    def __init__(self, name, class1):
        self.name=name
        self.class1=class1
    #marks function
    def marks():
        a=int(input("Enter marks of subject a"))
        b=int(input("Enter marks of subject b"))
        result=(a+b)/2
        print(result)
    def message(self):
        #call the function 
        print("I love coding")



#child class
class teacher(student): 
    def __init__(self, salary, name, class1):
        self.salary=salary
        #to transfer variables from first class to second class do as following
        student.__init__(self, name, class1)  # now name, class1 has come to second class 
    
    def average(self):
        #trasfer or call function from parent class 
        student.marks()

    def message(self):
        student.message(self)
        print("this is good")

teacher1=teacher(1233, "John", 12)
teacher1.average()
teacher1.message()

#--------------------------------Polymorphism---------------------------------------------------
#whne two functions share same name in parent class and one in child class which means one functions in parent and one in child have same name.
#code inside that will be different. We will call function in child class.
