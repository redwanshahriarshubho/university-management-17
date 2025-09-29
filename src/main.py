from services import UniversitySystem
from tabulate import tabulate

def display_menu():
    print("\n=== University Management System ===")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Assign Grade")
    print("5. View Student Courses")
    print("6. View Course Roster")
    print("7. Exit")

def main():
    uni = UniversitySystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Student name: ")
            email = input("Email: ")
            major = input("Major: ")
            student_id = uni.add_student(name, email, major)
            print(f"Student added with ID: {student_id}")
            
        elif choice == "2":
            title = input("Course title: ")
            instructor = input("Instructor: ")
            capacity = int(input("Capacity: "))
            course_id = uni.add_course(title, instructor, capacity)
            print(f"Course added with ID: {course_id}")
            
        elif choice == "3":
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            if uni.enroll_student(student_id, course_id):
                print("Enrollment successful!")
            else:
                print("Enrollment failed (invalid IDs or full course)")
                
        elif choice == "4":
            enrollment_id = input("Enrollment ID: ")
            grade = input("Grade: ")
            if uni.assign_grade(enrollment_id, grade):
                print("Grade assigned successfully!")
            else:
                print("Invalid enrollment ID")
                
        elif choice == "5":
            student_id = input("Student ID: ")
            courses = uni.get_student_courses(student_id)
            if courses:
                headers = ["Course ID", "Title", "Instructor"]
                data = [[c.course_id, c.title, c.instructor] for c in courses]
                print(tabulate(data, headers=headers))
            else:
                print("No courses found or invalid student ID")
                
        elif choice == "6":
            course_id = input("Course ID: ")
            students = uni.get_course_students(course_id)
            if students:
                headers = ["Student ID", "Name", "Email", "Major"]
                data = [[s.student_id, s.name, s.email, s.major] for s in students]
                print(tabulate(data, headers=headers))
            else:
                print("No students found or invalid course ID")
                
        elif choice == "7":
            print("Exiting system...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()