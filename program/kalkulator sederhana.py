print("kalkulator sederhana\n")
def kalkulator ():
    
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    
    pilih = int(input("masukkan pilihan : "))
    
    if pilih in (1, 2, 3, 4):
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: "))

    if pilih == 1: print(b1, "+", b2, "=", b1 + b2)      
    elif pilih == 2: print(b1, "-", b2, "=", b1 - b2)       
    elif pilih == 3: print(b1, "*", b2, "=", b1 * b2)        
    elif pilih == 4: print(b1, "/", b2, "=", b1 / b2)
    else: print("tidak ada pilihan itu") 
    
kalkulator()
    