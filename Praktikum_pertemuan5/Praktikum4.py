def buat_biodata(nama, umur, jurusan):
    print("Nama    :", nama)
    print("Umur    :", umur)
    print("Jurusan :", jurusan) 

print("--- Positional argument ---")
buat_biodata("Cicih Paramita", 18, "Sistem Informasi")
print("--- Keyword argument ---")
buat_biodata(jurusan="Sistem Informasi", nama="Cicih Paramita", umur=18)