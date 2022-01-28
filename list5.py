class Person:
  def __init__(self, name, surname,age):
    self.name = name
    self.age = age
    self.surname=surname
    
    def birlestir(self):
      print(self.name+self.surname)
      
      p1 = Person("John", "Brown",36)
      p2= Person("Meltem","Yıldırım",45)
      p3=Person("Ahmet","Yıldız",30)
      
      print(p1.name,p2.age,p3.surname)
      # p1.name = "Ali"
      print(p1.name)
      print(p2.age)
      p3.birlestir()

