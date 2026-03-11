class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 2

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


h_rose = 10
h_cactus = 100
h_sunflower = 110
a_rose = 30
a_cactus = 120
a_sunflower = 45
tmp1 = h_rose
tmp2 = h_cactus
tmp3 = h_sunflower

rose = Plant("Rose", h_rose, a_rose)
cactus = Plant("Cactus", h_cactus, a_cactus)
sunflower = Plant("Sunflower", h_sunflower, a_sunflower)

plants = [rose, cactus, sunflower]
tmp = [tmp1, tmp2, tmp3]

if __name__ == "__main__":
    print("== Day 1 ===")
    for i in range(3):
        plants[i].get_info()

    print("== Day 7 ===")
    for i in range(6):
        for plant in plants:
            plant.grow()
            plant.age_one_day()

    h_rose = rose.height
    h_cactus = cactus.height
    h_sunflower = sunflower.height
    new_height = [h_rose, h_cactus, h_sunflower]
    for i in range(3):
        plants[i].get_info()
        print(f"Growth this week: +{new_height[i] - tmp[i]}cm")
