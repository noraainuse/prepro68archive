'''actor'''
def oh_yi_young():
    '''yiyoung'''
    print("Go Youn-jung")
def pyo_nam_kyung():
    '''nam'''
    print("Shin Si-ah")
def kim_sa_bi():
    '''sabi'''
    print("Han Ye-ji")
def um_jae_il():
    "taelill"
    print("Kang You-seok")
def main():
    '''main'''
    match str(input()):
        case "yiyoung":
            oh_yi_young()
        case "namkyung":
            pyo_nam_kyung()
        case "sabi":
            kim_sa_bi()
        case "jaeil":
            um_jae_il()
        case _:
            print("No actor matched")
main()
