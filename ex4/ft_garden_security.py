class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, h):
        if h >= 0:
            self.__height = h
            print(f"Height updated: {h}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, a):
        if a >= 0:
            self.__age = a
            print(f"Age updated: {a} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {a} days [REJECTED]")
            print("Security: Negative age rejected\n")


if __name__ == "__main__":
    h = 15
    a = 3
    plant = SecurePlant("Rose")
    if h > 0 and a > 0:
        print(f"Plant created: {plant.name}")
        plant.set_height(h)
        plant.set_age(a)
        print(
            "\nCurrent plant:" + plant.name +
            f"({plant.get_height()}cm, {plant.get_age()} days)"
        )
    else:
        if h <= 0 and a <= 0:
            plant.set_height(h)
            plant.set_age(a)
        elif h <= 0:
            plant.set_height(h)
        elif a <= 0:
            plant.set_age(a)
