import os

bersih = "cls" if os.name == "nt" else "clear"


pengguna = [
    ["admin", "admin123", "Admin"],
    ["zaky", "zaky", "Pengguna Biasa"],
]
patungan = []
id_berikut = 1
user_aktif = None


angka_valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} 


while True:
    os.system(bersih)
    print("=" * 45)
    print("   SISTEM KALKULATOR & PENDATAAN PATUNGAN")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih_awal = input("Pilih menu (1-3): ").strip()

    if pilih_awal == "2":
        os.system(bersih)
        print("=== REGISTER (Pengguna Biasa) ===")
        username_baru = input("Username baru : ").strip()
        if username_baru == "":
            print("Username tidak boleh kosong!")
            input("Tekan Enter untuk lanjut...")
            continue
  
        username_ada = set()
        for u in pengguna:
            username_ada.add(u[0].lower())
        if username_baru.lower() in username_ada:
            print("Username sudah dipakai!")
            input("Tekan Enter untuk lanjut...")
            continue
        password_baru = input("Password baru : ").strip()
        if len(password_baru) < 4:
            print("Password minimal 4 karakter!")
            input("Tekan Enter untuk lanjut...")
            continue
        pengguna.append([username_baru, password_baru, "Pengguna Biasa"])
        print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    elif pilih_awal == "1":
        percobaan = 0
        user_aktif = None
        while percobaan < 3 and user_aktif is None:
            os.system(bersih)
            print("=== LOGIN ===")
            input_user = input("Username : ").strip()
            input_pass = input("Password : ").strip()
            for u in pengguna:
                if u[0] == input_user and u[1] == input_pass:
                    user_aktif = u
            if user_aktif is None:
                percobaan = percobaan + 1
                print("Username/password salah! Sisa percobaan:", 3 - percobaan)
                input("Tekan Enter untuk lanjut...")
        if user_aktif is None:
            print("Login gagal 3 kali. Kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")
            continue

       
        while user_aktif is not None:
            os.system(bersih)
            print("=" * 45)
            print("Login sebagai:", user_aktif[0], "(" + user_aktif[2] + ")")
            print("=" * 45)
            print("1. Tambah data patungan")
            print("2. Tampilkan seluruh anggota")
            print("3. Tambah anggota")
            print("4. Kurangi kontribusi anggota")
            print("5. Hapus anggota")
            print("6. Hitung nominal patungan")
            print("7. Ubah data patungan (nama/total biaya)")
            print("8. Hapus data patungan")
            if user_aktif[2] == "Admin":
                print("9. Lihat daftar pengguna")
            print("0. Logout")
            menu = input("Pilih menu: ").strip()

       
            if menu == "1":
                os.system(bersih)
                print("=== TAMBAH DATA PATUNGAN ===")
                nama_kegiatan = input("Nama kegiatan       : ").strip()
                if nama_kegiatan == "":
                    print("Nama kegiatan tidak boleh kosong!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                teks = input("Total biaya (Rp)    : ").strip()
            
                angka = True
                for h in teks:
                    if h not in angka_valid:
                        angka = False
                if teks == "":
                    angka = False
                if angka == False:
                    print("Total biaya harus berupa angka!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                if int(teks) <= 0:
                    print("Total biaya harus lebih dari 0!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                anggota_baru = []
                nama_ada = set()   
                print("Masukkan nama anggota (kosongkan lalu Enter untuk selesai):")
                while True:
                    nama = input("Anggota " + str(len(anggota_baru) + 1) + " : ").strip()
                    if nama == "":
                        if len(anggota_baru) == 0:
                            print("Minimal 1 anggota!")
                            continue
                        break
                    if nama.lower() in nama_ada:
                        print("Nama sudah ada dalam daftar!")
                    else:
                        anggota_baru.append([nama, 0])
                        nama_ada.add(nama.lower())
                patungan.append([id_berikut, nama_kegiatan, int(teks), user_aktif[0], anggota_baru])
                id_berikut = id_berikut + 1
                print("Data patungan berhasil ditambahkan!")
                input("Tekan Enter untuk lanjut...")

         
            elif menu in ["2", "3", "4", "5", "6", "7", "8"]:
                os.system(bersih)
                terlihat = []
                for p in patungan:
                    if user_aktif[2] == "Admin" or p[3] == user_aktif[0]:
                        terlihat.append(p)
                if len(terlihat) == 0:
                    print("Belum ada data patungan.")
                    input("Tekan Enter untuk lanjut...")
                    continue
                print("=== DAFTAR PATUNGAN ===")
                for i in range(len(terlihat)):
                    print(str(i + 1) + ".", terlihat[i][1], "| Total Rp", terlihat[i][2], "| Pemilik:", terlihat[i][3])
                teks = input("Pilih nomor patungan: ").strip()
                angka = True
                for h in teks:
                    if h not in angka_valid:
                        angka = False
                if teks == "":
                    angka = False
                if angka == False:
                    print("Nomor patungan harus berupa angka!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                if int(teks) < 1 or int(teks) > len(terlihat):
                    print("Nomor patungan tidak ada!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                p = terlihat[int(teks) - 1]

          
                n = len(p[4])
                nominal = []
                total_pengurangan = 0
                dasar = 0
                if n > 0:
                    for a in p[4]:
                        total_pengurangan = total_pengurangan + a[1]
                    dasar = p[2] / n
                    for a in p[4]:
                        nominal.append(dasar - a[1] + total_pengurangan / n)


                hasil = {}
                for i in range(n):
                    hasil[p[4][i][0]] = round(nominal[i])

                os.system(bersih)

                if menu == "2":
                    print("=== ANGGOTA:", p[1], "===")
                    if n == 0:
                        print("Belum ada anggota.")
                    else:
                        nomor = 1
                        for nama in hasil:
                            print(str(nomor) + ".", nama, "-> Rp", hasil[nama])
                            nomor = nomor + 1
                    input("Tekan Enter untuk lanjut...")

                elif menu == "3":
                    print("=== TAMBAH ANGGOTA:", p[1], "===")
                    nama = input("Nama anggota baru: ").strip()
                    nama_ada = set()
                    for a in p[4]:
                        nama_ada.add(a[0].lower())
                    if nama == "":
                        print("Nama tidak boleh kosong!")
                    elif nama.lower() in nama_ada:
                        print("Nama sudah ada dalam daftar!")
                    else:
                        p[4].append([nama, 0])
                        print("Anggota ditambahkan. Nominal dihitung ulang otomatis.")
                    input("Tekan Enter untuk lanjut...")

              
                elif menu == "4":
                    print("=== KURANGI KONTRIBUSI:", p[1], "===")
                    if n == 0:
                        print("Belum ada anggota.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    for i in range(n):
                        print(str(i + 1) + ".", p[4][i][0], "-> Rp", round(nominal[i]))
                  
                    teks = input("Pilih nomor anggota: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor anggota harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > n:
                        print("Nomor anggota tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    idx = int(teks) - 1
               
                    teks = input("Jumlah pengurangan (Rp): ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Jumlah pengurangan harus berupa angka!")
                    elif int(teks) <= 0:
                        print("Jumlah pengurangan harus lebih dari 0!")
                    elif int(teks) > nominal[idx]:
                        print("Pengurangan melebihi nominal anggota!")
                    else:
                        p[4][idx][1] = p[4][idx][1] + int(teks)
                        print("Kontribusi diperbarui. Selisih dibagi rata ke seluruh anggota.")
                    input("Tekan Enter untuk lanjut...")

               
                elif menu == "5":
                    print("=== HAPUS ANGGOTA:", p[1], "===")
                    if n == 0:
                        print("Belum ada anggota.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    for i in range(n):
                        print(str(i + 1) + ".", p[4][i][0])
                    teks = input("Pilih nomor anggota: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor anggota harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > n:
                        print("Nomor anggota tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    yakin = input("Yakin hapus " + p[4][int(teks) - 1][0] + "? (Y/T): ").strip().upper()
                    if yakin == "Y":
                        p[4].pop(int(teks) - 1)
                        print("Anggota dihapus. Nominal dihitung ulang.")
                    elif yakin == "T":
                        print("Penghapusan dibatalkan.")
                    else:
                        print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "6":
                    print("=== HITUNG PATUNGAN:", p[1], "===")
                    if n == 0:
                        print("Belum ada anggota, tidak bisa dihitung.")
                    else:
                        print("Total biaya   : Rp", p[2])
                        print("Jumlah anggota:", n)
                        print("Porsi rata    : Rp", round(dasar))
                        print("-" * 40)
                        jumlah = 0
                        for nama in hasil:
                            print(nama, ": Rp", hasil[nama])
                            jumlah = jumlah + hasil[nama]
                        print("-" * 40)
                        print("Total terkumpul: Rp", jumlah)
                    input("Tekan Enter untuk lanjut...")

            
                elif menu == "7":
                    print("=== UBAH DATA PATUNGAN ===")
                    print("Nama kegiatan:", p[1])
                    print("Total biaya  : Rp", p[2])
                    nama_baru = input("Nama baru (Enter = tetap)  : ").strip()
                    teks = input("Total baru (Enter = tetap) : ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks != "" and angka == False:
                        print("Total biaya harus berupa angka! Perubahan dibatalkan.")
                    elif teks != "" and int(teks) <= 0:
                        print("Total biaya harus lebih dari 0! Perubahan dibatalkan.")
                    else:
                        if nama_baru != "":
                            p[1] = nama_baru
                        if teks != "":
                            p[2] = int(teks)
                        print("Data patungan diperbarui.")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "8":
                    yakin = input("Yakin hapus patungan '" + p[1] + "'? (Y/T): ").strip().upper()
                    if yakin == "Y":
                        patungan.remove(p)
                        print("Data patungan dihapus.")
                    elif yakin == "T":
                        print("Penghapusan dibatalkan.")
                    else:
                        print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

          
            elif menu == "9" and user_aktif[2] == "Admin":
                os.system(bersih)
                print("=== DAFTAR PENGGUNA ===")
                for i in range(len(pengguna)):
                    print(str(i + 1) + ".", pengguna[i][0], "-", pengguna[i][2])
                input("Tekan Enter untuk lanjut...")

           
            elif menu == "0":
                user_aktif = None
                print("Berhasil logout.")
                input("Tekan Enter untuk lanjut...")

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk lanjut...")


    elif pilih_awal == "3":
        print("Terima kasih!")
        break

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")