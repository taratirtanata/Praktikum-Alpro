def hapus(data, angka):
    akhir = []
    for i in data:
        if type(i) == tuple:
            a = list()

            for j in i:
                if j == angka:
                    continue
                else:
                    a.append(tuple(a))
            akhir.append(tuple(a))
        
        else:
            if i == angka:
                continue
            else:
                akhir.append(i)
    
    #balikin ke tuple lagi
    print(tuple(akhir))             