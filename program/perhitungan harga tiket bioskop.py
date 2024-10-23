print("Selamat Datang di bioskop")
nama = input("Masukan nama Anda: ")

def harga_tiket():
    
    reguler = 50000
    vip = 100000
    
    tipe = input("Masukkan tipe tiket (reguler/vip): ")
    member = input("Masukkan status member (aktif/tidak): ")
    
    harga = reguler if tipe.lower() == "reguler" else vip
    diskon = 0.8 if member.lower() == "aktif" else 1
    total = harga * diskon
    
    print(f"\nHalo {nama}, \nTotal yang harus anda bayar: Rp {total}\n")
    
harga_tiket()