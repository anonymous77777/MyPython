def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter the number of people\n")) # n = 5

i = 0
while i <= n:
    j = 1
    x = int(input('Enter the number of chairs at table',j,"\n")) # people at different table
    i += x
    j += 1
    total *= factorial(n) / factorial(x)#FIXEDME
print('The number of table assignments is', total)
 

                  
