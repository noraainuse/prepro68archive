'''goldenspin'''
def main():
    '''main'''
    streak = 0
    while True:
        x = input()
        match x:
            case "Idle":
                streak = 0
                print("Waiting for the next Spin.")
            case "Stop":
                break
            case _:
                if 1.617 < float(x) < 1.619:
                    streak += 1
                    if streak >= 4:
                        print("Steel Ball Run! Golden Spin!")
                    else:
                        print("Spin... and keep spinning.")
                else:
                    streak = 0
                    print("That’s not the true Spin... Try again!")
main()
