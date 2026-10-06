username_benar = "zaky"
password_benar = "097"

login = False

for i in range(3):
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong!")
    elif username == username_benar and password == password_benar:
        print("Login Berhasil")
        login = True
        break
    else:
        print("Login Gagal. Sisa percobaan:", 2 - i)

if login == False:
    print("Login gagal 3 kali. Program berakhir.")

else:
    uang_bulanan = int(input("\nMasukkan uang saku awal: "))
    total_pengeluaran = 0

    while uang_bulanan > 0:
        print("\n==========================")
        print("       MENU UTAMA")
        print("==========================")
        print("[1] Catat Pengeluaran")
        print("[2] Cek Sisa Uang Saku")
        print("[3] Keluar")
        print("==========================")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":

            while True:
                pengeluaran = int(input("Masukkan pengeluaran: Rp"))

                if pengeluaran <= uang_bulanan:
                    uang_bulanan = uang_bulanan - pengeluaran
                    total_pengeluaran = total_pengeluaran + pengeluaran

                    print("Pengeluaran berhasil dicatat!")
                    print("Sisa uang saku: Rp", uang_bulanan)

                else:
                    print("Saldo tidak cukup!")
                    continue

                if uang_bulanan == 0:
                    print("Uang saku sudah habis!")
                    break

                lagi = input(
                    "Apakah ingin mencatat pengeluaran lagi? (Y/T): "
                ).upper()

                if lagi == "T":
                    break

        elif pilihan == "2":
            print("\n=== REKAPITULASI ===")
            print("Sisa uang saku    : Rp", uang_bulanan)
            print("Total pengeluaran : Rp", total_pengeluaran)

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak valid! Pilih 1, 2, atau 3.")

    if uang_bulanan == 0:
        print("\nSaldo habis. Program berakhir.")