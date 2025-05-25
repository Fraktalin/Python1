class GroupLimitError(Exception):
    """Помилка: забагато студентів"""
    pass


class Person:
    def __init__(self, gender: str, age: int, name: str, surname: str):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}, {self.gender}, вік: {self.age}"


class Student(Person):
    def __init__(self, gender: str, age: int, name: str, surname: str, student_id: str):
        super().__init__(gender, age, name, surname)
        self.student_id = student_id

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, ID: {self.student_id}, {self.gender}, вік: {self.age}"


class Group:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) >= 10:
            raise GroupLimitError(f"Група '{self.group_name}' вже має 10 студентів.")
        self.students.append(student)

    def find_student(self, surname: str) -> Student | None:
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def delete_student(self, surname: str):
        student = self.find_student(surname)
        if student:
            self.students.remove(student)

    def __str__(self):
        if not self.students:
            return f"Група {self.group_name} порожня"
        students_list = '\n'.join(str(s) for s in self.students)
        return f"Група {self.group_name}:\n{students_list}"


gr = Group('PD1')
try:
    for i in range(11):
        gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'ID{i}'))
except GroupLimitError as e:
    print("Помилка:", e)

assert str(gr.find_student('Surname0')) == str(gr.students[0]), 'Test find'
gr.delete_student('Surname0')
assert gr.find_student('Surname0') is None, 'Test delete'
