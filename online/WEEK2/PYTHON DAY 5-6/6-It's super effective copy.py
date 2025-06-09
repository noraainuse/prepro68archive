'''It's_super_effective'''

def element():
    '''pokemon'''
    name = input()
    ult = input()
    ele = input()
    el1 = input()
    el2 = input()

    def mul(att, de):
        result = 1
        if att == "Fire":
            if de in ("Fire", "Water"):
                result = 0.5
            elif de == "Grass":
                result = 2
        elif att == "Water":
            if de in ("Water", "Grass"):
                result = 0.5
            elif de == "Fire":
                result = 2
        elif att == "Electric":
            if de in ("Electric", "Grass"):
                result = 0.5
            elif de == "Water":
                result = 2
        elif att == "Grass":
            if de in ("Grass", "Fire"):
                result = 0.5
            elif de == "Water":
                result = 2
        return result

    if el1 == el2:
        total = mul(ele, el1)
    else:
        total = mul(ele, el1) * mul(ele, el2)

    print(f"{name} use {ult}!")
    if total > 1:
        print("It's super effective!")
    elif total < 1:
        print("It's not very effective...")
    print(f"Effectiveness x {total:.2f}")
element()
