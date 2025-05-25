from student import Student

class GroupLimitError(Exception):
    """Помилка: забагато студентів"""
    pass

class Group:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students: list[Student] = []

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
