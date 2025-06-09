'''charcheck'''
def check_and_format(ip):
    '''check_and_text'''
    numror = ip.isnumeric()
    match numror:
        case True:
            return "This is a number"
        case False:
            if ip.isalpha() is True:
                if ip.islower() is True:
                    return "All lowercase letters"
                if ip.isupper() is True:
                    return "All uppercase letters"
                return "Mixed case letters"
            return "Invalid input"

def main():
    '''main'''
    ip = str(input())
    print(check_and_format(ip))
main()
