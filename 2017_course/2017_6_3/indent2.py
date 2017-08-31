def scramble(input, indent):
    output = []
    for i in range(len(input)):
        copy = input
        item = copy.pop(i)
        sub_scramble = scramble(copy, indent + "   ")
        for j in sub_scramble:
            print(indent, "item", item, "j", j)
            output.append(item + sub_scramble)
    return output

list = ["Able", "Baker", "Charlie"]
s = scramble(list, "   ")
for i in s:
    print[i]
        
