"""
def factorial(n):
    for i in range(1,n+1):
        i *= (i+1)
    return i

def committee(people, members, chairperson):
    if chairperson == True:
        ways = int(factorial(members) / ((factorial(people)-1)*factorial(members-people)))
        return ways
    else:
        ways = int(factorial(members) / (factorial(people) * factorial(members-people)))
        return ways
    
committee(10,3,True)
committee(10,3,False)
committee(members = 3, people = 10, chairperson = True)
committee(chairperson = False, members = 3, people = 10)
committee(2,2,True)
committee(3,3,False)
"""

def factorial(n):
    try:
        if n < 0:
            f = 0
            raise ValueError('Cannot take the factorial of a negative number.')

        f = 1
        for i in range(2, n+1):
            f *= i

    except ValueError as excpt:
        print(excpt)

    return f

def committee(people, members, chairperson = True):
    try:
        if people <= 0:
            raise ValueError('People count must be positive.')
        if members > people:
            raise ValueError('Member count must not be greater than people count.')

        if chairperson:
    #        ways = int(factorial(members) / ((factorial(people-1))*factorial(members-people)))
            ways = int(factorial(people) / ((factorial(members-1))*factorial(people-members)))
        else:
    #        ways = int(factorial(members) / (factorial(people) * factorial(members-people)))
            ways = int(factorial(people) / (factorial(members) * factorial(people-members)))

        return ways

    except ValueError as excpt:
        print(excpt)

