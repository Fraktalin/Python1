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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!