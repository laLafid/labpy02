def pertambahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def kalkulator ():
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    
    choice = int(input("masukkan pilihan: "))
    
    if choice in (1, 2, 3, 4):
        num1 = float(input("masukan bilangan pertama: "))
        num2 = float(input("masukan bilangan kedua: "))

    if choice == 1:
            print(num1, "+", num2, "=", pertambahan(num1, num2))
            
    elif choice == 2:
            print(num1, "-", num2, "=", pengurangan(num1, num2))
            
    elif choice == 3:
            print(num1, "*", num2, "=", perkalian(num1, num2))
            
    elif choice == 4:
            print(num1, "/", num2, "=", pembagian(num1, num2))

    else:
        return("tidak ada pilihan itu") 
    
kalkulator()
    