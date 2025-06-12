'''prefix'''
def main(text, check_this):
    '''main'''
    x = text.endswith(check_this)
    match x:
        case True:
            print("Valid")
        case False:
            print("Invalid")
main(input(), input())
