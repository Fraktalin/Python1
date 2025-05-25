class Person:
    def __init__(self, gender: str, age: int, name: str, surname: str):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, {self.gender}, вік: {self.age}"
