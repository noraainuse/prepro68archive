'''essay'''
def es_check(text):
    '''essay checker'''
    x = len(text) >= 300
    match x:
        case True:
            print("Essay is 300 characters or more.")
        case False:
            print("Please write more.")
es_check(input())
