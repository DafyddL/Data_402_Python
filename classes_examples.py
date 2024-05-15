class Animal:
    aquatic = False
    terrestrial = True

    def __init__(self, name, animal_type, animal_noise, age):
        self.name = name
        self.animal_type = animal_type
        self.animal_noise = animal_noise
        self.age = age

    def speak(self):
        print(" ".join([self.animal_noise for i in range(3)]))

    def walk(self):
        if not self.terrestrial:
            print("This animal cannot walk on land")
        else:
            pass


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "dog", "woof", age)
        self.breed = breed

    def fetch(self):
        print("Fetched")

    def play(self):
        print("Dog is happy")


class Fish(Animal):

    def __init__(self, name, age):
        super().__init__(name, "fish", "boop", age)
        self.terrestrial = False
        self.aquatic = True

    def play(self):
        print("How are you supposed to play with a fish? Stop trying to climb in the fish tank with it and have some respect for yourself.")


steve = Dog("Steve", 4, "Dalmation")
mike = Fish("Mike", 2)

