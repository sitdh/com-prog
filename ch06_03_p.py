grade_resource = open('score.txt')
student_info = list()

for line in grade_resource:
    data = line.split()
    data[1] = int(data[1])
    student_info.append(data)

grade_resource.close()

sid = int(input().strip())
needle = list()
while sid > 0:
    needle.append(str(sid))
    sid = int(input().strip())

for sid in needle:
    result = 'Not Found'
    for student_record in student_info:
        if sid in student_record:
            result = student_record[1]

    print(result)
