class Student:
    def __init__(self, student_id, name, email, major):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.courses = []

class Course:
    def __init__(self, course_id, title, instructor, capacity):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled = []

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id
        self.grade = None