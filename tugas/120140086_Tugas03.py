class Dagangan:
    # Atribut kelas untuk menyimpan jumlah barang dan list barang
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        # Atribut instance
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        # Menambahkan informasi barang ke list_barang saat instansiasi baru
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    # Fungsi bantu untuk menampilkan jumlah_barang dan list_barang
    @classmethod
    def lihat_barang(cls):
        print("Jumlah Barang:", cls.jumlah_barang)
        print("List Barang:")
        for barang in cls.list_barang:
            print("- Nama:", barang[0])
            print("  Stok:", barang[1])
            print("  Harga:", barang[2])

    # Destructor untuk mengurangi jumlah_barang saat instans dihapus
    def __del__(self):
        Dagangan.jumlah_barang -= 1

# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

# Memanggil fungsi bantu untuk melihat barang
Dagangan.lihat_barang()

# Menghapus salah satu instans
del Dagangan1

# Memanggil fungsi bantu kembali setelah menghapus instans
Dagangan.lihat_barang()
