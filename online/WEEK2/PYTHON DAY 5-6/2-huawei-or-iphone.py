"""huaweioriphone"""

def main():
    """main"""
    #ip
    name = str(input())
    snum = int(input())
    #fml
    sresult = snum
    if not sresult % 2:
        ooe = str("Even")
    else:
        ooe = str("Odd")
    print(f"{snum} is {ooe}.")
    match ooe:
        case "Even":
            print(f"Congratulations!! {name} got Huawei Pura X.")
        case "Odd":
            print(f"Sadness!! {name} got iPhone 16 Pro Max.")


main()
