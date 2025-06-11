"""H"""
def main():
    """H"""
    Score = int(input())
    Titan = int(input())
    D = input()
    if (Titan >= 7 and D == "Yes") or (Score >= 80 and Titan > 5 and D == "Yes"):
        print("Scout Regiment")
    elif (Score >= 80 and Titan > 1 and D =="Yes"):
        print("Military Police Regiment")
    elif D == "Yes":
        print("Garrison Regiment")
    else:
        print("Training Corps")
main()
