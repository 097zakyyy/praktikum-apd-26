print("===LOGIN RENTAL PS ===")
nama = input("Masukkan Nama: ")
nim = input("Masukkan 2/3 digit terakhir NIM: ")

if nama =="iqbal" and nim == "104":
    print("Login berhasil")
    print("")
    
    
    print("===PILIHAN KONSOL===")
    print("1. PS4 = Rp 10000/jam")
    print("2. PS4 Pro = Rp 15000/jam")
    print("3. PS5 = Rp 20000/jam")
    pilihan = int(input("Pilih konsol (1-3): "))
    
    if pilihan == 1:
        konsol = "PS4"
        harga_per_jam = 10000
    elif pilihan == 2:
        konsol = "PS4 PRO"
        harga_per_jam = 15000
    elif pilihan == 3:
        konsol = "PS5"
        harga_per_jam = 20000
    else :
        print("pilih yang betul")
        
    jam = int(input("Sewa Berapa Jam:"))
    
    total_harga = harga_per_jam *jam
    
    if jam >= 5:
        diskon = int(0.08 * total_harga)
    elif jam >= 3:
        diskon = int(0.05 * total_harga)
    else:
        diskon = 0
    
    waktu = input("main saat weekend atau weekdays: ")
    
    if waktu =="weekend":
        biaya_weekend = int(0.10 *total_harga)
    else:
        biaya_weekend = 0
    
    total_bayar = total_harga - diskon + biaya_weekend
    
    print("")
    print("==============================")
    print("      STRUK PENYEWAAN PS")
    print("==============================")
    print("Nama          :", nama)
    print("NIM           :", nim)
    print("Jenis konsol  :", konsol)
    print("Jumlah jam    :", jam)
    print("Waktu sewa    :", waktu)
    print("------------------------------")
    print("Total harga   : Rp", total_harga)
    print("Diskon durasi : Rp", diskon)
    print("Biaya weekend : Rp", biaya_weekend)
    print("------------------------------")
    print("Total bayar   : Rp", total_bayar)
    print("==============================")

else:
    print("Login gagal, program berhenti")
        