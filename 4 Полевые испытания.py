def external_average_grade(self):
    all_grades = []
    for grades in self.grades.values():
        all_grades += grades
    result = round(sum(all_grades) / len(all_grades), 1)
    return result

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def give_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        return 'Ошибка'

    average_grade = external_average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self,other):
        if not isinstance(other, Student):
            print(f'{other} не является студентом')
            return
        return self.average_grade() < other.average_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    average_grade = external_average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

    def __lt__(self,other):
        if not isinstance(other, Lecturer):
            print(f'{other} не является лектором')
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name,surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


maruna = Student('Maruna', 'Bill', 'f')
kesha = Student('Kesha', 'Tim', 'f')
karl = Lecturer('Karl', 'Smith')
zola = Lecturer('Zola', 'Kent')
tonya = Reviewer('Tonya', 'Hash')
mike = Reviewer('Mike', 'Lemon')

maruna.add_courses('Git')

kesha.courses_in_progress.append('Python')
zola.courses_attached.append('Python')
kesha.give_grade(zola, 'Python', 10)

tonya.courses_attached.append('Python')
maruna.courses_in_progress.append('Python')
tonya.rate_hw(maruna, 'Python', 9)
tonya.rate_hw(maruna, 'Python', 10)
tonya.rate_hw(maruna, 'Python', 9)
tonya.rate_hw(kesha, 'Python', 9)
tonya.rate_hw(kesha, 'Python', 5)
tonya.rate_hw(kesha, 'Python', 7)

print(maruna)

print(kesha < maruna)
print(kesha > maruna)

karl.courses_attached.append('Python')
maruna.give_grade(karl, 'Python', 10)
maruna.give_grade(karl, 'Python', 9)
maruna.give_grade(karl, 'Python', 8)
print(karl)

print(zola < karl)
print(zola > karl)

print(mike)

def hw_average_grade(students_list, course):
    course_grades = []
    for student in students_list:
        course_grades += student.grades[course]
    average_course_grade = round(sum(course_grades) / len(course_grades), 1)
    return average_course_grade

students = [maruna, kesha]
print(hw_average_grade(students, 'Python'))

def lecture_average_grade(lecturers_list, course):
    lecture_grades = []
    for lecturer in lecturers_list:
        lecture_grades += lecturer.grades[course]
    average_lecture_grade = round(sum(lecture_grades) / len(lecture_grades), 1)
    return average_lecture_grade

lecturers = [karl, zola]
print(lecture_average_grade(lecturers, 'Python'))