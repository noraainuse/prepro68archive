'''delete-dash'''

def i_na_tood(text):
    '''remover'''
    x = text.startswith("-")
    if x is not False:
        return text[1::2]
    return text[::2]
def main():
    '''main'''
    text = str(input())
    print(i_na_tood(text))

main()
