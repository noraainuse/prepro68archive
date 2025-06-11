'''steak'''
def main(temp, time):
    '''main'''
    text = ''
    if temp > 80 or time > 20:
        text = 'Burnt'
    elif temp > 69 and time > 10:
        text = 'Well Done'
    elif 64 <= temp <= 68 and 8 <= time <= 9:
        text = 'Medium Well'
    elif 58 <= temp <= 63 and 6 <= time <= 7:
        text = 'Medium'
    elif 53 <= temp <= 57 and 4 <= time <= 5:
        text = 'Medium Rare'
    elif 48 <= temp <= 52 and 2 <= time <= 3:
        text = 'Rare'
    elif temp < 48 or time < 2:
        text = 'Raw'
    else:
        text = 'In between levels — might be under or overcooked'
    print(f'Steak doneness level: {text}')
main(float(input()), float(input()))
