class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        if self.age > 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not ready for blooming")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        shade = ((self.height * self.diameter) / 3.14) / 100
        print(f"{self.name} provides {shade:.0f} square meters of shades")


class Vegetable(Plant):
    def __init__(self, name, height, age, harv_season, nutr_value):
        super().__init__(name, height, age)
        self.harv_season = harv_season
        self.nutr_value = nutr_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 20, 30, "Red")
    print(
        f"\n{rose.name} (Flower): {rose.height}cm," +
        f"{rose.age} days, {rose.color} color"
    )
    rose.bloom()
    sunflower = Flower("Sunflower", 12, 15, "Yellow")
    print(
        f"\n{sunflower.name} (Flower): {sunflower.height}cm," +
        f"{sunflower.age} days, {sunflower.color} color"
    )
    sunflower.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(
        f"\n{oak.name} (Tree): {oak.height}cm," +
        f"{oak.age} days, {oak.diameter}cm diameter"
    )
    oak.produce_shade()
    pine = Tree("Pine", 1500, 2575, 120)
    print(
        f"\n{pine.name} (Tree): {pine.height}cm," +
        f"{pine.age} days, {pine.diameter}cm diameter"
    )
    pine.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(
        f"\n{tomato.name} (Vegetables): {tomato.height}cm," +
        f"{tomato.age} days, {tomato.harv_season} harvest"
    )
    print(f"{tomato.name} is rich in {tomato.nutr_value}")
    cucumber = Vegetable("Cucumber", 220, 120, "summer", "vitamin D")
    print(
        f"\n{cucumber.name} (Vegetables): {cucumber.height}cm," +
        f"{cucumber.age} days, {cucumber.harv_season} harvest"
    )
    print(f"{cucumber.name} is rich in {cucumber.nutr_value}")
