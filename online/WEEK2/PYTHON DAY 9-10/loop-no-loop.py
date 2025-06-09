'''loop'''

def loop(start, stop, step):
    '''loop function'''
    if step > 0 and start < stop:
        x = step
        print(start)
        loop(start + x, stop, step)
    elif step < 0 and start > stop:
        y = step
        print(start)
        loop(start + y, stop, step)
    elif not step:
        print('Step must not be zero.')

def main():
    '''main'''
    start = int(input())
    stop = int(input())
    step = int(input())
    loop(start, stop, step)

main()
