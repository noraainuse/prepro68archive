'''blind'''
def main(x,y,could_move):
    '''main'''
    xone,yone = x,y
    for _ in range(could_move):
        checker = input().lower()
        match checker:
            case "n":
                yone += 1
            case "s":
                yone -= 1
            case "e":
                xone += 1
            case "w":
                xone -= 1
            case "r":
                xone,yone = x,y
    print(xone)
    print(yone)
main(int(input()),int(input()),int(input()))
