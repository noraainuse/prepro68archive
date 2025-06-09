'''crafterv1'''

def main():
    '''main'''
    #rub_input
    i_wii_wait = float(input())
    i_craft = float(input())
    stick = int(input())
    string = int(input())
    #kantum
    bow_stick = stick // 3
    bow_string = string // 3
    craft_dai = min(bow_stick, bow_string)
    #jacraftdaigian
    craft_time = i_wii_wait // i_craft
    total_bow = int(min(craft_dai, craft_time))
    #s
    grammar = "s" * (total_bow > 1)
    print(f'You can craft {total_bow} bow{grammar} within {i_wii_wait} seconds.')
main()
