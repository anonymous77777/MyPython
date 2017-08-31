def foo2(n):
    if n != 0:
        foo2(n-1)

    print(n)

#    return

foo2(3)
