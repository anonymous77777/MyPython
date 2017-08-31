fout = open('GPA_output.txt', 'w')
name_of_file = input('Enter name of input file: ')
fint = open(name_of_file)
A = ['F','D','C','B','A']
t1 = 0
t2 = 0
while True:
    student_name = fint.readline()
    if student_name == 'n' or student_name =='':
        break
    while True:
        cour_unit_grade = fint.readline()
        if cour_unit_grade == 'n' or cour_unit_grade =='':
            break
        L = cour_unit_grade.split() # L = ['ECS10','4', 'B-']
        t1 += int(L[1])
        t3 = A.index(L[2][0])
        if len(L[2]) > 1:
            t3 = eval(str(t3) + L[2][1] + '0.3')
        t3 = 4 if t3 > 4 else t3
        t3 = 0 if t3 < 0 else t3
        t2 += (t3 * int(L[1]))
    GPA = t2 / t1
    f.write("%-26s%.2f\n" % (student_name, GPA))
    t1 = 0
    t2 = 0

fout.close()
fint.close()
 

