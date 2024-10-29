print("Selamat Datang di bioskop")
nama = input("Silahkan masukan nama Anda: ")

reguler, vip = 50000, 100000

tipe = input("Masukkan tipe tiket (reguler/vip): ").lower()
if tipe not in ["reguler", "vip"]:
    print("Tipe tiket yang Anda masukkan tidak valid.")
else:
    member = input("Masukkan status member (aktif/tidak): ").lower()
    if member not in ["aktif", "tidak", "tidak aktif"]:
        print("Status member tidak valid.")
    else:
        harga = reguler if tipe == "reguler" else vip
        diskon = 0.8 if member == "aktif" else 1
        total = harga * diskon
        print(f"\nHalo {nama}, \nTotal yang harus anda bayar adalah: Rp {total}\n")