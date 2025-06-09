"""table"""

def main():
    """main"""
    mae_sout_kon = int(input())
    for i in range(1, 13):
        mae_mutil = mae_sout_kon * i
        if i < 10:
            print(f"{mae_sout_kon} x {i}  = {mae_mutil}")
        else:
            print(f"{mae_sout_kon} x {i} = {mae_mutil}")


main()
