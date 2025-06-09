'''mario'''
def mushroom_or_enemy(letter, checkcase):
    '''mushroom'''
    y = ''
    match checkcase:
        case "Mushroom":
            for i in letter:
                if i in '012345678':
                    x = str(int(i) + 1)
                    y += x
                else:
                    y += i
            return y.upper()
        case "Enemy":
            for i in letter:
                if i in '0123456789':
                    if i == '0':
                        y += ''
                    else:
                        x = str(int(i) - 1)
                        y += x
                elif i.isupper() is True:
                    y += str(i.lower())
                elif i.islower() is True:
                    y = y + ''
                else:
                    y = y + str(i)
            return y

def main():
    '''main'''
    letter = input()
    checkcase = input()
    print(mushroom_or_enemy(letter, checkcase))
main()
