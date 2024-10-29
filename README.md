# labpy02


# Program Pemesanan Tiket Bioskop


## Flowchart untuk program ini

![alt text](<gambar/flowchart tiket bioskop.png>)

## Penjelasan Kode
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
### Hasil Kode

![alt text](<gambar/hasil tiket .png>)

# Program Kalkulator Sederhana

## Flowchart 

![alt text](<gambar/flowchart kalkulator sederhana.jpeg>)

## Penjelasan Kode

1. Looping:
```ruby
while True:
    print("Kalkulator Sederhana\n1. penjumlahan\n2. pengurangan\n3. perkalian\n4. pembagian")
    pilih = input("masukkan pilihan : ").lower()
    if pilih in ['1', 'penjumlahan', '2', 'pengurangan', '3', 'perkalian', '4', 'pembagian']:
        break
    else:
        print("tidak ada pilihan itu, silakan pilih lagi")
```
Tujuannya agar Program terus menampilkan opsi kalkulator (penjumlahan, pengurangan, perkalian, dan pembagian) hingga pengguna memasukkan pilihan yang valid.

2. Meminta input bilangan:
```ruby
A = float(input("masukan bilangan pertama: "))
B = float(input("masukan bilangan kedua: "))
```

3. Melakukan operasi aritmatika:
```ruby
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
```
### Hasil Kode

![alt text](<gambar/hasil kalkulator.png>)