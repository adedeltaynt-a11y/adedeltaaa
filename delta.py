import math

print("=== KALKULATOR PYTHON ===")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")
print("6. Akar")
print("7. Sin")
print("8. Cos")
print("9. Tan")

pilih = int(input("Pilih operasi: "))

if pilih >= 1 and pilih <= 5:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilih == 1:
        print("Hasil:", a + b)
    elif pilih == 2:
        print("Hasil:", a - b)
    elif pilih == 3:
        print("Hasil:", a * b)
    elif pilih == 4:
        if b != 0:
            print("Hasil:", a / b)
        else:
            print("Tidak bisa dibagi nol")
    elif pilih == 5:
        print("Hasil:", a ** b)

elif pilih == 6:
    a = float(input("Masukkan angka: "))
    print("Hasil:", math.sqrt(a))

elif pilih >= 7 and pilih <= 9:
    sudut = float(input("Masukkan sudut: "))
    rad = math.radians(sudut)

    if pilih == 7:
        print("Sin =", math.sin(rad))
    elif pilih == 8:
        print("Cos =", math.cos(rad))
    elif pilih == 9:
        print("Tan =", math.tan(rad))

else:
    print("Pilihan tidak tersedia")