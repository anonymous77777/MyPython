import committee
available = total_num = int(input("Enter the number of professors in the department:\n"))
can_or_not = input("Can a professor be on multiple committees? Enter y or n:\n")
total_ways = 1
chairperson = {'y': True, 'n': False}
while True:
    name = input('Enter that name of the committee:\n')
    if name == '':
        break
    need_or_not = input('Does the committee need a chairperson? Enter y or n:\n')
    num_of_memb = int(input('Enter the number of members:\n'))
    if can_or_not == 'n':
        available -= num_of_memb
        if available <= 0:
            break
    if available < num_of_memb:
        num_of_memb = available
        print("Assigning only %d members to the %s committee.\n" %(available, name))
    try:
        ways = committee.committee(available, num_of_memb, chairperson[need_or_not])
        print('There are %d ways to form the %s committee' %(ways, name))
    except ValueError as excpt:
        print(excpt)
        
    total_ways *= ways
print('There are %d ways to form all the committees.' %total_ways)
        
