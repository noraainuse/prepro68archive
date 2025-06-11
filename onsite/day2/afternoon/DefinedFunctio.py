'''loop'''
def wrapping(t):
    '''wrapping'''
    return f'<{t}_>'
def looping(t):
    '''looping'''
    for i in range(4):
        print(t, i)
def welcome():
    '''welcome'''
    print("Welcome To AIT03, DSBA09, IT23")
def main():
    '''main'''
    looping(wrapping(str(input())))
    welcome()
main()
