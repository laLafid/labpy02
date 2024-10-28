while True:
    print("kalkulator sederhana\n")
    print("menu pilihan : ")
    print("1. penjumlahan\n2. pengurangan\n3. perkalian\n4. pembagian\n5. pangkat\n6. keluar\n")
    pilih = input("masukkan pilihan : ")
    
    if pilih == '1' or pilih == 'penjumlahan': 
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: ")) 
        print(b1, "+", b2, "=", b1 + b2)        
    elif pilih == '2' or pilih == 'pengurangan': 
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: ")) 
        print(b1, "-", b2, "=", b1 - b2)    
    elif pilih == '3' or pilih == 'perkalian': 
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: "))
        print(b1, "*", b2, "=", b1 * b2)         
    elif pilih == '4' or pilih == 'pembagian': 
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: "))
        if b2 != 0:
            print(b1, "/", b2, "=", b1 / b2)
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
    elif pilih == '5' or pilih == 'pangkat': 
        b1 = float(input("masukan bilangan pertama: "))
        b2 = float(input("masukan bilangan kedua: "))
        print(b1, "**", b2, "=", b1 ** b2)
    elif pilih == '6' or pilih == 'keluar':
        print("terimakasih") 
        break 
    else: print("tidak ada pilihan itu") 
      

   

    
    
