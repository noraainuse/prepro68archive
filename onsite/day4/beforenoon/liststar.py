'''star'''
def star(t):
    '''main'''
    x = t.startswith("A") or t.startswith("a")
    match x:
        case True:
            print(t.capitalize())
        case False:
            print(t.lower())
star(input())
