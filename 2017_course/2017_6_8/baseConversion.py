def baseConversion(num, base):
    if num >= base :
        baseConversion((num // base), base)
        print((num % base), end = ' ')
    else:
        print(num, end = ' ')

num = int(input('Enter a num:'))
base = int(input('Enter a base:'))
baseConversion(num, base)
