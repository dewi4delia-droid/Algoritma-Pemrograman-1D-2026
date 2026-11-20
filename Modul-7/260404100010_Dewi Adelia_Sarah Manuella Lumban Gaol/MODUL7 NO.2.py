playlist = {}

while True:
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada")
        elif nama == "":
            print("Nama playlist tidak boleh kosong")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            lagu = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][lagu] = penyanyi
            print("Lagu berhasil ditambahkan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "3":
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            print(playlist)

    elif pilih == "4":
        lagu = input("Cari lagu: ")
        ditemukan = False

        for nama, data in playlist.items():
            if lagu in data:
                print("Playlist:", nama)
                print("Lagu:", lagu)
                print("Penyanyi:", data[lagu])
                ditemukan = True

        if ditemukan == False:
            print("Lagu tidak ditemukan")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            lagu = input("Judul lagu: ")
            if lagu in playlist[nama]:
                del playlist[nama][lagu]
                print("Lagu berhasil dihapus")
            else:
                print("Lagu tidak ditemukan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "6":
        nama = input("Nama playlist: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")
