eng2uz = dict()
eng2uz2 = {}
student = {'name': 'Dinora',
           'id': 1111,
           'course': 'BIS'}
eng2uz['one'] = 'bir'

def calculateAverage(myFinalMarks):
    total = 0
    for key in myFinalMarks:
        total = total + myFinalMarks[key]

    average = total / len(myFinalMarks)
    return average

def histogram(s):
    d = dict() #emty dictionary is created
    for c in s:
        if c not in d: #if it is not a dictionary
            d[c] = 1
        else:
            d[c] += 1
    return d

def get_input():
    cw_weight = float(input("enter cw weight: "))
    cw_mark = int(input("enter mark: "))
    exam_weight = float(input("enter exam weight: "))
    exam_mark = int(input("enter exam mark: "))
    csf = {
        'cw1-weight': cw_weight,
        'cw1-mark': cw_mark,
        'exam-weight': exam_weight,
        'exam-mark': exam_mark
    }
    return csf

#print(eng2uz)
print(eng2uz2)
print(student)
print(student['course'])
print(len(student))
print('name' in student)
print('modules' in student)
print(calculateAverage({'CSF': 70, 'FunPro': 40, 'WT': 85}))
print(histogram('Computer'))
print(calculate_mark(get_input()))