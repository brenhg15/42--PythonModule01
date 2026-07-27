#!/usr/bin/env python3


class Plant:
    """Encapsulated Plant class validating height and age inputs."""

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.name}: {rose.get_height():.1f}cm, "
          f"{rose.get_age()} days old")

    rose.set_height(25.0)
    print("Height updated: 25cm")

    rose.set_age(30)
    print("Age updated: 30 days")

    # Intentos con valores inválidos
    rose.set_height(-5.0)
    rose.set_age(-10)

    print(f"Current state: {rose.name}: {rose.get_height():.1f}cm, "
          f"{rose.get_age()} days old")


if __name__ == "__main__":
    main()