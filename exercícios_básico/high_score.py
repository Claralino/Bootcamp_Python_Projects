
students_scores = input("type the students scores: ").split( )
max_score = 0

for scores in range(0, len(students_scores)):
    students_scores[scores] = int(students_scores[scores])

for i in range(0, len(students_scores)):
    if students_scores[i] > max_score:
        max_score = students_scores[i]
    else:
        max_score = max_score

print(f'the high score is: {max_score}')

