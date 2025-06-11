'''stick'''
def main():
    '''main'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    for i in range(max(a,b,c,d,e,f,g), 0, -1):
        print(f'{' ' * (i - 1)}*')
main()
