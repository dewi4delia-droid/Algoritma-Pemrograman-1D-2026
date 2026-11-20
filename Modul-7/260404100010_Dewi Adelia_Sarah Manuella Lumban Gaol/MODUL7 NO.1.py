tugas = {}

while True:
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Selesaikan")
    print("4. Hapus")
    print("5. Hitung")
    print("6. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        if nama in tugas:
            print("Tugas sudah ada")
        elif nama == "":
            print("Nama tugas tidak boleh kosong")
        else:
            tugas[nama] = False
            print("Tugas berhasil ditambahkan")

    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            print(tugas)

    elif pilih == "3":
        nama = input("Nama tugas: ")
        if nama in tugas:
            tugas[nama] = True
            print("Tugas selesai")
        else:
            print("Tugas tidak ada")

    elif pilih == "4":
        nama = input("Nama tugas: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus")
        else:
            print("Tugas tidak ada")

    elif pilih == "5":
        print("Selesai:", sum(tugas.values()))
        print("Belum:", len(tugas) - sum(tugas.values()))

    elif pilih == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")

