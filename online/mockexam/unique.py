'''string'''
def i_score(score):
    '''score'''
    if 80 <= score <= 100:
        return 'Grade: A'
    elif 75 <= score <= 79:
        return 'Grade: B+'
    elif 70 <= score <= 74:
        return 'Grade: B'
    elif 65 <= score <= 69:
        return 'Grade: C+'
    elif 60 <= score <= 64:
        return 'Grade: C'
    elif 55 <= score <= 59:
        return 'Grade: D+'
    elif 50 <= score <= 54:
        return 'Grade: D'
    elif 0 <= score <= 49:
        return 'Grade: F'
    else:
        return 'Grade: Incorrect score'

def main():
    '''main'''
    receive_score = int(input())
    print(i_score(receive_score))
main()
