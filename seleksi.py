#tugas membuat kasus yang ada di toko
#5230411150_Muhammad Rafli Maulana

print("========================")
print("Diskon Toko Jaya Makmur")
print("========================")

totalBelanja = int(input("Total belanja = "))


if totalBelanja >= 200000:
    status = input("Status = 1.Anggota 2.Bukan anggota :")
    if status == "1":
        diskon = totalBelanja * (20/100)
        print("Diskon : 20%")
        total_bayar = totalBelanja - diskon 
        print("Total Bayar :", total_bayar)
    else:
        diskon = totalBelanja * (10/100)
        print("Diskon : 10%")
        total_bayar = totalBelanja - diskon
        print("Total Bayar :", total_bayar)

else:
    print("Diskon : Maaf Tidak mendapatkan Diskon")
    print("Total Bayar :", totalBelanja)

