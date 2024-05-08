def hitung(dompet):
    uang = dict()
    total = 0

    for i in dompet:
        if i in uang.keys():
            uang[i] += 1
        else:
            uang[i] = 1
    
    for key, value in uang.items():
        print(f"{value} lembar senilai {key}")
        total += int(key[4:]) * value
    
    print()