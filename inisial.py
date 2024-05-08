def inisial(daftar):
    nama = dict()
    
    for i in daftar:
        if i[0] in nama.keys():
            nama[i[0]] += 1
            print(f"{i}{nama[i[0]]}")
        else:
            nama[i[0]] = 1
            print


#daftar = ('michael', 'minie', 'miboli', maxine')
            
#outputnya bakal:
            #michael
            #minie2
            #miboli3
            #maxine4