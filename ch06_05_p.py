data_source = open('score.txt')

student_ids = list()
for student_line in data_source:
    student_id, _ = student_line.split()
    student_ids.append(student_id)

# Bubble sort
id_sorted = False
while not id_sorted:
    id_sorted = True
    for i in range(0, len(student_ids) - 1):
        if int(student_ids[i+1]) > int(student_ids[i]):
            id_sorted = False
            student_ids[i], student_ids[i+1] = student_ids[i+1], student_ids[i] 

print("\n".join(student_ids))
