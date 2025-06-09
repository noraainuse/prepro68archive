'''parkingfee'''

def main():
    '''main'''
    hour = int(input())
    minute = int(input())
    if minute > 0:
        hour += 1
    if hour >= 0 and minute >= 0:
        price = (hour * 30) - 30
        print(price)
    else:
        print("โปรดใส่ข้อมูลที่ไม่ติดลบ")


main()
