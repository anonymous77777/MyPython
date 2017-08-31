A = ['F','D','C','B','A']
t1 = 0
t2 = 0

while True:
    S = input("Enter course number, units, and grade, separated by spaces\n");
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

print('The GPA is %.2f' % (t2 / t1))
