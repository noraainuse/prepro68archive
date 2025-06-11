'''logi'''
def main(p, q):
    '''main'''
    p = p == "True"
    q = q == "True"
    or_check = p or q
    and_check = p and q
    impl = not(p) or q
    bic = p == q
    print(f'p: {p} q: {q}')
    print(f'p ∨ q: {or_check}')
    print(f'p ∧ q: {and_check}')
    print(f'p → q: {impl}')
    print(f'p ↔ q: {bic}')
main(str(input()), str(input()))
