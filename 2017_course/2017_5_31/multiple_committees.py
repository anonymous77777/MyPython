import committee


total_num = int(input('Enter the number of professors in the department:'))
can_or_cannot = input('Can a professor be on multiple committees?')
ways = []
while True:
    name_of_comt = input('Enter that name of the committee:')
    if name_of_comt = '':
        break
    need_or_not = input('Dose the committee need a chairperson?Enter y or n:')
    num_of_mem = int(input('Enter the number of members:'))
    available = total_num - num_of_mem
    
    if can_or_cannot = 'y': # ?

    else: #not allowed
 
        if available <= 0:
            break
        avaiable -= num_of_mem
    if available < num_of_mem:
        num_of_mem = total
        print('Assigning only %d members to the %s committee.' % (available,name_of_comt))

    way = committee.committee(total_num, num_of_mem)
    ways.append(way)
    print('There are %d ways to form the %s committee.' % (ways, name_of_comt))
total_ways = 1
for i in ways:
    total_ways *= i
print('There are %d ways to form all the committees.' % total_ways)
    


    
            
        










if can_or_cannot = 'y':
        # There is no limit on how many committees a professor can serve on or chair
else:
        # Each professor can serve on at most one committee.
        # if there are no unassigned professors left after a committee is formed
