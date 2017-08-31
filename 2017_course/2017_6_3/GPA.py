name_of_file = input('Enter name of input file: ')
fint = open(name_of_file)
fout = open('GPA_output.txt', 'w')
A = ['F','D','C','B','A']
t1 = 0
t2 = 0
def calculate_GPA(): # S stands for course information; course number; units; and grades
    while True:
        global t1
        global t2
        S = fint.readline()
        if len(S) == 0:
            break
        L = S.split()
        t1 += int(L[1])
        t3 = A.index(L[2][0])
        if len(L[2]) > 1:
            t3 = eval(str(t3) + L[2][1] + '0.3')
        t3 = 4 if t3 > 4 else t3
        t3 = 0 if t3 < 0 else t3
        t2 += (t3 * int(L[1]))
    t1 = 0
    t2 = 0
    GPA = float(t2 / t1)
    return GPA

while True:
    student_name = fint.readline()
    calculate_GPA()
    if student_name == 'n' or student_name =='':
        break
fout.close()
fint.close()

