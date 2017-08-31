#for i in range(10,0,-2):
#    print(i*i)

# i1 = float(input());
# i2 = float(input());
# i3 = float(input());
# i4 = float(input());

# for x in (1,2,3,4):
#     xx[x]=float(input())
#     x += 1

# xx = range(4)
# xx = float(input())

# sum =i1+i2+i3+i4
# t=sum+sum*0.85
# print('%.2f'%t)

# def test_args_kwargs(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
#
# kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
# test_args_kwargs(**kwargs)

# def greet_me(**kwargs):
#     for key1, value1 in kwargs.items():
#         print("{0} == {1}".format(key1, value1))
#
# greet_me(name="yasoob", xx="XX")
'''''""
def generator_function():
    for i in range(10):
        yield i
for item in generator_function():
    print(item)
'''

A = ['C','H','O']
W = [12.0110,1.0079,15.9994]
B = ['0','1','2','3','4','5','6','7','8','9']
S = " "
while True:
    N = [0,0,0]
    S = input("Enter a chemical formula, or just the enter key to quit:");
    if len(S) == 0:
        break
    L = list(S)
    if L[0] not in A:
        print("Badly formed molecular formula; try again.\n")
        continue
    i = 0
    x = S.split("C|H|O")
    print(x)
'''
    while i < len(L):
        if L[i] not in B:
            i = i+1
            continue
        j = i+1
        while j < len(L):
            if L[j] in B:
                j += 1
            else:
                break
        j -= 2
        k = j
        while k >= 0:
            N[A.index(L[i-1])] += int(L[i+k]) * pow(10, j-k)
            del L[i+k]
            k -= 1
        del L[i-1]
    
    j = 0
    x = 0
    while j < len(A):
        N[j] += L.count(A[j])
        x += W[j] * N[j]
        j += 1
    print("The molecular weight is %.4f"%(x),"\n")
'''
