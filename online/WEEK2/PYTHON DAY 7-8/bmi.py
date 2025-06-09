'''bmi'''
import math

def main():
    '''main'''
    while True:
        weight = 0
        height = 0
        weight = float(input())
        height = float(input())
        if weight >= 0 and height >= 0:
            break
        else:
            print("Weight and height must be positive numbers. Please try again")
    after_cal = height / 100
    bmi = weight / math.pow(after_cal, 2)
    print(f'Your BMI is {bmi:.2f}')
    if bmi > 30:
        print("Category: Severely obese / Obesity Level 3")
        print("Health Risk: Very high risk (Level 3)")
    elif 25.00 < bmi < 29.99:
        print("Category: Obese / Obesity Level 2")
        print("Health Risk: High risk (Level 2)")
    elif 23.00 < bmi < 24.99:
        print("Category: Overweight / Obesity Level 1")
        print("Health Risk: Increased risk (Level 1)")
    elif 18.50 < bmi < 22.99:
        print("Category: Normal (Healthy)")
        print("Health Risk: Average (normal risk)")
    else:
        print("Category: Underweight")
        print("Health Risk: Higher than normal")

main()
