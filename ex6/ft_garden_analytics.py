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
        total_growth = 0
        for plant in self.plants:
            before = plant.height
            plant.grow()
            total_growth += plant.height - before
        return total_growth

    @classmethod
    def create_garden_network(cls):
        return cls("NetworkGarden")

    @staticmethod
    def validate_height(height):
        return height > 0

    class GardenStats:
        def gardens_plants(self, plants):
            print("Plants in garden:")
            for plant in plants:
                print(f"- {plant.name}: {plant.height}cm", end="")
                if plant.types == 'FloweringPlant':
                    print(f", {plant.color} flowers", end="")
                    if plant.age > 20:
                        print(" (blooming)")
                    else:
                        print()
                elif plant.types == 'PrizeFlower':
                    print(f", {plant.color} flowers", end="")
                    if plant.age > 20:
                        print(" (blooming)", end="")
                    if plant.points > 0:
                        print(f", Prize points: {plant.points}", end="")
                elif plant.types == 'Plant':
                    print()
            print()

        def count_plants(self, plants, total_growth):
            num = 0
            pl = 0
            f = 0
            pr = 0
            for plant in plants:
                num += 1
            print(f"\nPlant added: {num}, total growth: {total_growth}cm")
            for plant in plants:
                if plant.types == 'Plant':
                    pl += 1
                elif plant.types == 'FloweringPlant':
                    f += 1
                elif plant.types == 'PrizeFlower':
                    pr += 1
            print(
                f"Plant types: {pl} regular, {f} flowering," +
                f" {pr} prize flowers"
            )

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
    def __init__(self, name, height, age, points, types):
        self.name = name
        self.__height = height
        self.age = age
        self.__points = 0
        self.types = 'Plant'

    def grow(self):
        self.__height += 1
        print(self.name, "grew 1cm")
        return self.height


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, points, types):
        super().__init__(name, height, age, points, types)
        self.color = color
        self.__points = 0
        self.types = 'FloweringPlant'


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, points, types):
        super().__init__(name, height, age, color, points, types)
        self.__points = points
        self.types = 'PrizeFlower'


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    network = GardenManager.create_garden_network()
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak", 250, 1850, 0, '')
    rose = FloweringPlant("Rose", 25, 15, "Red", 0, '')
    sunflower = PrizeFlower("Sunflower", 35, 40, "Yellow", 10, '')
    bob_oak = Plant("Oak", 75, 1850, 0, '')
    bob_rose = FloweringPlant("Rose", 15, 10, "Red", 0, '')
    bob_sunflower = PrizeFlower("Sunflower", 35, 40, "Yellow", 10, '')

    alice_garden.add_plant(oak)
    print("Added Oak Tree to Alice's garden")
    alice_garden.add_plant(rose)
    print("Added Rose Flower to Alice's garden")
    alice_garden.add_plant(sunflower)
    print("Added Sunflower to Alice's garden\n")
    bob_garden.add_plant(bob_oak)
    bob_garden.add_plant(bob_rose)
    bob_garden.add_plant(bob_sunflower)

    total_growth = alice_garden.grow_plants()

    print("\n=== Alice's Garden Report ===")
    stats = GardenManager.GardenStats()
    stats.gardens_plants(alice_garden.plants)
    stats.count_plants(alice_garden.plants, total_growth)
    print("\nHeight validation test:", GardenManager.validate_height(100))

    stats = GardenManager.GardenStats()
    alice_score = stats.calculate_score(alice_garden.plants)
    bob_score = stats.calculate_score(bob_garden.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    stats = GardenManager.GardenStats()
    stats.calculate_stats(GardenManager.all_gardens)
