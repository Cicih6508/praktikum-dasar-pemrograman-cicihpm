biaya_admin = 2500  
def hitung_total(harga):  
    total = harga + biaya_admin  
    return total
print(hitung_total(15000))


#by cici :
# Biaya Admin merupakan variabel global, sehingga dapat diakses di dalam fungsi hitung_total. 
# Harga merupakan parameter fungsi yang menerima nilai harga
# Total merupakan variabel lokal yang hanya dapat diakses di dalam fungsi