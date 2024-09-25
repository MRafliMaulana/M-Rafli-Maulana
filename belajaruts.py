#Membuat Program Sederhana
#Daftar Hadir mahasiswa
data = []
while True:
    print("==================Presensi Mahasiswa===============")
    print("1. Presensi Kelas")
    print("2. Cek kehadiran")
    print("3. Nilai sesuai kehadiran")
    print("4. Keluar")
    print("===================================================")
    opsi = int(input("Masukan opsi [1-4] = "))
    if opsi == 1:
        presensi = input("Masukkan Nama Mahasiswa = ")
        data.append(presensi)
    elif opsi == 2:
        mahasiswaHadir = input("Masukkann nama mahasiswa = ")
        for i in data:
            if i == mahasiswaHadir:
                print("============Kehadiran=============")
                print("1. Tepat waktu")
                print("2. Terlambat")
                inputKehadiran = int(input("Masukkan opsi sesuai waktu kehadiran [1-2] = "))
                if inputKehadiran == 1:
                    print("Kamu Sangat Disiplin = ", i)
                    break
                elif inputKehadiran == 2:
                    print("Kamu kurang disiplin = ", i)
                    break
    elif opsi == 3:
        print("============Nilai Kehadiran=============")
        namaHadir = input("Masukkan nama mahasiswa = ")
        for i in data:
            if i == namaHadir:
                print("Nilai Kehadiran Mahasiswa")
                print("1. Tepat waktu")
                print("2. Terlambat")
                inputHadir = int(input("Masukkan opsi sesuai hadir [1-2] = "))
                if inputHadir == 1:
                    nilai = 100
                    print("Nama Mahasiswa =",i)
                    print("Nilai kamu =",nilai)
                    break
                elif inputHadir == 2:
                    nilai = 75
                    print("Nama Mahasiswa =",i)
                    print("Nilai kamu =",nilai)
                    break
    elif opsi == 4:
        print("Program keluar","Terima Kasih")
        break



                    
        

