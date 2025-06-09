"""thaismilebusv1"""

def buscal():
    """buscal"""
    #-----input-----
    busrange = float(input())
    upstop = int(input())
    downstop = int(input())
    age = int(input())
    #formula&output
    brus = busrange * (downstop - upstop)
    if age < 12:
        print("Payment: FREE")
    elif age >= 12 and brus < 6:
        print("Payment: 15 THB")
    elif age >= 12 and 6 < brus < 18:
        print("Payment: 20 THB")
    elif age >= 12 and brus > 18:
        print("Payment: 25 THB")

buscal()
