def fibonacci(n):
    global calls
    calls += 1
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
       

n=int(input('Enter how far you want to compute the Fibonacci sequence up to\n'))
print('Here is the Fibonacci sequence for n=%d' %n)

for i in range(n+1):
    calls = 0
    f = fibonacci(i)
    print("i", i, "Fibonacci", f, "calls", calls, "ratio", f/calls)
