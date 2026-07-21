class Plant:
    def __init__(self, plant_name, plant_height, plant_age):
        self.name = plant_name
        self.height = plant_height
        self.age = plant_age
    
    def print_plant(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    plant_1.print_plant()
    plant_2.print_plant()
    plant_3.print_plant()
