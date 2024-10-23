def harga_tiket():
    reguler = 50000
    vip = 100000
    tipe = input("masukkan tipe tiket (reguler/vip): ")
    member = input("masukkan status member (aktif/tidak): ")
    
    harga = reguler if tipe == "reguler" else vip
    diskon = 0.8 if member == "aktif" else 1
    total = harga * diskon
    print("total bayar: ", total)
    
harga_tiket()