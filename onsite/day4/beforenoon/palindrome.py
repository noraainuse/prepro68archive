'''palindrome'''
def palin(text):
    '''main'''
    if text[::-1] == text:
        print("Yes")
    else:
        print("No")
palin(str(input()).lower())
