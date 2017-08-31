def factorial(n):
    if n < 0:
        raise ValueError('Cannot take the factorial of a negative number.')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def committee(people, members, chairperson = True):
    if people <= 0:
        raise ValueError('Invalid weight')
    if members > people:
        raise ValueError('Member count must not be greater than people count.')
    if chairperson == True:
        ways = int(factorial(people) / (factorial(members-1) * factorial(people-members)))
    elif chairperson == False:
        ways = int(factorial(people) / (factorial(members)*factorial(people-members)))
    return ways
    

