def bosan(daftar):
    for x, y in enumerate(daftar):
        try:
            print(y[-1-x], end='')
        except:
            print('x', end='')




# Deskripsi
# Kebosanan Henry belum juga hilang. Dia menuliskan daftar nama teman-temannya lalu memasukkannya ke dalam tuple. Henry ingin mengambil 1 karakter dari paling belakang dari setiap nama tersebut. Dia juga ingin menggeser indeksnya kekiri setiap kali namanya berganti. Henry juga sadar akan ada kondisi dimana nama pergeserannya terlalu banyak sehingga akan menghasilkan IndexError, Henry ingin saat kondisi tersebut terjadi karakter yang diambil diganti menjadi ‘x’.Bantulah Henry untuk membuat fungsi bosan(daftar)  yang memenuhi kondisi tersebut.

# Contoh
# Pemanggilan:

# data = ("Yusta", "Anbu", "Acen", "Dori")

# bosan(daftar)

# Output:

# abcD

 

# Penjelasan:

# a -> index terakhir

# b -> index sebelum terakhir

# dst.

# Pemanggilan:

# data = ("Yusta", "Cindy", "Claresta", "Elisabeth", "Agustin", "Anastasya", "Wijaya")

# bosan(daftar)

# Output:

# adsbusx

 

# Penjelasan:

# x -> pergeseran index terlalu banyak sehingga keluar dari nama menghasilkan IndexError

 

 

# Batasan
# Fungsi anda tidak perlu return, lakukan print() di dalam fungsi.

# Output berupa string

# Format data berupa tuple of string.      


# For example:

# Test	Result
# daftar = ("Yusta", "Monic", "Claresta", "Elisabeth", 
# "Agustin", "Anastasya", "Wijaya")
# bosan(daftar)
# aisbusx
