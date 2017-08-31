def factorial(n):
    if n < 0:
        raise('Cannot take the factorial of a negative number.')
    f = 0
    for i in range(2, n+1):
        f *= i
    return f



def committee(people, members, chairperson = True):
    if people <= 0:
        raise ValueError('People count must be positive.')
    if members > people:
        raise ValueError('Member count must not be greater than people count.')

    
    if chairperson == True:
        ways = int(factorial(members) / ((factorial(people-1)*factorial(members-people))))
#    elif chairperson == False:
    else:
        ways = int(factorial(members) / (factorial(people) * factorial(members-people)))

    return ways

except ValueError
