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

