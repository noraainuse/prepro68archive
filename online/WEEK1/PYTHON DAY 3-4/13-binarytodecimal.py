"""binarytodecimal"""


def main():
    """main"""
    #ip
    w1 = int(input())
    w2 = int(input())
    w3 = int(input())
    w4 = int(input())
    w5 = int(input())
    w6 = int(input())
    w7 = int(input())
    w8 = int(input())
    w9 = int(input())
    w10 = int(input())
    #fml
    linebin = (str(w1) + str(w2) + str(w3) + str(w4) + str(w5) + str(w6)
    + str(w7) + str(w8) + str(w9) + str(w10))
    linedec = ((w1 * 2**9) + (w2 * 2**8) + (w3 * 2**7) + (w4 * 2**6) + (w5 * 2**5)
    + (w6 * 2**4) + (w7 * 2**3)+ (w8 * 2**2) + (w9 * 2**1) + (w10 * 2**0))
    #op
    print(f"Binary number: {linebin}")
    print(f"Calculated decimal value: {linedec}")


main()
