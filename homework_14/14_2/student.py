from person import Person

class Student(Person):
    def __init__(self, gender: str, age: int, name: str, surname: str, student_id: str):
        super().__init__(gender, age, name, surname)
        self.student_id = student_id

    def __str__(self) -> str:
        return f"Студент: {self.name} {self.surname}, ID: {self.student_id}, {self.gender}, вік: {self.age}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)
