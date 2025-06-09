"""it's super effective"""

def main():
    """main"""
    #only_input
    poke_name = str(input())
    attack_move = str(input())
    attack_element = str(input())
    defend_element_1 = str(input())
    defend_element_2 = str(input())
    ef_power = 1.00
    #formula_x&y
    #match1
    match attack_element:
        case "Fire":
            if defend_element_1 == "Grass":
                ef_power *= 2.00
            elif defend_element_1 == "Fire" or defend_element_1 == "Water":
                ef_power *= 0.50
        case "Water":
            if defend_element_1 == "Fire":
                ef_power *= 2.00
            elif defend_element_1 == "Water" or defend_element_1 == "Grass":
                ef_power *= 0.50
        case "Electric":
            if defend_element_1 == "Water":
                ef_power *= 2.00
            elif defend_element_1 == "Electric" or defend_element_1 == "Grass":
                ef_power *= 0.50
        case "Grass":
            if defend_element_1 == "Water":
                ef_power *= 2.00
            elif defend_element_1 == "Fire" or defend_element_1 == "Grass":
                ef_power *= 0.50
        #match2
    if defend_element_1 != defend_element_2:
        match attack_element:
            case "Fire":
                if defend_element_2 == "Grass":
                    ef_power *= 2.00
                elif defend_element_2 == "Fire" or defend_element_2 == "Water":
                    ef_power *= 0.50
            case "Water":
                if defend_element_2 == "Fire":
                    ef_power *= 2.00
                elif defend_element_2 == "Water" or defend_element_2 == "Grass":
                    ef_power *= 0.50
            case "Electric":
                if defend_element_2 == "Water":
                    ef_power *= 2.00
                elif defend_element_2 == "Electric" or defend_element_2 == "Grass":
                    ef_power *= 0.50
            case "Grass":
                if defend_element_2 == "Water":
                    ef_power *= 2.00
                elif defend_element_2 == "Fire" or defend_element_2 == "Grass":
                    ef_power *= 0.50

    print(f"{poke_name} use {attack_move}!")
    if ef_power < 1.00:
        print("It's not very effective...")
    elif ef_power > 1.00:
        print("It's super effective!")
    print(f"Effectiveness x {ef_power:.2f}")


main()
