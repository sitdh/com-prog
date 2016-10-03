grade_resource = open('score.txt')
student_info = list()

for line in grade_resource:
    data = line.split()
    data[1] = int(data[1])
    student_info.append(data)

grade_resource.close()

student_id = input().strip()
for student_record in student_info:
    if student_id in student_record:
        print(student_record[1])
        exit()
