#Employee Management System
class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}"

if __name__ == "__main__":
    emp1 = Employee(101, "John", "IT")
    emp2 = Employee(102, "Sara", "HR")

    print("Employee Details from GitHub:")
    print(emp1.display_info())
    print(emp2.display_info())

