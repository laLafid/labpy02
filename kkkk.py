def tiket():
    reguler = 50000
    vip = 100000
    
    tipe = input("masukkan tipe tiket (reguler/vip): ")
    
    member = input("masukkan status member (yes/no): ")
    
    if tipe == "reguler" and member == "yes":
        print("total bayar: ", reguler * 0.8)
    elif tipe == "reguler" and member == "no":
        print("total bayar: ", reguler)
    elif tipe == "vip" and member == "yes":
        print("total bayar: ", vip * 0.8)
    elif tipe == "vip" and member == "no":
        print("total bayar: ", vip)

tiket()
