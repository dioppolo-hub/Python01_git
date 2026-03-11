class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_garden_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 10, 30)
cactus = Plant("Cactus", 100, 120)
sunflower = Plant("Sunflower", 80, 45)

plants = [rose, cactus, sunflower]

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for i in range(3):
        plants[i].ft_garden_data()
