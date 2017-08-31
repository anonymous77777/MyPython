def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
       
    

n = int(input("Enter the number of people\n"))

r = int(input("Enter the number of chairs at table 1\n"))

s = int(input("Enter the number of chairs at table 2\n"))

num_at_1 = factorial(r)
num_at_2 = factorial(s)
num = factorial(n)
total = int(num / (num_at_1 * num_at_2))

print('The number of table assignment is', total)


    
        
