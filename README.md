# labpy02


# Program Pemesanan Tiket Bioskop

Flowchart untuk program ini

![alt text](<gambar/flowchart tiket bioskop.png>)

1. Menyapa pengguna:
```ruby
print("Selamat Datang di bioskop")
```

2. Meminta nama pengguna:
```ruby
nama = input("Silahkan masukan nama Anda: ")
```

3. Memberikan harga tiket:
```ruby
reguler, vip = 50000, 100000
```

4. Meminta tipe tiket:
```ruby
tipe = input("Masukkan tipe tiket (reguler/vip): ").lower()
```

5. Validasi tipe tiket:
```ruby
if tipe not in ["reguler", "vip"]:
    print("Tipe tiket yang Anda masukkan tidak valid.")
```

6. Meminta status member:
```ruby
member = input("Masukkan status member (aktif/tidak): ").lower()
```

7. Pemeriksaaan:
```ruby
if member not in ["aktif", "tidak", "tidak aktif"]:
    print("Status member tidak valid.")
```

8. Menghitung Harga Tiket:
```ruby
harga = reguler if tipe == "reguler" else vip
diskon = 0.8 if member == "aktif" else 1
total = harga * diskon
```

9. Menampilkan Total Harga:
```ruby
print(f"\nHalo {nama}, \nTotal yang harus anda bayar adalah: Rp {total}\n")
```


![alt text](<gambar/flowchart kalkulator sederhana.jpeg>)
