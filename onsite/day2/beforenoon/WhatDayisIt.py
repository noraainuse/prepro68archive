'''day'''
def main(x):
    '''main'''
    match x:
        case 1:
            print("day of week : Monday")
        case 2:
            print("day of week : Tuesday")
        case 3:
            print("day of week : Wednesday")
        case 4:
            print("day of week : Thursday")
        case 5:
            print("day of week : Friday")
        case 6:
            print("day of week : Saturday")
        case 7:
            print("day of week : Sunday")
        case _:
            print("day of week : Invalid")
main(int(input()))
