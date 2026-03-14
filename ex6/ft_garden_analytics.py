class GardenManager:
    all_gardens = []

    def __init__(self, owner):
        self.owner = owner
        self.owners = []
        self.plants = []
        GardenManager.all_gardens.append(self)

    def add_plant(self, plant):
        self.plants.append(plant)

    def count_owner(self, owner):
        self.owners.append(owner)

    def grow_plants(self):
        print(self.owner, "is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    @classmethod
    def create_garden_network(cls):
        return cls("NetworkGarden")

    @staticmethod
    def validate_height(height):
        return height > 0


    class GardenStats:
        @staticmethod
        def gardens_plants(plants):
            print("Plants in garden:")
            for plant in plants:
                print(f"- {plant.name}: {plant.height}cm")


        def calculate_score(self, plants):
            score = 0
            for plant in plants:
                score += plant.height
                score += plant.points
            return score

        def calculate_stats(self, owners):
            num = 0
            for owner in owners:
                num += 1
            print("Total gardens managed:", num)


class Plant:
    def __init__(self, name, height, age, points):
        self.name = name
        self.height = height
        self.age = age
        self.points = 0

    def grow(self):
        self.height += 1
        print(self.name, "grew 1cm")



class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, points):
        super().__init__(name, height, age, points)
        self.color = color
        self.points = 0


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, points):
        super().__init__(name, height, age, color, points)
        self.points = points


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak", 250, 1850, 0)
    rose = FloweringPlant("Rose", 25, 10, "Red", 0)
    sunflower = PrizeFlower("Sunflower", 35, 40, "Yellow", 10)
    bob_oak = Plant("Oak", 75, 1850, 0)
    bob_rose = FloweringPlant("Rose", 15, 10, "Red", 0)
    bob_sunflower = PrizeFlower("Sunflower", 35, 40, "Yellow", 10)

    alice_garden.add_plant(oak)
    print("Added Oak Tree to Alice's garden")
    alice_garden.add_plant(rose)
    print("Added Rose Flower to Alice's garden")
    alice_garden.add_plant(sunflower)
    print("Added Sunflower to Alice's garden\n")
    bob_garden.add_plant(bob_oak)
    bob_garden.add_plant(bob_rose)
    bob_garden.add_plant(bob_sunflower)

    alice_garden.grow_plants()

    print("\n=== Alice's Garden Report ===")
    GardenManager.GardenStats.gardens_plants(alice_garden.plants)
    print("\nHeight validation test:", GardenManager.validate_height(100))

    stats = GardenManager.GardenStats()
    alice_score = stats.calculate_score(alice_garden.plants)
    bob_score = stats.calculate_score(bob_garden.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    stats = GardenManager.GardenStats()
    stats.calculate_stats(GardenManager.all_gardens)