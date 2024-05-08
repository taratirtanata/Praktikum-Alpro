def hitung(buku):
    book = dict()
    total = 0

    for i in buku:
        if i in book.keys():
            book[i] += 1
        else:
            book[i] = 1
        total += 1
    
    for key, value in book.items():
        print(f"Buku dengan judul {key} sejumlah {value} buku")
