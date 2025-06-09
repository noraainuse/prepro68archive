'''vowel'''

def vowel(text):
    '''vowel'''
    vv = ''
    for i in text:
        if i in('AEIOUaeiou'):
            vv += '*'
        else:
            vv += i
    return vv

def main():
    '''main'''
    text = str(input())
    print(vowel(text))

main()
