number_of_element = int(input().strip())

elements = dict()
for i in range(0, number_of_element):
    elements[i+1] = int(input().strip())

element_line = []
previous_key = 1
element_line.append(previous_key) 
for _ in range(number_of_element - 1):
    element_line.append(elements[previous_key]) 
    previous_key = elements[previous_key]

element_line = [str(e) for e in element_line]
print(' '.join(element_line))
