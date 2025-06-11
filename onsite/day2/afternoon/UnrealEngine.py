'''unreal'''
def main():
    '''main'''
    facing = 'North'
    x = float(0)
    y = float(0)
    while True:
        match str(input()):
            case "W":
                facing = 'North'
                y += 1
                print('X: 0.0, Y: 1.0')
            case "A":
                facing = 'West'
                x -= 1
                print('X: -1.0, Y: 0.0')
            case "S":
                facing = 'South'
                y -= 1
                print('X: 0.0, Y: -1.0')
            case "D":
                facing = 'East'
                x += 1
                print('X: 1.0, Y: 0.0')
            case "Done":
                break
    print(f'Position: {int(x), int(y)}')
    print(f'Facing: {facing}')
main()
