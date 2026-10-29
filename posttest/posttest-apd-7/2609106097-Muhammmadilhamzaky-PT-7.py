import os

bersih = "cls" if os.name == "nt" else "clear"

pengguna = {
    "admin": {"password": "admin123", "role": "Admin"},
    "zaky": {"password": "zaky", "role": "Pengguna Biasa"}
}

patungan = {}
id_berikut = 1
user_aktif = None

def input_angka(pesan):
    try:
        teks = input(pesan).strip()
        if not teks.isdigit():
            raise ValueError("Input bukan angka")
        angka = int(teks)
    except ValueError:
        return None
    else:
        return angka

def jumlah_rekursif(nilai, indeks=0):
    if indeks == len(nilai):
        return 0
    return nilai[indeks] + jumlah_rekursif(nilai, indeks + 1)

def nama_sudah_ada(nama, daftar):
    return nama.lower() in [d.lower() for d in daftar]

def hitung_nominal(p):
    anggota = p["anggota"]
    n = len(anggota)
    total_pengurangan = jumlah_rekursif(list(anggota.values()))
    dasar = p["total_biaya"] / n

    hasil = {
        nama: round(dasar - pengurangan + total_pengurangan / n)
        for nama, pengurangan in anggota.items()
    }
    return hasil, dasar

def baca_pilihan():
    return input("Pilih menu: ").strip()

def login():
    for i in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        try:
            if pengguna[username]["password"] == password:
                print("Login berhasil!")
                return username
            raise ValueError("Password salah")
        except (KeyError, ValueError):
            print("Login salah! Sisa percobaan:", 2 - i)
    return None

def input_anggota_awal():
    anggota = {}

    while True:
        nama_anggota = input("Nama anggota (Enter untuk selesai): ").strip()

        if nama_anggota == "":
            if not anggota:
                print("Minimal 1 anggota!")
                continue
            break

        if nama_sudah_ada(nama_anggota, anggota):
            print("Nama anggota sudah ada!")
        else:
            anggota[nama_anggota] = 0
    return anggota

def tampil_menu_awal():
    os.system(bersih)
    print("=== SISTEM KALKULATOR PATUNGAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

def tampil_menu_utama(role):
    os.system(bersih)
    print("=== MENU UTAMA ===")
    print("Login sebagai:", user_aktif, "-", role)
    print("1. Tambah data patungan")
    print("2. Tampilkan anggota")
    print("3. Tambah anggota")
    print("4. Kurangi kontribusi")
    print("5. Hapus anggota")
    print("6. Hitung nominal patungan")
    print("7. Ubah data patungan")
    print("8. Hapus data patungan")

    if role == "Admin":
        print("9. Lihat daftar pengguna")

    print("0. Logout")

def register():
    username = input("Username baru: ").strip()

    if not username:
        print("Username tidak boleh kosong!")
    elif nama_sudah_ada(username, pengguna):
        print("Username sudah dipakai!")
    else:
        password = input("Password baru: ").strip()

        if len(password) < 4:
            print("Password minimal 4 karakter!")
        else:
            pengguna[username] = {
                "password": password,
                "role": "Pengguna Biasa"
            }
            print("Register berhasil!")

    input("Tekan Enter...")

def tambah_patungan():
    global id_berikut

    nama = input("Nama kegiatan: ").strip()
    total = input_angka("Total biaya (Rp): ")

    if not nama or total is None or total <= 0:
        print("Nama atau total biaya tidak valid!")
    else:
        anggota = input_anggota_awal()

        patungan[id_berikut] = {
            "nama": nama,
            "total_biaya": total,
            "pemilik": user_aktif,
            "anggota": anggota
        }

        id_berikut += 1
        print("Data patungan berhasil ditambahkan!")

    input("Tekan Enter...")

def tampil_daftar_patungan(daftar_id):
    print("=== DAFTAR PATUNGAN ===")
    for i, k in enumerate(daftar_id, 1):
        p = patungan[k]
        print(i, ".", p["nama"], "| Total Rp", p["total_biaya"])

def ubah_patungan(p):
    nama_baru = input("Nama baru (Enter = tetap): ").strip()
    total_baru = input("Total biaya baru (Enter = tetap): ").strip()

    if total_baru and (not total_baru.isdigit() or int(total_baru) <= 0):
        print("Total biaya tidak valid!")
    else:
        if nama_baru:
            p["nama"] = nama_baru
        if total_baru:
            p["total_biaya"] = int(total_baru)
        print("Data berhasil diubah!")

def hapus_patungan(id_pilih):
    yakin = input("Hapus data ini? (Y/T): ").upper()
    if yakin == "Y":
        del patungan[id_pilih]
        print("Data patungan dihapus!")

def tambah_anggota(anggota):
    nama = input("Nama anggota baru: ").strip()

    if not nama:
        print("Nama tidak boleh kosong!")
    elif nama_sudah_ada(nama, anggota):
        print("Anggota sudah ada!")
    else:
        anggota[nama] = 0
        print("Anggota berhasil ditambahkan!")

def hapus_anggota(anggota):
    daftar = list(anggota.keys())

    if not daftar:
        print("Belum ada anggota.")
        return

    for i, nama in enumerate(daftar, 1):
        print(i, ".", nama)

    nomor_a = input_angka("Pilih nomor anggota: ")

    if nomor_a is not None and 1 <= nomor_a <= len(daftar):
        nama = daftar[nomor_a - 1]
        yakin = input("Hapus " + nama + "? (Y/T): ").upper()

        if yakin == "Y":
            del anggota[nama]
            print("Anggota berhasil dihapus!")
    else:
        print("Nomor anggota tidak valid!")

def kurangi_kontribusi(anggota, hasil):
    daftar = list(anggota.keys())
    n = len(daftar)

    for i, nama in enumerate(daftar, 1):
        print(i, ".", nama, "-> Rp", hasil[nama])

    nomor_a = input_angka("Pilih nomor anggota: ")
    jumlah = input_angka("Jumlah pengurangan (Rp): ")

    if (nomor_a is not None
            and 1 <= nomor_a <= n
            and jumlah is not None
            and jumlah > 0
            and jumlah <= hasil[daftar[nomor_a - 1]]):
        nama = daftar[nomor_a - 1]
        anggota[nama] += jumlah
        print("Kontribusi berhasil diperbarui!")
    else:
        print("Input pengurangan tidak valid!")

def proses_hitung(menu, p):
    anggota = p["anggota"]
    n = len(anggota)

    if n == 0:
        print("Belum ada anggota.")
        return

    hasil, dasar = hitung_nominal(p)

    if menu == "2":
        print("=== DAFTAR NOMINAL ANGGOTA ===")
        for nama, nominal in hasil.items():
            print(nama, "-> Rp", nominal)

    elif menu == "4":
        kurangi_kontribusi(anggota, hasil)

    elif menu == "6":
        print("Total biaya: Rp", p["total_biaya"])
        print("Jumlah anggota:", n)
        print("Porsi rata-rata: Rp", round(dasar))
        for nama, nominal in hasil.items():
            print(nama, ": Rp", nominal)

def menu_utama():
    global user_aktif

    while user_aktif is not None:
        role = pengguna[user_aktif]["role"]

        tampil_menu_utama(role)
        menu = baca_pilihan()

        if menu == "0":
            user_aktif = None
            print("Logout berhasil!")
            input("Tekan Enter...")
            continue

        if menu == "9" and role == "Admin":
            for nama, data in pengguna.items():
                print(nama, "-", data["role"])
            input("Tekan Enter...")
            continue

        terlihat = {
            k: v for k, v in patungan.items()
            if role == "Admin" or v["pemilik"] == user_aktif
        }

        if menu == "1":
            tambah_patungan()
            continue

        if menu not in ["2", "3", "4", "5", "6", "7", "8"]:
            print("Menu tidak valid!")
            input("Tekan Enter...")
            continue

        if not terlihat:
            print("Belum ada data patungan.")
            input("Tekan Enter...")
            continue

        daftar_id = list(terlihat.keys())
        tampil_daftar_patungan(daftar_id)

        nomor = input_angka("Pilih nomor patungan: ")

        if nomor is None or not 1 <= nomor <= len(daftar_id):
            print("Nomor patungan tidak valid!")
            input("Tekan Enter...")
            continue

        id_pilih = daftar_id[nomor - 1]
        p = patungan[id_pilih]

        if menu == "7":
            ubah_patungan(p)
        elif menu == "8":
            hapus_patungan(id_pilih)
        elif menu == "3":
            tambah_anggota(p["anggota"])
        elif menu == "5":
            hapus_anggota(p["anggota"])
        else:
            proses_hitung(menu, p)

        input("Tekan Enter untuk lanjut...")

def main():
    global user_aktif

    while True:
        tampil_menu_awal()
        pilih = baca_pilihan()

        if pilih == "3":
            print("Terima kasih!")
            break

        elif pilih == "2":
            register()

        elif pilih == "1":
            user_aktif = login()

            if user_aktif is None:
                input("Login gagal. Tekan Enter...")
                continue

            menu_utama()

        else:
            print("Menu tidak valid!")
            input("Tekan Enter...")

try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan oleh pengguna.")
finally:
    print("Program selesai.")