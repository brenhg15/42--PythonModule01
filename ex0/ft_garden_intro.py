def ft_garden_intro(name: str, height: int, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    name = "Rose"
    height = 25
    age = 30
    ft_garden_intro(name, height, age)
    print(" ")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
