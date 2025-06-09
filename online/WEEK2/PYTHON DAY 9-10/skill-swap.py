'''skillswap'''
#global_input
POKE = str(input())

def skill_swap(poke1, poke2):
    '''skill_swap'''
    return f'Rachata| {poke2} vs {poke1} |Guest'

def main():
    '''main'''
    poke1, _, poke2 = POKE.partition(' ')
    print(skill_swap(poke1, poke2))
main()
