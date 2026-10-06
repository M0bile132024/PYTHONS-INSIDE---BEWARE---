import time as t
class car_details:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"{self.brand},{self.color}"
    def listinmator(self):
        myit = iter(self.brand)
        for x in self.brand:
            print(next(myit))
            t.sleep(1)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x        
    
        
inputbrand = str(input("Car brand you use."))
inputcolor = str(input("Car color you use."))
Id = car_details(inputbrand, inputcolor)
print("PROCESSING...")
t.sleep(5)
print("Sucess!Your car Id has been logged in the database as:")
t.sleep(3)
print(Id)
t.sleep(3)
print("With your car brand being spelt as:")
t.sleep(3)
Id.listinmator()
input("Is that correct?")
print("""Well in case please wait for your
      car's extented warranty advisor to be
      avavible in aproximately:""")

myclass = MyNumbers()
myiter = iter(myclass)
i = 0
j = 1
while i != j:
    t.sleep(1)
    print(next(myiter))
    


