'''temp'''

def main():
    '''temp'''
    while True:
        temp = float(input())
        if temp <= 50:
            print("Temperature is normal.")
        else:
            print(f"Warning! Temperature too high: {temp}°C")
            break

main()
