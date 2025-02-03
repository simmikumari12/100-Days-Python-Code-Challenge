class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Education:
    def __init__(self, school, major):
        self.school = school
        self.major = major

class Course(Education):
    def __init__(self, school, major, course_name):
        Education.__init__(self, school, major)
        self.course_name = course_name

class Student(Course, Person):
    def __init__(self, name, age, school, major, course_name):
        Course.__init__(self, school, major, course_name)
        Person.__init__(self, name, age)

    def print_data(self):
        print("\nStudent Data: ")
        print(f"Name = {self.name}, age = {self.age}, school = {self.school} major= {self.major}, course_name = {self.course_name}\n")

def main():
    while True:

        Sname = input("\nEnter Student Name: ").title()
        Sage = int(input("Enter Student's Age: "))
        Sschool = input("Enter School Name: ")
        Smajor = input("Enter Current Major: ")
        Scourse = input("Enter Courses: ")

        student1 = Student(f"{Sname}", f"{Sage}", f"{Sschool}", f"{Smajor}", f"{Scourse}")
        student1.print_data()

        c = input("Enter 'q' or 'quit' when done entering all Student Data !").lower()

        if c == "q" or c == "quit":
            break
        else:
            continue
    

if __name__ == "__main__":
    main()
