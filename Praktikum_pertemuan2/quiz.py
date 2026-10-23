usia = 20
memiliki_ktp = True
if usia >= 17:
    if memiliki_ktp:
        print("Anda dapat mendaftar sebagai pemilih.")
    else:
        print("Anda memenuhi syarat usia, namun KTP belum tersedia.")
else:
    print("Anda belum memenuhi syarat usia minimal.")