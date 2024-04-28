from abc import ABC, abstractclassmethod

class operasi(ABC):
    @abstractclassmethod
    def op(self, x, y):
        pass

#Operasi Penjumlahan
class tambah(operasi):
    def op(self, x, y):
        return x + y
    
#Operasi Pengurangan
class kurang(operasi):
    def op(self, x, y):
        return x - y
    
#Operasi Perkalian
class kali(operasi):
    def op(self, x, y):
        return x * y
    
#Operasi Pembagian
class bagi(operasi):
    def op(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Tidak Bisa Dibagi Dengan Angka 0 (Nol)"
        
#Operasi Perpangkatan
class pangkat(operasi):
    def op(self, x, y):
        return pow(x, y)

#Kalkulator
class kalkulator(self, x, y):
    def _init_(Self):
        self.op={
            '+': tambah(),
            '-': kurang(),
            '*': kali(),
            '/': bagi(),
            '^': pangkat()
        }
    def kalkulator(self, hitung, x, y):
        if hitung in self.operasi:
            operasi = 
