'''wish'''

def wish(x):
    '''wish'''
    y = ''
    if x >= 1000000:
        y = 'BYD SEAL.'
    elif 100000 <= x < 1000000:
        y = 'Capybara.'
    elif 50000 <= x < 100000:
        y = 'Huawei Matebook X Pro (Harmony OS Next).'
    elif 35000 <= x < 50000:
        y = 'Nvidia Geforce RTX5070Ti.'
    elif 30000 <= x < 35000:
        y = 'Xiaomi 15 Pro.'
    elif 25000 <= x < 30000:
        y = 'Luxury meal.'
    elif 0 < x < 25000:
        y = 'Gold Coin or Huawei Watch.'
    if x > 0:
        print(f"For a salary of {x:,} Baht, P'Aung will buy a {y}")
    elif not x:
        print("P'Aung is unemployed, so he plans to apply for the Taiwan Government Scholarship"
        " (MOE) to pursue a Master's degree instead.")
    elif x < 0:
        print("Invalid Input")

wish(int(input()))
