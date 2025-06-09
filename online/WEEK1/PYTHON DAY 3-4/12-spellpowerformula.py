"""spellpowerformula"""


def main():
    """main"""
    magicname = str(input())
    s = float(input())#stable
    x = float(input())#magic circle
    m = float(input())#mana used
    a = float(input())#magic power
    c = float(input())#magic stack
    t1 = float(input())#magic casting
    t2 = float(input())#magic working time
    r = float(input())#magic shooting range
    d = float(input())#magic basic range

    for1 = s * x * (m**a)
    for2 = c * ((t1 + 1)**0.7) * (1 + t2) * (1 + r / d)
    w = for1 / for2
    print(f"Spell: {magicname}")
    print(f"Spell power (W) = {w:.2f}")


main()
