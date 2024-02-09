# Base class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

# Subclass Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

# Subclass Developer inheriting from Employee
class Developer(Employee):
    def __init__(self, name, salary, productivity):
        super().__init__(name, salary)
        self.productivity = productivity

    def calculate_salary(self):
        return super().calculate_salary() * self.productivity

# Subclass Intern inheriting from Employee
class Intern(Employee):
    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration

    def calculate_salary(self):
        return super().calculate_salary() * self.duration

# Function to calculate total salary expense using list comprehension
def total_salary_expense(employees):
    return sum([employee.calculate_salary() for employee in employees])

# Sample usage
manager1 = Manager("John", 5000, 1000)
developer1 = Developer("Alice", 4000, 1.2)
intern1 = Intern("Bob", 2000, 0.5)

employees = [manager1, developer1, intern1]
total_expense = total_salary_expense(employees)
print("Total Salary Expense:", total_expense)
