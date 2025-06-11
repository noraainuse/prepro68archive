'''main'''
def main(h, w, hip, bday):
    '''main'''
    c1 = 155 <= h <= 165
    c2 = 22 <= w <= 24
    c3 = 34 <= hip < 36
    c4 = not bday % 2
    if c1 is True and c2 is True and c3 is True and c4 is True:
        print('"Yes, she is my specs."')
    else:
        print('"No, she isn\'t my specs."')
main(float(input()), float(input()), float(input()), int(input()))
