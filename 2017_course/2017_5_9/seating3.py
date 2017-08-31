def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number of people\n"))
k = 0
j = 1
total = factorial(n)
while k < n:
    
    i = int(input('Enter the number of chairs at table %d\n' %j ))
    j += 1
    k = k + i

#    total = total / factorial(i)
#    if k > n:
#        total = total / factorial(n-k)

    if (k > n):
        i = i - (k - n)
        print("Seating only {} people at table {}".format(i, (j-1)))
    total = total / factorial(i)

print('The number of table assignments is %d' %total)
