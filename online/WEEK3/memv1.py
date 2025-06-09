'''memv1'''

def find_my_iphone(text):
    '''change'''
    complete_text = ''
    for r in text:
        match r:
            case "a":
                complete_text += r.replace("a", "Mem")
            case "e":
                complete_text += r.replace("e", "Me")
            case "i":
                complete_text += r.replace("i", "Mi")
            case "o":
                complete_text += r.replace("o", "Mo")
            case "u":
                complete_text += r.replace("u", "Miu")
    if not text or not complete_text:
        return "Memi???"
    return complete_text
def main():
    '''main()'''
    mem_speak = input()
    print(find_my_iphone(mem_speak))
main()
