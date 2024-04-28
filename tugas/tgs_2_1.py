class AlatTulis:
    def __init__(self, nama, stok, harga_satuan):
        self.__nama = nama
        self.__stok = stok
        self.__harga_satuan = harga_satuan
        self.__harga_total_sementara = stok * harga_satuan

    def set_nama(self, nama):
        self.__nama = nama

    def set_stok(self, stok):
        self.__stok = stok
        self.__harga_total_sementara = self.__stok * self.__harga_satuan

    def set_harga_satuan(self, harga_satuan):
        self.__harga_satuan = harga_satuan
        self.__harga_total_sementara = self.__stok * harga_satuan

    def get_nama(self):
        return self.__nama

    def get_stok(self):
        return self.__stok

    def get_harga_satuan(self):
        return self.__harga_satuan

    def get_harga_total_sementara(self):
        return self.__harga_total_sementara


# Membuat objek-objek alat tulis
pena = AlatTulis("Pena", 10, 4500)
pensil = AlatTulis("Pensil", 15, 2000)
penghapus = AlatTulis("Penghapus", 5, 1000)

# Menampilkan informasi masing-masing alat tulis
print(f"Nama alat tulis: {pena.get_nama()}")
print(f"Stok: {pena.get_stok()}")
print(f"Harga satuan: {pena.get_harga_satuan()}")
print(f"Harga total sementara: {pena.get_harga_total_sementara()}")

print(f"\nNama alat tulis: {pensil.get_nama()}")
print(f"Stok: {pensil.get_stok()}")
print(f"Harga satuan: {pensil.get_harga_satuan()}")
print(f"Harga total sementara: {pensil.get_harga_total_sementara()}")

print(f"\nNama alat tulis: {penghapus.get_nama()}")
print(f"Stok: {penghapus.get_stok()}")
print(f"Harga satuan: {penghapus.get_harga_satuan()}")
print(f"Harga total sementara: {penghapus.get_harga_total_sementara()}")

# Menampilkan total harga semua barang
total_harga = pena.get_harga_total_sementara() + pensil.get_harga_total_sementara() + penghapus.get_harga_total_sementara()
print(f"\nTotal harga: {total_harga}")
