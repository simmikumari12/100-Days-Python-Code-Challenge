grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
num_students =len(grades)
print(f"\n{num_students} Students took the exam.")
print(f"The highest grade was: {max(grades)}")
print(f"The lowest grade was: {min(grades)}")
print(f"The average grade was: {sum(grades)/num_students}")

day1 = ["Mary", "Jake", "Sam", "Alex", 'Percy', "Jessica", "Trent", "Mahmoud"]
day2 = ["Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"]

student = []
students_one_day = []
students_in_second_day = []
students_in_both_day = []

for s in day1:
    if s not in day2:
        students_one_day.append(s)

for t in day2:
    if t not in day1:
        students_one_day.append(t)

for u in day1:
    if u in day2:
        student.append(u)

print(f"\n{len(student) + len(students_one_day)} students attended the class.")
print(f"{student} attended both class days.")    
print(f"{students_one_day} atttended one class day.")
