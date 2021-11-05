eng2uz = dict()
eng2uz2 = {}
student = {'name': 'Dinora',
           'id': 1111,
           'course': 'BIS'}
eng2uz['one'] = 'bir'

print(eng2uz)
print(eng2uz2)
print(student)
print(student['course'])
print(len(student))
print('name' in student)
print('modules' in student)

vals = student.values()
print('BIS' in vals) #checks for values