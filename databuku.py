def databuku(data):
    for i in data:
        for j in i:
            
            if type(j) is int:
                tahun = j
            
            elif j.isupper():
                penulis = j
            
            else:
                judul = j

        print(judul)
        print(tahun)
        print(penulis)
