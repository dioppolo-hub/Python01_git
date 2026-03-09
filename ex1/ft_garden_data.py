class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def ft_garden_data(self):
    print ("=== Garden Plant Registry ===")
    return f"{self.name}:", {self.height}cm, {self.age} days old"


rose = Plant("Rose", 10, 30)
cactus = Plant("Cactus", 100, 120)
sunflower = Plant("Sunslower", 80, 45)
print(rose.ft_garden_data())
print(cactus.ft_garden_data())
print(sunflower.ft_garden_data())
