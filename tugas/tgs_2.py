class Pegawai:
    def __init__(self, nama, gaji_pokok):
        self.__nama = nama
        self.__gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        pass

    def get_nama(self):
        return self.__nama

    def get_gaji_pokok(self):
        return self.__gaji_pokok


class Manajer(Pegawai):
    def __init__(self, nama, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, gaji_pokok)
        self.__tunjangan_jabatan = tunjangan_jabatan

    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.__tunjangan_jabatan


class KaryawanBiasa(Pegawai):
    def __init__(self, nama, gaji_pokok, bonus_proyek):
        super().__init__(nama, gaji_pokok)
        self.__bonus_proyek = bonus_proyek

    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.__bonus_proyek


class Perusahaan:
    def __init__(self):
        self.__daftar_pegawai = []

    def tambah_pegawai(self, pegawai):
        self.__daftar_pegawai.append(pegawai)

    def tampilkan_gaji_pegawai(self):
        for pegawai in self.__daftar_pegawai:
            print(f"{pegawai.get_nama()}: {pegawai.hitung_gaji()}")

# Membuat objek-objek pegawai
manajer1 = Manajer("Budi", 5000000, 2000000)
karyawan1 = KaryawanBiasa("Andi", 3000000, 1000000)

# Membuat objek perusahaan
perusahaan = Perusahaan()

# Menambahkan pegawai ke dalam perusahaan
perusahaan.tambah_pegawai(manajer1)
perusahaan.tambah_pegawai(karyawan1)

# Menampilkan gaji pegawai di perusahaan
perusahaan.tampilkan_gaji_pegawai()