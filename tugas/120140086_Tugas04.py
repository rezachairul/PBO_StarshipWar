class Calculator:
    def _init_(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Cannot divide by zero"
        
class AdvancedCalculator(Calculator):
    def power(self):
        return self.num1 ** self.num2
    
    def root(self):
        return self.num1 ** (1/self.num2)

def main():
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    
    # Kalkulator biasa
    calc = Calculator(num1, num2)
    print("Hasil penjumlahan:", calc.add())
    print("Hasil pengurangan:", calc.subtract())
    print("Hasil perkalian:", calc.multiply())
    print("Hasil pembagian:", calc.divide())
    
    # Kalkulator lanjutan
    adv_calc = AdvancedCalculator(num1, num2)
    print("Hasil pemangkatan:", adv_calc.power())
    print("Hasil akar:", adv_calc.root())
