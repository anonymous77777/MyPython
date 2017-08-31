def scramble(input):
    output = []
    length = len(input)
    if length == 1:
        output = [input]
    else:
      for i in range(length):
        copy = input[:]
        item = copy.pop(i)
        sub_scramble = scramble(copy)
        for j in sub_scramble:
            extended_list = [item]
            extended_list.extend(j)
            output.append(extended_list)
    return output
if __name__ == "__main__":
    list = ["Able", "Baker", "Charlie"]
    s = scramble(list)
    for i in s:
        print(i)
        
