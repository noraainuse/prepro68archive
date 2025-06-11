'''toktok'''
def plus_time():
    '''time'''
    time_def = 0
    for _ in range(12):
        match input():
            case "Scroll":
                time_def += 2
            case "Live":
                time_def += 5
    if time_def >= 60:
        print(f'Using {time_def // 60} hour on TokTok')
    elif time_def > 0:
        print(f'Using {time_def} minutes on TokTok')
    elif not time_def:
        print('-1')
plus_time()
