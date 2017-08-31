Dictionary = {}
MENU = {'a':'AddPlayer()','d':'RemovePlayer()',\
        'u':'UpdatePlayer()','r':'OutputAbove()',\
        'o':'ShowInOrder()','q':'exit()'}

def GetInput(strPrompt, scope):
    while True:
        str = input(strPrompt)
        if str.isdigit():
            if int(str) in scope:
                return(int(str))

def ShowInOrder(iAbove = 0):
    if iAbove == 0:
        print('\nROSTER')
    else:
        print('\nAbove %d'%iAbove)
    for i in (sorted(Dictionary.keys())):
        if Dictionary[i] > iAbove:
            print('Jersey number: %d, Rating: %d' % (i, Dictionary[i]))

def AddPlayer():
    new_jersey = GetInput('Enter a new player jersey number:\n', range(0,100))
    new_rating = GetInput('Enter the player rating:\n', range(1,10))
    Dictionary[new_jersey] = new_rating

def RemovePlayer():
    num_to_be_del = GetInput('Enter a jersey number:\n', range(0,100))
    if num_to_be_del in list(Dictionary.keys()):
        del Dictionary[num_to_be_del]

def UpdatePlayer():
    old_num = GetInput('Enter a jersey number:\n', range(0,100))
    if old_num in list(Dictionary.keys()):
        now = GetInput('Enter a new rating for player:\n', range(1,10))
        Dictionary[old_num] = now

def OutputAbove():
    ShowInOrder(GetInput('Enter a rating:\n', range(1,10)))

def ShowMENU():
    while True:
        print('\nMENU')
        print('a - Add player')
        print('d - Remove player')
        print('u - Update player rating')
        print('r - Output players above a rating')
        print('o - Output roster')
        print('q - Quit\n')
        option = input('Choose an option:')
        if option in list(MENU.keys()):
            exec(MENU[option])

for i in range(1,6):
    jersey_number = GetInput('Enter player %d\'s jersey number:\n'%i, range(0,100))
    rating = GetInput("Enter palyer %d's rating:\n"%i, range(1,10))
    Dictionary[jersey_number] = rating

ShowInOrder()
ShowMENU()