import os
import time

data = {
    "0": {
        "nik": "987654321012466",
        "nama": "shinta",
        "jenis_kelamin": "P",
        "agama": 1,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 1,
    },
    "1": {
        "nik": "987654321012465",
        "nama": "mirza",
        "jenis_kelamin": "L",
        "agama": 1,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 2,
    },
    "2": {
        "nik": "987654321012464",
        "nama": "arifin",
        "jenis_kelamin": "L",
        "agama": 6,
        "status_perkawinan": "kawin",
        "pekerjaan": 1,
    },
    "3": {
        "nik": "987654321012463",
        "nama": "rafli",
        "jenis_kelamin": "L",
        "agama": 4,
        "status_perkawinan": "kawin",
        "pekerjaan": 4,
    },
    "4": {
        "nik": "987654321012462",
        "nama": "Nizar",
        "jenis_kelamin": "L",
        "agama": 2,
        "status_perkawinan": "kawin",
        "pekerjaan": 6,
    },
    "5": {
        "nik": "987654321012461",
        "nama": "Dinda",
        "jenis_kelamin": "P",
        "agama": 7,
        "status_perkawinan": "kawin",
        "pekerjaan": 5,
    },
    "6": {
        "nik": "987654321012460",
        "nama": "Herman",
        "jenis_kelamin": "L",
        "agama": 7,
        "status_perkawinan": "kawin",
        "pekerjaan": 1,
    },
    "7": {
        "nik": "987654321012459",
        "nama": "Rizqhul",
        "jenis_kelamin": "L",
        "agama": 1,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 1,
    },
    "8": {
        "nik": "987654321012458",
        "nama": "Talita",
        "jenis_kelamin": "P",
        "agama": 2,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 1,
    },
    "9": {
        "nik": "987654321012457",
        "nama": "Haris",
        "jenis_kelamin": "L",
        "agama": 1,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 3,
    },
    "10": {
        "nik": "987654321012456",
        "nama": "Gilang",
        "jenis_kelamin": "L",
        "agama": 1,
        "status_perkawinan": "kawin",
        "pekerjaan": 5,
    },
    "11": {
        "nik": "987654321012455",
        "nama": "Citra",
        "jenis_kelamin": "P",
        "agama": 5,
        "status_perkawinan": "kawin",
        "pekerjaan": 3,
    },
    "12": {
        "nik": "987654321012454",
        "nama": "Made",
        "jenis_kelamin": "L",
        "agama": 4,
        "status_perkawinan": "kawin",
        "pekerjaan": 6,
    },
    "13": {
        "nik": "987654321012453",
        "nama": "Naila",
        "jenis_kelamin": "P",
        "agama": 1,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 1,
    },
    "14": {
        "nik": "987654321012452",
        "nama": "Rifqi",
        "jenis_kelamin": "L",
        "agama": 1,
        "status_perkawinan": "kawin",
        "pekerjaan": 2,
    },
    "15": {
        "nik": "987654321012451",
        "nama": "Friska",
        "jenis_kelamin": "P",
        "agama": 4,
        "status_perkawinan": "belum kawin",
        "pekerjaan": 4,
    },
}


def print_menu():
    clear_screen()
    print("==========Program Kependudukan==========\n")
    print("1. Tampilkan jumlah penduduk perempuan yang belum kawin")
    print("2. Tampilkan jumlah penduduk perempuan yang tidak beragama islam")
    print("3. Tampilkan jumlah penduduk laki-laki yang perkerjaannya PNS")
    print("4. Tampilkan jumlah penduduk laki-laki yang perkerjaannya petani atau nelayan")
    print("5. Keluar")


def populasi_perempuan_belumKawin():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "P" and item.get("status_perkawinan") != "kawin":
            counter += 1
    return counter


def non_muslim_wanita():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "P" and item.get("agama") != 1:
            counter += 1
    return counter


def lakilaki_pns():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "L" and item.get("pekerjaan") == 1:
            counter += 1
    return counter


def lakilaki_nelayan_atau_petani():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "L" and (
            item.get("pekerjaan") == 4 or item.get("pekerjaan") == 5
        ):
            counter += 1
    return counter


def print_count(count):
    clear_screen()
    print("<<<<<<<<<>>>>>>>>")
    print(f"Jumlah : {count}")
    print("<<<<<<<<<>>>>>>>>")

    time.sleep(3)


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


while True:
    print_menu()
    menu = input("Masukan pilihan menu [1-5] : ")

    if menu == "1":
        count = populasi_perempuan_belumKawin()
        print_count(count)

    elif menu == "2":
        count = non_muslim_wanita()
        print_count(count)

    elif menu == "3":
        count = lakilaki_pns()
        print_count(count)

    elif menu == "4":
        count = lakilaki_nelayan_atau_petani()
        print_count(count)

    elif menu == "5":
        break

    else:
        clear_screen()
        print("<<<<<<<<<<<<<>>>>>>>>>>>")
        print("Pilihan Menu Tidak Valid")
        print("<<<<<<<<<<<<<>>>>>>>>>>>")
        time.sleep(3)

print("<<<<<>>>>>>")
print("Terimakasih")
print("<<<<<>>>>>>")