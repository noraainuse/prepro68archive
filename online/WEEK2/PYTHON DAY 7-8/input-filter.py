'''inputfilter'''

def main():
    '''main'''
    while True:
        text = str(input())
        match text:
            case "exit":
                print("The program has been stopped.")
                break
            case _:
                print(text)


main()
