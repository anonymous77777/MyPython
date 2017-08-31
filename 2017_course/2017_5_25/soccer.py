Dictionary = {}

for i in range(1,6):
    jersey_number = int(input('Enter player %d jersey number:\n' % i))
    rating = int(input('Enter palyer %d rating:\n' % i))
    Dictionary[jersey_number] = rating
    i += 1

list_of_jersey_number = []
for jn in Dictionary:
    list_of_jersey_number.append(jn)

new_list = sorted(list_of_jersey_number)
print()
print('ROSTER')
for num in new_list:
    print('Jersey number: %d, Rating: %d' % (num, Dictionary[num]))

print('MENU')
print('a - Add player')
print('d - Remove player')
print('u - Update player rating')
print('r - Output players above a rating')
print('o - Output roster')
print('q - Quit')
option = print('Choose an option:')
if option == 'q':
    break
if option == 'o':
    print('ROSTER')
    for num in new_list:
        print('Jersey number: %d, Rating: %d' % (num, Dictionary[num]))
if option == 'a':
    new_jersey = int(input('Enter a new player jersey number:\n'))
    new_rating = int(input('Enter the player rating:\n'))
    Dictionary[new_jersey] = new_rating
if option == 'd':
    num_to_be_del = int(input('Enter a jersey number:\n'))
    del Dictionary[num_to_be_del]
if option == 'u':
    old_num = int(input('Enter a jersey number:\n'))
    now = int(input('Enter a new rating for player:\n'))
    Dictionary[old_num] = now
if option == 'r':
    w = int(input('Enter a rating:\n'))
    print()
    if w in Dictionary.values():
        print('ABOVE 5')
        
    
    
    
                
    
