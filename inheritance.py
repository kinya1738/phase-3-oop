class Pet:
    def speak(self):
        print("pet is speaking")


class Dog(Pet):
    def speak(self):
        super().speak()
        print("Dog is speaking")

class Cat(Pet):
    pass

dog1 = Dog()
dog1.speak()
