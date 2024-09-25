import mysql.connector
import os
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_barang",
)

cursor = conn.cursor()


def insert_barang(data):
    sql = "INSERT into barang(kode, nama, jumlah, satuan, harga) VALUES(%s, %s, %s, %s, %s)"
    value = (
        data["kode"],
        data["nama"],
        data["jumlah"],
        data["satuan"],
        data["harga"],
    )

    cursor.execute(sql, value)
    conn.commit()


def update_barang(data):
    sql = "UPDATE barang set nama=%s, jumlah=%s, satuan=%s, harga=%s WHERE kode=%s"
    value = (
        data["nama"],
        data["jumlah"],
        data["satuan"],
        data["harga"],
        data["kode"],
    )
    cursor.execute(sql, value)
    conn.commit()


def delete_barang(kodeBarang):
    sql = "DELETE FROM barang WHERE kode=%s"
    cursor.execute(sql, (kodeBarang,))
    conn.commit()


def search_barang(kodeBarang):
    sql = "SELECT * FROM barang WHERE kode=%s"
    cursor.execute(sql, (kodeBarang,))
    result = cursor.fetchone()
    return result


def get_all_barang():
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def print_all_barang():
    clear_screen()
    list_barang = get_all_barang()

    print("-----------------------------------------------------------")
    print(" No Kode   Nama Barang           Jumlah Satuan        Harga")
    print("-----------------------------------------------------------")
    no = 0
    for barang in list_barang:
        no = no + 1
        print(
            "{:3d}".format(no),
            "{:6s}".format(barang[0]),
            "{:20s}".format(barang[1]),
            "{:7d}".format(barang[2]),
            "{:^8s}".format(barang[3]),
            "{:>10,d}".format(barang[4]),
        )

    print("-----------------------------------------------------------")


def print_menu():
    clear_screen()
    print("=========Menu=========")
    print("1. Tambah barang")
    print("2. Ubah barang")
    print("3. Hapus barang")
    print("4. Tampilkan barang")
    print("x. Keluar dari menu")
    print("======================")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


while True:
    print_menu()
    menu = input("Pilih menu [1,2,3,4,X]: ")

    if menu == "1":
        clear_screen()
        kode = input("Masukan kode barang [xxxxx] : ")
        clear_screen()

        if search_barang(kode) != None:
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            print("Kode barang sudah digunakan")
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            time.sleep(3)
            continue

        nama = input("Masukan nama barang : ")
        clear_screen()
        jumlah = input("Masukan jumlah barang : ")
        clear_screen()
        satuan = input("Masukan satuan barang : ")
        clear_screen()
        harga = input("Masukan harga barang : ")
        clear_screen()

        data = {
            "kode": kode,
            "nama": nama,
            "jumlah": jumlah,
            "satuan": satuan,
            "harga": harga,
        }

        insert_barang(data)

        print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
        print("Berhasil menambahkan barang")
        print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
        time.sleep(3)

    elif menu == "2":
        clear_screen()
        kode = input("Masukan kode barang [xxxxx] : ")
        clear_screen()

        if search_barang(kode) == None:
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            print("Kode barang tidak ditemukan")
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            time.sleep(3)
            continue

        nama = input("Masukan nama barang : ")
        clear_screen()
        jumlah = input("Masukan jumlah barang : ")
        clear_screen()
        satuan = input("Masukan satuan barang : ")
        clear_screen()
        harga = input("Masukan harga barang : ")
        clear_screen()

        data = {
            "kode": kode,
            "nama": nama,
            "jumlah": jumlah,
            "satuan": satuan,
            "harga": harga,
        }

        update_barang(data)

        print("<<<<<<<<<<<<>>>>>>>>>>>>")
        print("Berhasil mengubah barang")
        print("<<<<<<<<<<<<>>>>>>>>>>>>")
        time.sleep(3)

    elif menu == "3":
        clear_screen()
        kode = input("Masukan kode barang [xxxxx] : ")
        clear_screen()

        if search_barang(kode) == None:
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            print("Kode barang tidak ditemukan")
            print("<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            time.sleep(3)
            continue

        delete_barang(kode)

        print("<<<<<<<<<<<<>>>>>>>>>>>>>")
        print("Berhasil menghapus barang")
        print("<<<<<<<<<<<<>>>>>>>>>>>>>")
        time.sleep(3)

    elif menu == "4":
        print_all_barang()
        input("Tekan 'enter' untuk lanjut")

    elif menu == "x" or menu == "X":
        break

    else:
        clear_screen()
        print("<<<<<<<<<<<<>>>>>>>")
        print("Pilihan Tidak Valid")
        print("<<<<<<<<<<<<>>>>>>>")
        time.sleep(3)

clear_screen()
print("<<<<<<<<<<<<>>>>>>")
print("---Sampai Jumpa---")
print("<<<<<<<<<<<<>>>>>>")