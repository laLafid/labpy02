def kalkulator():
    while True:
        print("Kalkulator Sederhana\n1. penjumlahan\n2. pengurangan\n3. perkalian\n4. pembagian")
        pilih = input("masukkan pilihan : ").lower()
        if pilih in ['1', 'penjumlahan', '2', 'pengurangan', '3', 'perkalian', '4', 'pembagian']:
            break
        else:
            print("tidak ada pilihan itu, silakan pilih lagi")

    A = float(input("masukan bilangan pertama: "))
    B = float(input("masukan bilangan kedua: "))

    if pilih in ['1', 'penjumlahan']:
        print("Hasil dari Penjumlahan:", A, "+", B, "=", A + B)
    elif pilih in ['2', 'pengurangan']:
        print("Hasil dari Pengurangan:", A, "-", B, "=", A - B)
    elif pilih in ['3', 'perkalian']:
        print("Hasil dari Perkalian:", A, "*", B, "=", A * B)
    elif pilih in ['4', 'pembagian']:
        if B != 0:
            print("Hasil dari Pembagian:", A, "/", B, "=", A / B)
        else:
            print("Error: Tidak bisa membagi dengan nol!")
    else:
        print("tidak ada pilihan itu")

kalkulator()