"""triangletype"""

def main():
    """main"""
    ab = float(input())
    bc = float(input())
    ca = float(input())
    if ab == bc == ca:
        print("Equilateral Triangle")
    elif ab == bc or bc == ca or ab == ca:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")


main()
