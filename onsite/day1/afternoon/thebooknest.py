'''book'''
def book_nest(nv_price, nv_count, doc_price, doc_count):
    '''nest'''
    total_bf = (nv_price * nv_count) + (doc_price * doc_count)
    vat = total_bf * (0.07)
    print(f'Price for novel books: {(nv_price * nv_count):.2f} baht')
    print(f'Price for documentary books: {(doc_price * doc_count):.2f} baht')
    print(f'Total price before VAT: {total_bf:.2f} baht')
    print(f'VAT (7%): {vat:.2f} baht')
    print(f'Total price after VAT: {(total_bf + vat):.2f} baht')
book_nest(float(input()), int(input()), float(input()), int(input()))
