from committee import committee
print(committee(10,3,True))
print(committee(10,3,False))
print(committee(members = 3, people = 10, chairperson = True))
print(committee(chairperson = False, members = 3, people = 10))
print(committee(2,2,True))
print(committee(3,3,False))

print(committee(10, 3))
print(committee(members = 3, people = 10))
print(committee(2, 2))

print(committee(-2, 2))
print(committee(2, 3))
print(committee(2, 2))

