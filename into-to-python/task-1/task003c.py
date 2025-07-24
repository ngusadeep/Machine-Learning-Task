from stdsscores_file import stdsscores

#to calculate CA & FM for each student
test_one = []
test_two = []
UE = []
CA = []
FM = []
GRADES = []
remarks = []

for test1 in stdsscores:
    test_one.append(test1[1])
for test2 in stdsscores:
    test_two.append(test2[2])
    
for exam_m in stdsscores:
        UE.append(exam_m[3])
        
for i, j in zip(test_one, test_two):
    total = (i * 0.45) + (j * 0.55)
    CA.append(round(total , 1))

for k, l in zip(CA, UE):
    r = (k * 0.5) + (l* 0.5)
    FM.append(round(r,1))


for mark in FM:
    if 70 <= mark <=100:
        GRADES.append('A')
    elif 60 <= mark < 70:
        GRADES.append('B+')
    elif 50 <= mark < 60:
        GRADES.append('B')
    elif 40 <= mark < 50:
        GRADES.append('C')
    elif 35 <= mark < 40:
        GRADES.append('D')
    else:
        GRADES.append('E')

for grade in GRADES:
    if grade == 'E':
        remarks.append('F')
    else:
        remarks.append('P')


#CA , UE , FM
# for n in CA:
#   print(f'Student CA:{n}')
# for m in UE:
#   print(f'Student UE:{m}')
# for o in FM:
#   print(f'Student FM:{o}')
# for g in GRADES:
#   print(f'Student GRADES:{g}')
# for rm in remarks:
#   print(f'Student remarks:{rm}')


