'''goldenbrown'''

def main():
    '''main'''
    total = 0
    check_walk_around = 0
    while True:
        action = str(input())
        status = ""
        food_check = 0
        food_try_out = 0
        match action:
            case "wait":
                if not check_walk_around:
                    total += 5
                    food_check = 1
                else:
                    food_check = 3
            case "walk around":
                total += 10
                check_walk_around = 1
                status += "Time passes..."
                food_check = 4
            case "come back":
                if check_walk_around == 1:
                    check_walk_around = 0
                    food_check = 1
                else:
                    food_check = 3
            case "take out":
                if not check_walk_around:
                    food_check = 2
                else:
                    food_check = 3
            case _:
                food_check = 3
        match food_check:
            case 1:
                if 22 < total < 36:
                    status = "golden brown."
                elif total > 36:
                    status = "burnt."
                elif total < 22:
                    status = "pale white."
                print(f"It's {status}")
            case 2:
                if 22 < total < 36:
                    food_try_out = "Success!"
                elif total > 36:
                    food_try_out = "I'm never camping again..."
                else:
                    print("No way that's done, let's keep going.")
            case 3:
                print("Invalid action, please try again.")
            case 4:
                print("Time passes...")
        if food_try_out in ('Success!', "I'm never camping again..."):
        #if food_try_out == "Success!" or food_try_out == "I'm never camping again...":
            print(food_try_out)
            break


main()
