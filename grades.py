# from math import average
"""
For your second program in today’s lab, you will need to write a program that stores student’s exam grades as a list and student 
attendance as a set. 
Grades List
Exam Grades: 83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80
Attendance Sets
Day 1: Mary, Jake, Sam, Alex, Percy, Jessica, Trent, Mahmoud
Day 2: Jake, Sam, Alex, Percy, Mahmoud, Trent, Caleb, Zayne
Your program will then need to print out the answers to the following questions:
1. Grades
a. How many students took the exam?
b. What was the highest exam grade?
c. What was the lowest exam grade?
d. What was the class average for the exam?
2. Attendance
a. How many students attended the class?
b. Who attended both days of class?
c. Who attended only one day of class?
Report any floating-point values to 1 decimal place.
"""

# grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
# num_students =len(grades)
# print(f"{num_students} Students took the exam.")
# print(f"The highest grade was: {max(grades)}")
# print(f"The lowest grade was: {min(grades)}")
# print(f"The average grade was: {sum(grades)/num_students}")

day1 = ["Mary", "Jake", "Sam", "Alex", 'Percy', "Jessica", "Trent", "Mahmoud"]
day2 = ["Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"]

student = []
students_both_day = []

for s in day1:
    if s in day2:
        students_both_day.append(s)
        student.append(s) # students present in both first and second days
    
    if s not in day2:
        student.append(s) # students present only on first day

for t in day2:
    if t not in day1:
        student.append(t) # students present only on day2
print(f"{students_both_day} attended both class days")
print(f"{len(student)} students attended the class")