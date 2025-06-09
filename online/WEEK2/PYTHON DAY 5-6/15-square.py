"""square"""

def main():
    """main"""
    sq_num = int(input())
    print("----------")
    for i in range(1, sq_num + 1):
        x = i**2
        print(f"{i} = {x}")
    print("----------")
main()
