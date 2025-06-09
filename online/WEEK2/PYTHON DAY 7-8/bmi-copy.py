"""bmi calculator"""
def main():
    """calculation"""

    while True:
        weight = float(input())
        height = float(input())

        if weight > 0 and height > 0:
            break
        print("Weight and height must be positive numbers. Please try again")

    bmi = weight / pow((height/100), 2)

    if bmi < 18.5:
        category = "Underweight"
        risk = "Higher than normal"
    elif bmi <= 22.99:
        category = "Normal (Healthy)"
        risk = "Average (normal risk)"
    elif bmi <= 24.99:
        category = "Overweight / Obesity Level 1"
        risk = "Increased risk (Level 1)"
    elif bmi <= 29.99:
        category = "Obese / Obesity Level 2"
        risk = "High risk (Level 2)"
    else:
        category = "Severely obese / Obesity Level 3"
        risk = "Very high risk (Level 3)"

    print(f"Your BMI is {round(bmi, 2)}")
    print(f"Category: {category}")
    print(f"Health Risk: {risk}")

main()
