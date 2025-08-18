# Classes and objects
# We have objects in coding that are taken from real life, like in real life we have objects all around us and every object has its own properties
# and functionalities. Objects are taken from the real world so that they will also have some properties and functionalities

# Example : we need to create a game where we need to create a player and we need to give two things to the player: properties, the way
# the player looks and functionalities. If we create a player with the help of the objects then we can give both the two things, properties
# and functionalities.
# Classes 
# Classes are the blueprints or the designs which are created before the object. For example, if in real life there is a laptop object which
# was actually designed and developed by the company where the company before creating the laptop object the company creates a blueprint of the
# laptop. Blueprint is the design where it gives how it should look like. Once the blueprint is okay, then the company starts creating the objects
# In real life before the object is created, their designing is done.
# Designing in coding is called as class, first class is created and then the object is created. In coding class, the class which is in coding 
# here we give all the properties and the functionalities. Class is like a group where we put all the functions together.
# syntax for creating class : 

#class Classname :
#synax to create object : objectname = classname()

#Rxample 1 : create class student with attributes/properties name, email, address, class. create one functions make where we calculate score
class Student : # init function is that where we give all properties variables it is used only tocreate variables.
#here shape,size, coloor other differenr properties are given
    def __init__(self, name, email, address, grade):#alays self keyword is used to define variables infunction
      self.name=name 
      self.email=email
      self.address=address
      self.grade=grade
    #for functionality we create seperate functions.
    def marks(self):
          score = int(input("Enter your English marks."))
          maths = int(input("Enter your maths score"))
          science = int(input("Enter your science score."))
          total = science+maths+score
          print(total)

Student1=Student("John", "John@icloud.com", "India", 74)
Student1.marks()
# Calling function of class - objectname.functionname()
# syntax to print the values - objectname.variablename()
print(Student1.name,Student1.email,Student1.address,Student1.grade)