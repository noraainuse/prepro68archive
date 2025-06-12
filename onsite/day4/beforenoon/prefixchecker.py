'''prefix'''
def main(text, check_this):
    '''main'''
    x = text.startswith(check_this)
    match x:
        case True:
            print("Yes")
        case False:
            print("No")
main(input(), input())
