name_of_file = input('Enter name of input file: ')
#name_of_file = 'GPA_input.txt'
fint = open(name_of_file)
fout = open('GPA_output.txt', 'w')
def calculate_GPA(cfint, cfout): # S stands for course information; course number; units; and grades
    A = ['F','D','C','B','A']
    Sname = cfint.readline().strip('\n')
    if Sname == '\n' or Sname == '':
        return Sname
    t1 = 0
    t2 = 0
    while True:
        S = cfint.readline()
        if S == '\n' or S == '':
            break
        L = S.split()
        t1 += int(L[1])
        t3 = A.index(L[2][0])
        if len(L[2]) > 1:
            t3 = eval(str(t3) + L[2][1] + '0.3')
        t3 = 4 if t3 > 4 else t3
        t3 = 0 if t3 < 0 else t3
        t2 += (t3 * int(L[1]))
    cfout.write("%-26s%.2f\n" % (Sname, (t2 / t1)))
    return S

while True:
    x = calculate_GPA(fint, fout)
    if x == '':
        break
fout.close()
fint.close()

