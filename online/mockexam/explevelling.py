'''explevelling'''

def exp_cal(lvl, player_exp, receive_exp):
    '''exp'''
    exp_capacity = (lvl / 2) * 1000
    show = exp_capacity + 500
    print(f'Level: {lvl+1}')
    print(f'EXP: {exp_capacity:.0f}/{show:.0f}')
def main():
    '''main'''
    lvl = int(input())
    player_exp = int(input())
    receive_exp = int(input())
    exp_cal(lvl, player_exp, receive_exp)

main()
