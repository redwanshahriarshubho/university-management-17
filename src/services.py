from .models import Student, Course, Enrollment
from .utils import generate_id

class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = {}

    def add_student(self, name, email, major):
        student_id = generate_id("STU")
        self.students[student_id] = Student(student_id, name, email, major)
        return student_id

    def add_course(self, title, instructor, capacity):
        course_id = generate_id("CRS")
        self.courses[course_id] = Course(course_id, title, instructor, capacity)
        return course_id

    def enroll_student(self, student_id, course_id):
        if student_id not in self.students or course_id not in self.courses:
            return False
        
        course = self.courses[course_id]
        if len(course.enrolled) >= course.capacity:
            return False
            
        enrollment_id = generate_id("ENR")
        self.enrollments[enrollment_id] = Enrollment(student_id, course_id)
        course.enrolled.append(student_id)
        self.students[student_id].courses.append(course_id)
        return enrollment_id

    def assign_grade(self, enrollment_id, grade):
        if enrollment_id in self.enrollments:
            self.enrollments[enrollment_id].grade = grade
            return True
        return False

    def get_student_courses(self, student_id):
        return [self.courses[cid] for cid in self.students[student_id].courses]

    def get_course_students(self, course_id):
        return [self.students[sid] for sid in self.courses[course_id].enrolled]