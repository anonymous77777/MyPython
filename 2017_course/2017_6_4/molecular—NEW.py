weight = {'C': 12.0110, 'H': 1.0079, 'O': 15.9994}
count = [0, 0, 0] # count = [C, H ,O]
while True:
    formula = input('Enter  a chemical formula, or just the enter key to quit:')
    #formula = 'COOHC6H40CO120H'
    if formula == '' or formula == '\n':
        break
    if formula[0].isdigit() or formula[0].islower():
        print('Badly formed molecular formula; try again.')
        continue
    L = list(formula)
    #L = ['C','O','O','H','C','6','H','4','0','C','O','1','2','O','9']
    for i in range(len(L)):
        if L[i].isdigit():
            continue
        if L[i] == 'C':
            if L[i] == L[-1]:
                count[0] += 1
            elif L[i] == L[-2]:
                count[0] += int(L[i+1])
            else:
                if L[i+1].isdigit():
                    count[0] += int(L[i+1])
                    if L[i+2].isdigit():
                        count[0] += int(L[i+1]*10) + int(L[i+2])
                    else:
                        count[0] += int(L[i+1])
                else:
                    count[0] += 1


        elif L[i] == 'O':
            if L[i] == L[-1]:
                count[2] += 1
            elif L[i] == L[-2]:
                count[2] += int(L[i+1])
            else:
                if L[i+1].isdigit():
                    count[2] += int(L[i+1])
                    if L[i+2].isdigit():
                        count[2] += int(L[i+1])*10 + int(L(i+2))
                    else:
                        count[2] += int(L[i+1])
                else:
                    count[2] += 1
    

        elif L[i] == 'H':
            if L[i] == L[-1]:
                count[1] += 1
            elif L[i] == L[-2]:
                count[1] += int(L[i+1])
            else:
                if L[i+1].isdigit():
                    count[1] += int(L[i+1])
                    if L[i+2].isdigit():
                        count[1] += int(L[i+1])*10 + int(L(i+2))
                    else:
                        count[1] += int(L[i+1])
                else:
                    count[1] += 1
    
    weight = float(weight['C']*count[0] + weight['H']*count[1] + weight['O']*count[2])
    print('The molecular weight is %.4f' % weight)
    count = [0, 0, 0]

    
    
    
