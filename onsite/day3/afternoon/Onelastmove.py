'''nahiwouldwin'''
def fire_dragon():
    '''a'''
    print("You used Fire Dragon!")
def thunder_blade():
    '''b'''
    print("You used Thunder Blade!")
    return 250
def shadow_fang_slash():
    '''c'''
    print("You used Shadow Fang Slash!")
def main():
    '''main'''
    move = str(input())
    win = False
    dealt = 0
    print("The Demon Lord is almost defeated!")
    print("You only have enough mana for one final move.")
    match move:
        case "Fire Dragon":
            fire_dragon()
            win = True
        case "Thunder Blade":
            dealt = thunder_blade()
        case "Shadow Fang Slash":
            shadow_fang_slash()
            win = True
        case _:
            print("You hesitated too long... The Demon Lord strikes back!")
    match win:
        case True:
            print("You win! The Demon Lord has been defeated!")
        case False:
            print(f"You dealt {dealt} damage... Not enough. The Demon Lord counterattacks!")
main()
