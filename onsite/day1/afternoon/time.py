'''clock'''
def clock(sec_in):
    '''clock'''
    h = sec_in // 3600
    mm = (sec_in % 3600) // 60
    ss = sec_in % 60
    print(f'{h:01d}:{mm:02d}:{ss:02d}')
clock(int(input()))
