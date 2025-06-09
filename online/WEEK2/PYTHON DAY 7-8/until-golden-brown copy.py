"""Until Godlen Brown"""

def golden(time):
    """status of chick function"""
    if time < 22:
        return "pale white"
    if time > 36:
        return "burnt"
    return "golden brown"

def main():
    """Untill golden brown function"""
    status = 0
    time = 0
    while True:
        action = input().lower()
        match action:
            case "wait":
                if status:
                    print("Invalid action, please try again.")
                else:
                    time += 5
                    print(f"It's {golden(time)}.")
            case "walk around":
                print("Time passes...")
                time += 10
                status = 1
            case "come back":
                if not status:
                    print("Invalid action, please try again.")
                else:
                    print(f"It's {golden(time)}.")
                    status = 0
            case "take out":
                if time > 36:
                    print("I'm never camping again...")
                    break
                if time >= 22 :
                    print("Success!")
                    break
                print("No way that's done, let's keep going.")
            case _:
                print("Invalid action, please try again.")

main()
