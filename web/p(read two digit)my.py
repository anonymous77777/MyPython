# C12H4O45
A = ['C','H','O']
W = [12.0110,1.0079,15.9994]
B = ['0','1','2','3','4','5','6','7','8','9']
S = " "
while True:
    S = input("Enter a chemical formula, or just the enter key to quit:"); # C12H4O45
    if len(S) == 0: 
        break
    L = list(S) # L = ['C','1','2','H','H','2','4','5']
    if L[0] not in A: # L[0] is the first character in our list, in this case 'C'.
        print("Badly formed molecular formula; try again.\n")
        continue # with a continue, we are going to ask the user to input a different chemical formula
    N = [0,0,0]
    i = 0 # i = 1
    while i < len(L): # len(L) = 9
        if L[i] not in B: # if L[0] not in B:
            i = i+1
            continue
        if (i+1) < len(L): # if 1+1 < 9
            if L[i+1] in B:  # if L[2] in B this part we check whether there are two  digits after an element
                N[A.index(L[i-1])] += int(L[i])*10 + int(L[i+1]) # N[0] += 
                if (i+2) < len(L):
                    if L[i+2] in B:
                        N[A.index(L[i-1])] += int(L[i])*100 + int(L[i+1])*10 + int(L[i+2])# N[0] +=
                        del L[i+2]
                else:
                    N[A.index(L[i-1])] += int(L[i])*10 + int(L[i+1]) # N[0] += 
                        
                    
 
                
               
            else:
                N[A.index(L[i-1])] += int(L[i])
        else:
            N[A.index(L[i-1])] += int(L[i])
        del L[i+1]
        del L[i]
        del L[i-1]
        
    j = 0
    x = 0
    while j < len(A):
        N[j] += L.count(A[j])
        x += W[j] * N[j]
        j += 1
    print("The molecular weight is %.4f"%(x),"\n")

