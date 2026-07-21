class Plant:
    def __init__(self, plant_name, plant_height, plant_age):
        self.name = plant_name
        self.height = plant_height
        self.age = plant_age
        self.start_height = plant_height
    
    def print_plant(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    
    def grow_one_day(self):
        self.height = round(self.height * 1.05, 1)
        self.age += 1

    def weekly_growth(self):
        total_growth = round(self.height - self.start_height, 1)
        print(f"Growth this week: {total_growth}cm")

if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    plant_1.print_plant()
    for x in range (1, 8):
        print(f"=== Day {x} ===")
        plant_1.grow_one_day()
        plant_1.print_plant()
    plant_1.weekly_growth()
