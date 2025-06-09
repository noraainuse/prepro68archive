'''evaluator'''
#คลาสกระจอก
def base_class(s, i, a, v):
    '''base'''
    r_base = ''
    c = 0
    if s >= 10 and v >= 8:
        c += 1
        r_base += 'Swordsman'
    if i >= 10:
        if not c:
            c += 1
            r_base += 'Mage'
        else:
            c += 1
            r_base += ' or Mage'
    if a >= 10:
        if not c:
            c += 1
            r_base += 'Thief'
        else:
            c += 1
            r_base += ' or Thief'
    if i >= 8 and v >= 8:
        if not c:
            c += 1
            r_base += 'Acolyte'
        else:
            c += 1
            r_base += ' or Acolyte'
    return r_base

#โดนยิงหัวที่ mid ด่าน asecnt
def mid_tier_class(s, i, a, v):
    '''mid-tier'''
    m_base = ''
    c = 0
    if s >= 20 and v >= 15:
        c += 1
        m_base += 'Knight'
    if i >= 20:
        if not c:
            c += 1
            m_base += 'Wizard'
        else:
            c += 1
            m_base += ' or Wizard'
    if a >= 20:
        if not c:
            c += 1
            m_base += 'Assassin'
        else:
            c += 1
            m_base += ' or Assassin'
    if i >= 15 and v >= 15:
        if not c:
            c += 1
            m_base += 'Priest'
        else:
            c += 1
            m_base += ' or Priest'
    return m_base

#ชนชั้นสูง
def high_tier_class(s, i, a, v):
    '''high-tier'''
    h_base = ''
    c = 0
    if s >= 50 and v >= 45:
        c += 1
        h_base += 'Lord Knight'
    if i >= 50:
        if not c:
            c += 1
            h_base += 'High Wizard'
        else:
            c += 1
            h_base += ' or High Wizard'
    if a >= 50:
        if not c:
            c += 1
            h_base += 'Guillotine Cross'
        else:
            c += 1
            h_base += ' or Guillotine Cross'
    if i >= 45 and v >= 45:
        if not c:
            c += 1
            h_base += 'High Priest'
        else:
            c += 1
            h_base += ' or High Priest'
    return h_base

def stat_print(s, i, a, v):
    '''stat'''
    print(f'str {s}')
    print(f'int {i}')
    print(f'agi {a}')
    print(f'vit {v}')

def main():
    """main"""
    s = int(input())
    i = int(input())
    a = int(input())
    v = int(input())
    print('=== Your Stats ===')
    stat_print(s, i, a, v)
    print('=== Class Evaluation Result ===')
    x = base_class(s, i, a, v)
    if not x:
        print('You are still a Novice. Keep training!')
    else:
        print(f'You are eligible for base class: {x}')
    y = mid_tier_class(s, i, a, v)
    if y:
        print(f'You are eligible for mid-tier class: {y}')
    z = high_tier_class(s, i, a, v)
    if z:
        print(f'You are eligible for high-tier class: {z}')

main()
