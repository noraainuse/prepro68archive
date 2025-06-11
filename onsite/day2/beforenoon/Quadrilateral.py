'''quad'''
def quad():
    '''quad'''
    AB = float(input())
    BC = float(input())
    CD = float(input())
    AD = float(input())
    A = float(input())
    B = float(input())
    C = float(input())
    D = float(input())
    if A + B + C + D != 360:
        print("Not a quadrilateral")
    elif (AB == BC == CD == AD) and (A == B == C == D):
        print("Square")
    elif ((AB == CD) or (AD == BC)) and A == B == C == D == 90:
        print("Rectangle")
    elif (AB == BC == CD == AD) and ((A == C) and (B == D)):
        print("Rhombus")
    elif ((AB == BC) and (CD == AD)) and ((A == C) and (B == D)):
        print("Parallelogram")
quad()
