'''count'''

def main():
    '''chars'''
    text = str(input())
    seen = ''
    for ch in text:
        if ch not in seen:
            count = text.count(ch)
            print(f'{ch} = {count}')
            seen += ch


main()
