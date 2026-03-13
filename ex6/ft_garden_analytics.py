class GardenManager:
    def __init__(self, owner):
        self.owner = owner


    class GardenStats(GardenManager):
        def __init__(self)


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flowering_Plant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def blooming(self):
        if self.age > 20:
            print("(blooming)")
        else:
            print("(Not ready for blooming)")


class Prize_Flower(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)