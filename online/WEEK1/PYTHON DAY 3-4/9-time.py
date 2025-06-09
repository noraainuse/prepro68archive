"""time"""


def convert_time_to_hour_month_second():
    """main"""
    secinp = int(input())
    h = secinp // 3600
    mm = (secinp % 3600) // 60
    ss = secinp % 60
    print(f"{h:01d}:{mm:02d}:{ss:02d}")


convert_time_to_hour_month_second()
