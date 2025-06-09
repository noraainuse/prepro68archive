'''defined-function'''
TEXT = str(input())
def wrapping(message):
    '''return_message'''
    return "<" + message + "_>"

def looping(wrapped_text):
    '''loop_the_text'''
    for i in range(4):
        print(wrapped_text + " " + str(i))

def welcome():
    '''print_welcome'''
    print("Welcome To AIT03 ,DSBA09 ,IT23")

def main():
    '''main'''
    wrapped = wrapping(TEXT)
    looping(wrapped)
    welcome()

main()
