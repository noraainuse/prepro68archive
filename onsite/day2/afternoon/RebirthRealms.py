'''magic'''
def magic_world():
    '''a'''
    print("You are reborn in a magical world. Magic flows through your veins!")
    return "Arcane Dominion"
def sci_fi_world():
    '''b'''
    print("You awaken in a futuristic tech world, surrounded by spaceships and robots!")
    return "Neon Nexus"
def anime_game_world():
    '''c'''
    print("You become the protagonist of a cartoon or game, ready for your adventure!")
    return "Pixel Realm"
def wuxia_world():
    '''d'''
    print("You awaken in a world of martial arts, "
          "ancient clans, and hidden techniques. The path of the sword awaits you!")
    return "Jianghu Eternal"
def past_with_memory():
    '''tt'''
    print("You return back in time with all your memories. Ready to change your fate!")
    return "Chrono Veil"
def main():
    '''main'''
    match str(input()):
        case "1":
            print(f'Your new world is: {magic_world()}')
        case "2":
            print(f'Your new world is: {sci_fi_world()}')
        case "3":
            print(f'Your new world is: {anime_game_world()}')
        case "4":
            print(f'Your new world is: {wuxia_world()}')
        case "5":
            print(f'You have returned to: {past_with_memory()}')
        case _:
            print("You chose no path, and "
                  "thus the currents of fate have carried you to eternal cleansing...")
main()
