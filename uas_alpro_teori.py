#SOAL NO 1
import mysql.connector
import matplotlib.pyplot as plt
import datetime as dt

# def connectionDB():
#     connector = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "",
#         database = "pln"

#     )
#     if connector.is_connected:
#         print("Database Terkoneksi")
#         return connector
#     else:
#         print("Database gagal terkoneksi")
#         return False


# def insertData(id, nama_pelanggan, tarif_daya, tarif_watt):
#     try:
#         conn = connectionDB()
#         cursor = conn.cursor()
#         sql = "INSERT INTO pelanggan (id, nama_pelanggan, tarif_daya, tarif_watt) VALUES (%s, %s, %s,%s)"
#         data = (id, nama_pelanggan, tarif_daya, tarif_watt)
#         cursor.execute(sql, data)
#         conn.commit()
#         print("Data berhasil ditambah")
#     except mysql.connector.Error as error:
#         print("terjadi kesalahan : ", error)
#     finally:
#         if conn.is_connected:
#             cursor.close()
#             conn.close()


# def menu():
#     print("=======================")
#     print("1. Input Data Nilai")
#     print("2. Update Data nilai")
#     print("3. Hapus Data")
#     print("4. Tampilkan Data")
#     print("5. Keluar")
#     print("=======================")




# def updateData(id, nama_pelanggan, tarif_daya, tarif_watt):
#     try:
#         conn = connectionDB()
#         cursor = conn.cursor()
#         sql = (
#             "UPDATE pelanggan SET nama_pelanggan = %s, tarif_daya = %s , tarif_watt = %s WHERE id = %s"
#         )
#         data = (nama_pelanggan, tarif_daya, tarif_watt, id)
#         cursor.execute(sql, data)
#         conn.commit()
#         print("data telah diubah")
#     except mysql.connector.Error as error:
#         print("terjadi kesalahan : ", error)
#     finally:
#         if conn.is_connected:
#             cursor.close()
#             conn.close()

# def deleteData(id):
#     try:
#         conn = connectionDB()
#         cursor = conn.cursor()
#         sql = "DELETE FROM pelanggan WHERE id=%s"
#         data = (id,)
#         cursor.execute(sql, data)
#         conn.commit()
#         print("data telah dihapus")
#     except mysql.connector.Error as error:
#         print("terjadi kesalahan : ", error)
#     finally:
#         if conn.is_connected:
#             cursor.close()
#             conn.close()

# def tampilData():
#     conn = connectionDB()
#     cursor = conn.cursor()
#     print (">>>> MENAMPILKAN REKAMAN TABEL PELANGGAN <<<<\n")
#     cursor.execute("SELECT * FROM pelanggan")
#     hasil = cursor.fetchall()
#     print("--------------------------------------------------------")
#     print("id   nama_pelanggan     tarif_daya          tarif_watt ")
#     print("--------------------------------------------------------")
#     for x in hasil:
#         print("{:3d}".format(x[0]),
#             "{:20s}".format(x[1]), 
#             "{:15s}".format(x[2]),
#             "{:10d}".format(x[3])),
            
#         print("---------------------------------------------------------")


# conn = connectionDB()
# cursor = conn.cursor()

# while True:
#     menu()
#     inputUser = int(input("masukkan pilihan [1-5] = "))
#     if inputUser == 1:
#         id = int(input("Masukkan id ="))
#         nama_pelanggan = input("Masukkan nama pelanggan =")
#         tarif_daya = input("Masukkan tarif daya = ")
#         tarif_watt = int(input("Masukkan tarif watt ="))
#         insertData(id, nama_pelanggan, tarif_daya, tarif_watt)
                    
#         print("Data sudah terisi")
#     elif inputUser == 2:
#         id = int(input("Masukkan id ="))
#         nama_pelanggan = input("Masukkan nama pelanggan baru =")
#         tarif_daya = input("Masukkan tarif daya baru = ")
#         tarif_watt = int(input("Masukkan tarif watt baru ="))

#         updateData(id, nama_pelanggan, tarif_daya, tarif_watt)
#         print("Berhasil mengedit data")
#     elif inputUser == 3:
#         id = int(input("Masukkan id = "))
#         deleteData(id)
#         print("Data berhasil di hapus")

#     elif inputUser == 4:
#         tampilData()
    
#     elif inputUser == 5:
#         print("program keluar")
#         break
        
    

#SOAL NO 2
import mysql.connector
import datetime as dt
def connectionDB():
    connector = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "pln"

    )
    if connector.is_connected:
        print("Database Terkoneksi")
        return connector
    else:
        print("Database gagal terkoneksi")
        return False

def insertData(resi, pelanggan_id, beban_pengguanaan, tagihan, bulan_tahun, status):
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        sql = "INSERT INTO tagihan (resi, pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        now = dt.datetime.now()
        tanggal_bayar = now.strftime("%Y-%m-%d")
        data = (resi, pelanggan_id, tanggal_bayar, beban_pengguanaan, tagihan, bulan_tahun, status)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambah")
    except mysql.connector.Error as error:
        print("terjadi kesalahan : ", error)
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()
print(">>>> MENAMBAH REKAMAN TABEL TAGIHAN <<<<\n")
resi = int(input("No Resi [00000] :"))
pelanggan_id = int(input("ID pelanggan :"))
beban_pengguanaan = int(input("Beban penggunaan :"))
tagihan = int(input("Jumlah tagihan :"))
bulan_tahun = input("Bulan Tahun :")
status = int(input("Status :"))
insertData(resi, pelanggan_id, beban_pengguanaan, tagihan, bulan_tahun,status)
       
        




#SOAL NO 3


def printStrukDataTabel():

    tanggal = "2024-01-17"
    resi = "1111"
    pelanggan_id = "123"
    nama = "Dimas"
    tarif_daya = "R1M/1200VA"
    beban = "180"
    tagihan = "180000"
    bulan_tahun = "JAN/2024"
    print("")
    print("")
    print(f"Tanggal  : {tanggal}")
    print(f"No Resi  : {resi}")

    print("/n              SRTUK PEMBAYARAN TAGIHAN LISTRIK             ")
    print("-------------------------------------------------------------")
    print(f"ID Pelanggan   : {pelanggan_id}")
    print(f"Nama           : {nama}")
    print(f"Tarif/Daya     : {tarif_daya}")
    print(f"Beban          : {beban}")
    print(f"Rp Tagihan PLN : Rp.{tagihan}")
    print(f"BL/TH          : {bulan_tahun}")
    print("=============================================================")
    print("Petugas")
    print("Joko Mulyo")

struk = printStrukDataTabel()
print(printStrukDataTabel)



    


        