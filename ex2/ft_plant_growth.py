class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_garden_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


h_rose = 10
tmp1 = h_rose
a_rose = 30
h_cactus = 100
tmp2 = h_cactus
a_cactus = 120
h_sunflower = 110
tmp3 = h_sunflower
a_sunflower = 45

rose = Plant("Rose", h_rose, a_rose)
cactus = Plant("Cactus", h_cactus, a_cactus)
sunflower = Plant("Sunflower", h_sunflower, a_sunflower)

plants = [rose, cactus, sunflower]
tmp = [tmp1, tmp2, tmp3]

if __name__ == "__main__":
    print("== Day 1 ===")
    for i in range(3):
        plants[i].ft_garden_data()

    print("== Day 7 ===")
    for i in range(7):
        h_rose = h_rose + 1
        h_cactus = h_cactus + 3
        h_sunflower = h_sunflower + 2

    a_rose = a_rose + 6
    a_cactus = a_cactus + 6
    a_sunflower = a_sunflower + 6

    rose = Plant("Rose", h_rose, a_rose)
    cactus = Plant("Cactus", h_cactus, a_cactus)
    sunflower = Plant("Sunflower", h_sunflower, a_sunflower)

    plants = [rose, cactus, sunflower]
    new_heights = [h_rose, h_cactus, h_sunflower]

    for i in range(3):
        plants[i].ft_garden_data()
        print(f"Growth this week: +{new_heights[i] - tmp[i]}cm")
