"""expandingcircle"""
def old_round(d):
    '''old'''
    return 3.14 * d

def new_round(oldround, r, t):
    '''new'''
    return oldround + (r * t)

def main():
    '''main'''
    t = float(input())
    d = float(input())
    r = float(input())
    oldround = old_round(d)
    newround = new_round(oldround, r, t)
    old_ratsame = d / 2
    new_ratsame = newround / (2 * 3.14)
    oldcir = 3.14 * (old_ratsame ** 2)
    newcir = 3.14 * (new_ratsame ** 2)
    result = newcir - oldcir
    print(f'{result:.3f}')

main()
