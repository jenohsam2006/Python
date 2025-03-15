#Jenoh Sam J B
#URK24CS1154
#create a class to represent a area rectangle
print("URK24CS1154")
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def __add__(self, other):
        return Rectangle(self.length + other.length, self.breadth + other.breadth)
    def __str__(self):
        return f"Length is {self.length} and Breadth is {self.breadth}"
    def area(self):
        return self.length * self.breadth
    def __eq__(self, other):
        return self.area() == other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __ge__(self, other):
        return self.area() >= other.area()
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 6)
r3 = r1 + r2
print(r3)
print(r1 == r2)
print(r1 < r2)
print(r1 > r2)
print(r1 >= r2)
print(r1 <= r2)


#Jenoh Sam J B
#URK24CS1154
#department details of a University
print("URK24CS1154")
class Department:
    def __init__(self, name, hod, faculty, students, programs):
        self.name, self.hod, self.faculty, self.students, self.programs = name, hod, faculty, students, programs
    def __str__(self):
        return f"{self.name} | HOD: {self.hod} | Faculty: {self.faculty} | Students: {self.students} | Programs: {self.programs}"
class University:
    def __init__(self):
        self.departments = {}
    def manage(self, action):
        name = input("Department Name: ")
        if action == 'add':
            self.departments[name] = Department(name, input("HOD: "), input("Faculty: "), input("Students: "), input("Programs: "))
        elif name in self.departments:
            dept = self.departments[name]
            if action == 'edit':
                dept.hod = input("New HOD: ") or dept.hod
                dept.faculty = input("New Faculty: ") or dept.faculty
                dept.students = input("New Students: ") or dept.students
                dept.programs = input("New Programs: ") or dept.programs
            elif action == 'delete':
                del self.departments[name]
        else:
            print("Not found!") 
    def display(self):
        print("\n".join(map(str, self.departments.values())) or "No departments.")
uni = University()
while (c := input("1.Add 2.Edit 3.Delete 4.Display 5.Exit\nChoice: ")) != '5':
    uni.manage({'1': 'add', '2': 'edit', '3': 'delete'}.get(c, '')) if c in '123' else uni.display()
