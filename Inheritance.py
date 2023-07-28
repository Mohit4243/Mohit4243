class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def make_sound(self):
        print(f"{self.name} says Meow")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def make_sound(self):
        print(f"{self.name} says Woof")


# Example usage:
if __name__ == "__main__":
    cat1 = Cat("Silly")
    dog1 = Dog("Tomy")

    cat1.make_sound()  # Output: Fluffy says Meow
    dog1.make_sound()  # Output: Buddy says Woof
