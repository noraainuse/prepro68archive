"""lowest_"""

def highest(current_max, new_value):
    '''max_checker'''
    if new_value > current_max:
        return new_value
    return current_max

def lowest(current_min, new_value):
    '''min_checker'''
    if new_value < current_min:
        return new_value
    return current_min

def display_result(high, low):
    '''display'''
    print('max:', high)
    print('min:', low)
    print('-----')

def main():
    '''main'''
    #ใช้รอบเดียวพอบักตูด
    first_number = int(input())
    now_max = first_number
    now_min = first_number

    while True:
        inputer = input()
        #exit point
        if inputer == "exit":
            print('Program ended')
            break
        number = int(inputer)
        now_max = highest(now_max, number)
        now_min = lowest(now_min, number)
        display_result(now_max, now_min)

main()
