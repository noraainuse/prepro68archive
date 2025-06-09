'''cronym'''

def to_acro(sentence):
    '''acronym'''
    first, _, after = sentence.partition(" ")
    second, _, third = after.partition(" ")
    return (first[0] + second[0] + third[0]).upper()
def main():
    '''main'''
    sentence = str(input())
    print(to_acro(sentence))
main()
