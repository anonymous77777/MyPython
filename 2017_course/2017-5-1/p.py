A = ['C','H','O']
W = [12.0096,1.00784,15.999]
#W = [12.0116,1.00811,15.99977]
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
    while i < len(L):
        if L[i] not in B:
            i = i+1
            continue
        if (i+1) < len(L):
            if L[i+1] in B:
                N[A.index(L[i-1])] += int(L[i])*10 + int(L[i+1])
                del L[i+1]
            else:
                N[A.index(L[i-1])] += int(L[i])
        else:
            N[A.index(L[i-1])] += int(L[i])
        del L[i]
        del L[i-1]

    j = 0
    x = 0
    while j < len(A):
        N[j] += L.count(A[j])
        x += W[j] * N[j]
        j += 1
    print("The molecular weight is %.4f"%(x),"\n")

