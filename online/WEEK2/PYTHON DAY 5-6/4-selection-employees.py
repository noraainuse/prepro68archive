"""selectionemployees"""


def main():
    """main"""
    name = str(input())
    age = int(input())
    exp = int(input())
    if age > 60:
        pension = exp * 15000
        print(f"Mr./Miss. {name} has been retired.")
        print(f"The amount of pension is {pension:,} Baht.")
    elif age <= 60:
        print(f"Mr./Miss. {name} has been working for {exp} year/years.")


main()
