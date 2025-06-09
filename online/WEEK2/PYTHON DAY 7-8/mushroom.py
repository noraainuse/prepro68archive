"""mushroom"""

def main():
    """main"""
    round_count = 1
    lightest = None
    heaviest = None
    x_input = 0
    while True:
        mushroom_input = input()
        match mushroom_input:
            case "End":
                if round_count == "1":
                    print("No mushroom today.")
                    break
                else:
                    avg_weight = x_input / round_count
                    print(f"{avg_weight}")
            case _:
                # round_count += 1
                mushroom_input = float(mushroom_input)
                x_input += mushroom_input


main()
