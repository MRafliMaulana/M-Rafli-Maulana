#SOAL NO 1

# angka = [1,2,3,4,5,7,12,111,4,43,32,40,-11]
# ganjil = []
# genap = []

# for x in angka:
#     if x % 2 == 0:
#         genap.append(x)
#     else:
#         ganjil.append(x)

# print(ganjil)
# print(genap)

#SOAL NO 2 DAN 3

dataMhs = {
    0: {"nim": "5230411121", "nama": "Putri Oktaviana", "nilai": 80},
    1: {"nim": "5230411122", "nama": "Ani Meriana", "nilai": 75},
    2: {"nim": "5230411123", "nama": "Agus Adetya", "nilai": 50},
    3: {"nim": "5230411124", "nama": "hari Purnama", "nilai": 30},
}


def cetakNilai(dataMhs={}):
    print("{:<15} {:<30} {:<12} {:<6}".format("NIM", "Nama", "Nilai Angka", "Huruf"))
    print("-" * 65)
    for i, mhs in dataMhs.items():
        print(
            "{:<15} {:<30} {:<12} {:<6}".format(
                mhs["nim"], mhs["nama"], mhs["nilai"], nilaiKeHuruf(mhs["nilai"])
            ),
        )


def nilaiKeHuruf(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 60 and nilai <= 79:
        return "B"
    elif nilai >= 45 and nilai <= 59:
        return "C"
    elif nilai >= 30 and nilai <= 44:
        return "D"
    else:
        return "E"


# Tambahan 4 nama mahasiswa
dataMhs[4] = {"nim": "5230411125", "nama": "Muhammad Rafli Maulana", "nilai": 98}
dataMhs[5] = {"nim": "5230411126", "nama": "Mirza Haris Nugraha", "nilai": 80}
dataMhs[6] = {"nim": "5230411127", "nama": "Rezqul Dwi Rugani", "nilai": 80}
dataMhs[7] = {"nim": "5230411128", "nama": "Haris Sasena", "nilai": 75}

cetakNilai(dataMhs)