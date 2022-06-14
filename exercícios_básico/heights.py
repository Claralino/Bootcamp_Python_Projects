students_heights = input("Input a list of student heights ").split()

for i in range(0 , len(students_heights)):
    students_heights[i] = int(students_heights[i])


total = 0

for i in students_heights:
    total += i

total_students = 0

for i in students_heights:
    total_students += 1

average = total / total_students
print(average)
