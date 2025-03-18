#Jenoh Sam J B
#URK24CS1154
#create a base class called Employee and derive sub classes
print("URK24CS1154")
class Employee:
    def __init__(self, basic_salary, da_percent, hra_percent, tax_percent, epf):
        self.basic_salary = basic_salary
        self.da_percent = da_percent
        self.hra_percent = hra_percent
        self.tax_percent = tax_percent
        self.epf = epf
    def calculate_gross_salary(self):
        da = (self.da_percent / 100) * self.basic_salary
        hra = (self.hra_percent / 100) * self.basic_salary
        return self.basic_salary + da + hra
    def calculate_tax(self):
        return (self.tax_percent / 100) * self.calculate_gross_salary()
    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax() - self.epf
    def print_pay_details(self):
        print(f"Basic Salary: {self.basic_salary}")
        print(f"DA: {self.da_percent}%")
        print(f"HRA: {self.hra_percent}%")
        print(f"Gross Salary: {self.calculate_gross_salary()}")
        print(f"Tax: {self.calculate_tax()}")
        print(f"EPF: {self.epf}")
        print(f"Net Salary: {self.calculate_net_salary()}\n")
class Manager(Employee):
    def __init__(self):
        super().__init__(basic_salary=30000, da_percent=95, hra_percent=20, tax_percent=25, epf=3000)
class Engineer(Employee):
    def __init__(self):
        super().__init__(basic_salary=20000, da_percent=80, hra_percent=15, tax_percent=15, epf=2000)
while True:
    print("Choose an Employee Type:")
    print("1. Manager","\n2. Engineer","\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        employee = Manager()
    elif choice == "2":
        employee = Engineer()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Try again.")
        continue
    print("Choose an option:")
    print("a) Calculate Gross Salary")
    print("b) Calculate Net Salary")
    print("c) Calculate Tax")
    print("d) Print Pay Details")
    option = input("Enter option: ").lower()
    if option == "a":
        print(f"Gross Salary: {employee.calculate_gross_salary()}\n")
    elif option == "b":
        print(f"Net Salary: {employee.calculate_net_salary()}\n")
    elif option == "c":
        print(f"Tax: {employee.calculate_tax()}\n")
    elif option == "d":
        employee.print_pay_details()
    else:
        print("Invalid option! Try again.")


#Jenoh Sam J B
#URK24CS1154
#create a class Worker and derive two classes DailyWorker and SalariedWorker
print("URK24CS1154")
class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate
    def comp_pay(self, hours):
        pass
    def display(self):
        print(f"Worker Name: {self.name}")
        print(f"Salary Rate: {self.salary_rate}")
class DailyWorker(Worker):
    def comp_pay(self, hours):
        return self.salary_rate * hours
class SalariedWorker(Worker):
    def comp_pay(self, hours):
        return self.salary_rate * 40
worker1 = DailyWorker("John", 500)
worker2 = SalariedWorker("Alice", 400)
print("\nDaily Worker Details:-")
worker1.display()
print(f"Weekly Pay (worked 6 days, 8 hours/day): {worker1.comp_pay(6 * 8)}\n")
print("Salaried Worker Details:-")
worker2.display()
print(f"Weekly Pay (worked 45 hours but fixed pay for 40 hours): {worker2.comp_pay(45)}\n")
