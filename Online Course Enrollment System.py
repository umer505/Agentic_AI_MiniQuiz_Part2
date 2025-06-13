courses = {
    "ai": {"seats": int, "students": ["ali", "ahmed", "sara", "umer"]},
    "ml": {"seats": int, "students": ["haroon", "arshad", "sehar", "umer"]},
    "ds": {"seats": int, "students": ["ali", "ahmed", "sara", "umer", "haroon"]},
    "webdev": {"seats": int, "students": ["ali", "ahmed", "sara", "umer", "haroon", "arshad"]},
    "db": {"seats": int, "students": ["ali", "ahmed", "sara"]},
    "python": {"seats": int, "students": ["ali", "ahmed", "sara", "umer", "haroon", "arshad", "sehar"]},
    "Java": {"seats": int, "students": ["ali", "ahmed", "sara", "umer", "haroon", "arshad", "sehar"]},
    "C++": {"seats": int, "students": ["ali", "ahmed", "sara", "umer", "haroon", "arshad", "sehar"]},

}

def enroll_student(course_name, student_name):
    if course_name in courses:
        if student_name not in courses[course_name]["students"]:
            courses[course_name]["students"].append(student_name)
            print(f"{student_name} has been enrolled in {course_name}.")
        else:
            print(f"{student_name} is already enrolled in {course_name}.")
    else:
        print(f"Course {course_name} does not exist.")

def display_courses():
    print("Available courses:")
    for course, details in courses.items():
        print(f"{course}: {len(details['students'])} students enrolled, {details['seats']} seats available")

def main():
    while True:
        print("\nOnline Course Enrollment System")
        print("1. Display available courses")
        print("2. Enroll a student")
        print("3. Drop course")
        print("4. View enrolled students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_courses()
        
        elif choice == "2":
            course_name = input("Enter course name: ")
            student_name = input("Enter student name: ")
            enroll_student(course_name, student_name)
        
        elif choice == "3":
            course_name = input("Enter course name: ")
            student_name = input("Enter student name: ")
            if course_name in courses and student_name in courses[course_name]["students"]:
                courses[course_name]["students"].remove(student_name)
                print(f"{student_name} has been dropped from {course_name}.")
            else:
                print(f"{student_name} is not enrolled in {course_name} or the course does not exist.")
        
        elif choice == "4":
            course_name = input("Enter course name: ")
            if course_name in courses:
                print(f"Students enrolled in {course_name}: {', '.join(courses[course_name]['students'])}")
            else:
                print(f"Course {course_name} does not exist.")
        
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()