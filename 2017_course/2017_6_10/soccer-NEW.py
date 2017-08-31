def Output_roster():
    print('Roster')
    for i in range(len(list)):
        print('Jersey number: %d, Rating: %d' % (list[i], dic[list[i]]))


def Menu():
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')

def Add_player():
    new_num = int(input("Enter a new player's jersey number:\n"))
    his_rating = int(input("Enter the player's rating:\n"))
    list.append(new_num)
    list.sort()
    dic[new_num] = his_rating
    

def Delete_player():
    num_to_del = int(input('Enter a jersey number:\n')) 
    del dic[num_to_del]
    
def Update_player_rating():
    num_to_update = int(input('Enter a jersey number:\n')) 
    new_rating = int(input('Enter a new rating for player:\n')) 
    dic[num_to_update] = new_rating

def Output_players_above_a_rating(new_dic1):
    w_rating = int(input('Enter a rating:\n'))
    new_list = list(new_dic1.values())   # new_list = [3, 8, 3, 2] rating
    list_for_jersey = list(new_dic1.keys()) # list_for_jersey = [5, 7, 12, 20]
    print('Above %d' % w_rating)
    for i in range(len(new_list)):
        if new_list[i] > w_rating:           
            print('Jersey number: %d, Rating: %d' % (list_for_jersey[i], new_list[i]))

dic = {}
list = []
for i in range(1,6):
    jer_num = int(input("Enter player %d's jersey number:\n" %i))
    rating = int(input("Enter player %d's rating:\n" %i))
    print()
    dic[jer_num] = rating
    list.append(jer_num)
new_dic = {}
list.sort() # list = [20, 35, 87, 90, 120]
print('Roster')
for i in range(len(list)):
    print('Jersey number: %d, Rating: %d' % (list[i], dic[list[i]]))
    new_dic[list[i]] = dic[list[i]]
    #new_dic = {5:3, 7:8, 12:3, 20:2}

while True:
    Menu()
    opt = input('Choose an option:\n')
    if opt == 'q':
        break
    if opt == 'o':
        Output_roster()
    if opt == 'a':
        Add_player()
    if opt == 'd':
        Delete_player()
    if opt == 'u':
        Update_player_rating()
    if opt == 'r':
        Output_players_above_a_rating(new_dic)
                  
                  
