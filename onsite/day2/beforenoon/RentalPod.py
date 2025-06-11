'''nen'''
def nen(nen_know, leol_debt, dead_or_alive):
    '''nen'''
    c1 = nen_know == "Yes"
    c2 = leol_debt == "Yes"
    c3 = dead_or_alive == "Yes"
    if not c1:
        print("No ability information.")
    if not c2:
        print("Owner's confirmation is required.")
    if not c3:
        print("The owner's ability must be alive.")
    if c1 is True and c2 is True and c3 is True:
        print("Ability successfully added to Rental Pod.")
    else:
        print("Unsuccessful to add Ability.")
nen(str(input()), str(input()), str(input()))
