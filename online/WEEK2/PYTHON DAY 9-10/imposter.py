'''imposter'''

def nah_i_would_find(text):
    '''finder'''
    position = text.find("q")
    match position:
        case -1:
            return "There are no imposters."
        case _:
            return f'There is an imposter at position {position + 1}.'

def main():
    '''main'''
    text = str(input())
    print(nah_i_would_find(text))

main()
