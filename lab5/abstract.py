from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name,):
    self.name = name


  @abstractmethod
  def make_sound(self):
    pass


class Dog(Animal):

  def make_sound(self):
    print(f"{self.name} каже: Гав")


class Cat(Animal):

  def make_sound(self):
    print(f"{self.name} каже: Мяу")





animals = [Dog("Шурік"), Cat("Батон")]

for animal in animals:
  animal.make_sound() 




# множинне наслідування 

# мро порядок в якому виконується наслідування

# абстрактний метод

# статичний метод

# супер
