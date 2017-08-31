import committee

available = total_num = int(input('Enter the number of professors in the department: '))
can_or_cannot = input('Can a professor be on multiple committees? ')
total_ways = 1
chairperson = {'y': True, 'n': False}
while True:
    name_of_comt = input('Enter that name of the committee: ')
    if name_of_comt == '':
        break
    need_or_not = input('Dose the committee need a chairperson? Enter y or n: ')
    num_of_mem = int(input('Enter the number of members: '))

    if available < num_of_mem:
        num_of_mem = available
        print('Assigning only %d members to the %s committee.' % (available, name_of_comt))
    try:
        ways = committee.committee(available, num_of_mem, chairperson[need_or_not])
    except ValueError as excpt:
        print(excpt)
        continue
    total_ways *= ways
    print('There are %d ways to form the %s committee.' % (ways, name_of_comt))
    if can_or_cannot == 'n':
        available -= num_of_mem
    if available <= 0:
        break

print('There are %d ways to form all the committees.' % total_ways)
