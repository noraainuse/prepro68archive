'''rockpaper'''
TURN = int(input())
NAME1 = str(input())
NAME2 = str(input())
NAME1_COUNTER = 0
NAME2_COUNTER = 0
#rock_paper
def winner_loser(name1action, name2action):
    match name1action:
        case "rock":
            if name2action == "scissors":
                print(f'{NAME1} wins')
            elif name2:
                print(f'{NAME2} wins')
        case "scissors":
            if name2action == "paper":
                print(f'{NAME1} wins')
            else:
                print(f'{NAME2} wins')
        case "paper":
            if name2action == "rock":
                print(f'{NAME1} wins')
            else:
                print(f'{NAME2} wins')

def main():
    for i in range(TURN):
        name1action = str(input())
        name2action = str(input())
        winner_loser(name1action, name2action)
main()