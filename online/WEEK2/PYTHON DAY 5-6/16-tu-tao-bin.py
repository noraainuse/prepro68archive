"""tutaobin"""

def main():
    """main"""
    needed_time = int(input())
    limit_time = int(input())
    x = 0
    for _ in range(limit_time):
        test_word = str(input())
        if test_word == "espresso":
            x += 1
        else:
            x += 0

    if x == needed_time:
        print("Tao Bin Activate!!!")
    else:
        print("Failed to Activate")


main()
