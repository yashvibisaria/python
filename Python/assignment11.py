class employee : 
    def __init__(self, name, age, iddetails, salary, position, bonus, timings):
      self.name=name
      self.age=age
      self.iddetails=iddetails
      self.salary=salary
      self.position=position
      self.bonus=bonus
      self.timings=timings

    def increase(self):
          a = int(input("Enter how many pounds you want your salary to increase"))
          print(a)
          b = self.salary+a
          print("Your new salary is", b,".")
    def promotion(self):
        c = input("Do you want to be promoted from being a salesman?")
        print(c)
        if c=="yes":
            self.position="manager"
            print("Your new position is", self.position)
        else:
            print("You will remain a salesman.")
    def time(self):
        d = int(input("Enter the time you arrived."))
        print(d)
        in_time=9
        if d<=in_time:
            print("You're on time.")
        else:
            print("You're late.")
    

employee1=employee("John", "25", "122012", "£1200", "salesman", "___", "9 to 5")
print(employee1.name, employee1.age, employee1.iddetails, employee1.salary, employee1.position, employee1.bonus, employee1.timings)
employee1.increase()
employee1.promotion()
employee1.time()