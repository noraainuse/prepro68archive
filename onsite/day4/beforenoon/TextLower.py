'''textlower'''
def text_lower(txt):
    '''main'''
    if txt.isalpha() is True:
        print('Result:', txt.lower())
    else:
        print("The text contains non-alphabetic characters")
text_lower(input())
