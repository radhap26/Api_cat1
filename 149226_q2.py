class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}
    
    def add_assignment_grade(self, assignment_name, grade):
        """Add an assignment and grade to the student's record"""
        if 0 <= grade <= 100:
            self.assignments[assignment_name] = grade
            print(f"Grade {grade} added for assignment '{assignment_name}' for {self.name}")
        else:
            print("Invalid grade. Grade must be between 0 and 100.")
    
    def display_grades(self):
        """Display all grades for the student"""
        if not self.assignments:
            print(f"No assignments recorded for {self.name}")
            return
        
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        print("-" * 40)
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}%")
        
        # Calculate average
        average = sum(self.assignments.values()) / len(self.assignments)
        print(f"Average: {average:.2f}%")
        print("-" * 40)


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):
        """Add a student to the course"""
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} added to {self.course_name}")
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}")
    
    def assign_grade(self, student_id, assignment_name, grade):
        """Assign a grade to a specific student"""
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment_grade(assignment_name, grade)
                return
        print(f"Student with ID {student_id} not found in {self.course_name}")
    
    def display_all_students_grades(self):
        """Display all students and their grades"""
        if not self.students:
            print(f"No students enrolled in {self.course_name}")
            return
        
        print(f"\n=== {self.course_name} - Instructor: {self.name} ===")
        print("=" * 50)
        
        for student in self.students:
            student.display_grades()
            print()


def interactive_course_management():
    """Interactive function to manage the course"""
    print("=== Online Course Management System ===")
    
    # Get instructor information
    instructor_name = input("Enter instructor name: ")
    course_name = input("Enter course name: ")
    
    instructor = Instructor(instructor_name, course_name)
    
    while True:
        print()
        print("Course Management Menu:")
        print("1. Add a new student")
        print("2. Assign a grade to a student")
        print("3. Display all students and grades")
        print("4. Display grades for a specific student")
        print("5. Exit")
        print()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Add a new student
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            
            # Check if student ID already exists
            existing_student = None
            for student in instructor.students:
                if student.student_id == student_id:
                    existing_student = student
                    break
            
            if existing_student:
                print(f"Student with ID {student_id} already exists!")
            else:
                new_student = Student(student_name, student_id)
                instructor.add_student(new_student)
        
        elif choice == "2":
            # Assign a grade
            if not instructor.students:
                print("No students enrolled. Please add students first.")
                continue
            
            print("\nAvailable students:")
            for i, student in enumerate(instructor.students, 1):
                print(f"{i}. {student.name} (ID: {student.student_id})")
            
            try:
                student_index = int(input("Select student (enter number): ")) - 1
                if 0 <= student_index < len(instructor.students):
                    selected_student = instructor.students[student_index]
                    assignment_name = input("Enter assignment name: ")
                    
                    while True:
                        try:
                            grade = float(input("Enter grade (0-100): "))
                            if 0 <= grade <= 100:
                                break
                            else:
                                print("Grade must be between 0 and 100.")
                        except ValueError:
                            print("Please enter a valid number.")
                    
                    instructor.assign_grade(selected_student.student_id, assignment_name, grade)
                else:
                    print("Invalid student selection.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            # Display all students and grades
            instructor.display_all_students_grades()
        
        elif choice == "4":
            # Display grades for a specific student
            if not instructor.students:
                print("No students enrolled.")
                continue
            
            print("\nAvailable students:")
            for i, student in enumerate(instructor.students, 1):
                print(f"{i}. {student.name} (ID: {student.student_id})")
            
            try:
                student_index = int(input("Select student (enter number): ")) - 1
                if 0 <= student_index < len(instructor.students):
                    instructor.students[student_index].display_grades()
                else:
                    print("Invalid student selection.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "5":
            print("Thank you for using the Course Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the interactive system
if __name__ == "__main__":
    interactive_course_management()

   