class Plant:
    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = round(height, 1)
        self.age = age
        self.start_height = round(height, 1)

    def create_print_plant(self: "Plant") -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def print_plant(self: "Plant") -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow_one_day(self: "Plant") -> None:
        self.age += 1
        if self.name.capitalize() == "Rose":
            self.height = round(self.height + 0.8, 1)
        elif self.name.capitalize() == "Sunflower":
            self.height = round(self.height + 0.7, 1)
        elif self.name.capitalize() == "Cactus":
            self.height = round(self.height + 0.4, 1)
        else:
            self.height = round(self.height * 1.05, 1)

    def weekly_growth(self: "Plant") -> None:
        total_growth = round(self.height - self.start_height, 1)
        print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    plant_1 = Plant("rose", 25.0, 30)
    plant_2 = Plant("oak", 200.0, 365)
    plant_3 = Plant("cactus", 5.0, 90)
    plant_4 = Plant("sunflower", 80.0, 45)
    plant_5 = Plant("cactus", 15.0, 120)
    print("=== Plant Factory Output ===")
    plant_1.create_print_plant()
    plant_2.create_print_plant()
    plant_3.create_print_plant()
    plant_4.create_print_plant()
    plant_5.create_print_plant()
