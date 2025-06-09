"""main"""

def shabu_calculator():
    """main"""
    #input
    people_count = int(input())
    membership = str(input())
    birthday = str(input())
    all_cost = 0
    people_countd = 0
    #formula
    if membership == "yes":
        cost_per_people = 300
    else:
        cost_per_people = 399
    if people_count >= 4:
        people_countd = people_count // 4
        people_count_price = people_count - people_countd
        all_cost = people_count_price * cost_per_people
    else:
        all_cost = cost_per_people * people_count
    if birthday == "yes":
        all_cost = all_cost * 0.90
    if membership == "yes" and people_count >= 4 and birthday == "yes":
        print("Your promotions: Member discount: 300 Baht per person | " \
                  "Come 4 people, pay for only 3 people | Birthday discount: 10% off")
    elif membership == "yes" and people_count >= 4 and birthday == "no":
        print("Your promotions: Member discount: 300 Baht per person | " \
                  "Come 4 people, pay for only 3 people")
    if membership == "no" and people_count >= 4 and birthday == "yes":
        print("Your promotions: Come 4 people, pay for only 3 people | " \
            "Birthday discount: 10% off")
    elif membership == "yes" and people_count < 4 and birthday == "yes":
        print("Your promotions: Member discount: 300 Baht per person | " \
            "Birthday discount: 10% off")
    elif membership == "yes" and people_count < 4 and birthday == "no":
        print("Your promotions: Member discount: 300 Baht per person")
    elif membership == "no" and people_count < 4 and birthday == "yes":
        print("Your promotions: Birthday discount: 10% off")
    elif membership == "no" and people_count >= 4 and birthday == "no":
        print("Your promotions: Come 4 people, pay for only 3 people")
    print(f"Total amount to pay: {all_cost} Baht")


shabu_calculator()
