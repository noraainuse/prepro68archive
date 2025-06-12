'''longlong'''
def main(m, oil):
    '''main'''
    x,y = m.find("C"),m.find("P")
    i_move = abs(x - y)
    if oil >= i_move:
        print("Possible")
    else:
        print("Impossible")
main(str(input()), int(input()))
