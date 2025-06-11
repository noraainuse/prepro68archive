'''goldenspin'''
def main():
    '''main'''
    streak = 0
    while True:
        x = input()
        match x:
            case "Idle":
                pass
            case "Stop":
                break
            case _:
                print(type(x))
main()
