import committee
n = int(input('Enter the number of professors in the department:\n'))
c_or_not = input('Can a professor be on multiple committees? Enter y or n:\n')
availiable = n
total_way = 1
while True:
    name = input('Enter that name of the committee:\n')
    if name == '':
        break
    need_or_not = input('Dose the committee need a chairperson? Enter y or n:\n')
    if need_or_not == 'y':
        s = True
    elif need_or_not == 'n':
        s = False
    r = int(input('Enter the number of members:\n'))
    if c_or_not != 'y':
        if availiable <= 0:
            break
    if availiable < r:
        r = availiable
        print('Assigning only %d members to the %s committee' %(availiable, name))
    try:
        way = committee.committee(n, r, s)
        print('There are %d ways to form the %s committee.' %(way, name))
        if c_or_not != 'y':
            availiable -= r
        total_way *= way
    except ValueError as message:
        print(message)
       
    


print('There are %d ways to form all the committees.' % total_way)
