class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        """Display employee details"""
        print(f"Employee Details:")
        print(f"  Name: {self.name}")
        print(f"  ID: {self.employee_id}")
        print(f"  Salary: ${self.salary:,.2f}")
        print("-" * 40)
    
    def update_salary(self, new_salary):
        """Update employee salary"""
        if new_salary >= 0:
            old_salary = self.salary
            self.salary = new_salary
            print(f"Salary updated for {self.name}")
            print(f"  Old salary: ${old_salary:,.2f}")
            print(f"  New salary: ${self.salary:,.2f}")
        else:
            print("Error: Salary cannot be negative")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        """Add an employee to the department"""
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"Employee {employee.name} added to {self.department_name} department")
        else:
            print("Error: Invalid employee object")
    
    def calculate_total_salary(self):
        """Calculate total salary expenditure for the department"""
        total = sum(employee.salary for employee in self.employees)
        return total
    
    def display_total_expenditure(self):
        """Display total salary expenditure for the department"""
        total = self.calculate_total_salary()
        print(f"\nTotal Salary Expenditure for {self.department_name}:")
        print(f"  ${total:,.2f}")
        print(f"  Number of employees: {len(self.employees)}")
        print()
    
    def display_all_employees(self):
        """Display all employees in the department"""
        if not self.employees:
            print(f"No employees in {self.department_name} department")
            return
        
        print(f"\nAll Employees in {self.department_name} Department:")
        print()
        for i, employee in enumerate(self.employees, 1):
            print(f"\nEmployee {i}:")
            employee.display_details()


def get_employee_input():
    """Get employee details from user input"""
    print("\nEnter Employee Details:")
    name = input("Name: ").strip()
    
    while True:
        try:
            employee_id = input("Employee ID: ").strip()
            if employee_id:
                break
            else:
                print("Employee ID cannot be empty")
        except ValueError:
            print("Please enter a valid employee ID")
    
    while True:
        try:
            salary = float(input("Salary ($): "))
            if salary >= 0:
                break
            else:
                print("Salary cannot be negative")
        except ValueError:
            print("Please enter a valid salary amount")
    
    return Employee(name, employee_id, salary)


def main():
    print()
    print("EMPLOYEE AND DEPARTMENT MANAGEMENT SYSTEM")
    print()
    
    # Create a department
    dept_name = input("Enter department name: ").strip()
    department = Department(dept_name)
    
    while True:
        print()
        print("MENU:")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Display Total Expenditure")
        print("4. Update Employee Salary")
        print("5. Exit")
        print()
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            # Add employee
            employee = get_employee_input()
            department.add_employee(employee)
            
        elif choice == "2":
            # Display all employees
            department.display_all_employees()
            
        elif choice == "3":
            # Display total expenditure
            department.display_total_expenditure()
            
        elif choice == "4":
            # Update employee salary
            if not department.employees:
                print("No employees in the department to update")
                continue
                
            print("\nCurrent Employees:")
            for i, emp in enumerate(department.employees, 1):
                print(f"{i}. {emp.name} (ID: {emp.employee_id})")
            
            try:
                emp_choice = int(input("Select employee number to update salary: ")) - 1
                if 0 <= emp_choice < len(department.employees):
                    employee = department.employees[emp_choice]
                    new_salary = float(input(f"Enter new salary for {employee.name}: $"))
                    employee.update_salary(new_salary)
                else:
                    print("Invalid employee number")
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == "5":
            print("\nThank you for using the Employee Management System!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main() 