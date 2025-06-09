'''temperature'''

def cel_to_fah(d):
    '''ctf'''
    return d * (9 / 5) + 32

def cel_to_kel(d):
    '''ctk'''
    return d + 273.15

def fah_to_cel(d):
    '''ftc'''
    return (5 / 9) * (d - 32)

def fah_to_kel(d):
    '''ftk'''
    return (d + 459.67) * (5 / 9)

def kel_to_cel(d):
    '''ktc'''
    return d - 273.15

def kel_to_fah(d):
    '''ktf'''
    return 1.8 * (d - 273.15) + 32

def main():
    '''main'''
    temp = float(input())
    degree = str(input())
    x = 0
    y = 0
    match degree:
        case "Celsius":
            x = f'Fahrenheit = {cel_to_fah(temp):.2f}'
            y = f'Kelvin = {cel_to_kel(temp):.2f}'
        case "Fahrenheit":
            x = f'Celsius = {fah_to_cel(temp):.2f}'
            y = f'Kelvin = {fah_to_kel(temp):.2f}'
        case "Kelvin":
            x = f'Celsius = {kel_to_cel(temp):.2f}'
            y = f'Fahrenheit = {kel_to_fah(temp):.2f}'
    print(x)
    print(y)

main()
