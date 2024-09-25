class Node:
    def __init__(self, Sku, Nama, hargaBarang, stokItm):
        self.Sku = Sku
        self.Nama = Nama
        self.hargaBarang = hargaBarang
        self.stokItm = stokItm
        self.right = None
        self.left = None

class BinaryScrhTree:
    def __init__(self):
        self.root = None
    def input(self, Sku, Nama, hargaBarang, stokItm):
        if not self.root:
            self.root = Node(Sku, Nama, hargaBarang, stokItm)
        else:
            self.inputan(self.root, Sku, Nama, hargaBarang, stokItm)
    def inputan(self, banding, Sku, Nama, hargaBarang, stokItm):
        if Sku < banding.Sku:
            if banding.left is None:
                banding.left = Node(Sku, Nama, hargaBarang, stokItm)
            else:
                self.inputan(banding.left, Sku, Nama, hargaBarang, stokItm)
        elif Sku > banding.Sku:
            if banding.right is None:
                banding.right = Node(Sku, Nama, hargaBarang, stokItm)
            else:
                self.inputan(banding.right, Sku, Nama, hargaBarang, stokItm)
        else:
            print("SKU sudah terdata di dalam stok Item")
    
    def cari(self, Sku):
        return self.pencarian(self.root, Sku)
    def pencarian(self, banding, Sku):
        if not banding:
            return None
        if Sku == banding.Sku:
            return banding
        elif Sku < banding.Sku:
            return self.pencarian(banding.left, Sku)
        else:
            return self.pencarian(banding.right, Sku)
    
    def pembaruan_stokItem(self, Sku, barangBaru):
        item = self.cari(Sku)
        if item:
            item.stokItm += barangBaru
            print("Stok Item dengan no SKU",Sku,"telah di perbarui. Stok barang sekarang: ",item.stokItm)
        else:
            print("SKU",Sku, "tidak terdaftar. silahkan input data terlebih dahulu.")


class Transaksi:
    def __init__(self, Nama, Sku, jumlah, totalHarga):
        self.Nama = Nama
        self.Sku = Sku
        self.jumlah = jumlah
        self.totalHarga = totalHarga

class TransaksiList:
    def __init__(self):
        self.transaksi = []
    
    def tambahTransaksi(self, Nama, Sku, jumlah, hargaBarang):
        totalHarga = jumlah * hargaBarang
        self.transaksi.append(Transaksi(Nama, Sku, jumlah, totalHarga))
        print("Data Transaksi Pelanggan Berhasil Diinputkan")
    def lihatSemua_Transaksi(self):
        for trans in self.transaksi:
            print("Nama Pelanggan: ",trans.Nama, "SKU: ",trans.Sku, "Jumlah Item Beli: ",trans.jumlah, "Total Harga: ",trans.totalHarga)
    def SemuaTransaksi_by_totalHarga(self):
        sortingTransaksi = sorted(self.transaksi, key = lambda r: r.totalHarga, reverse = True)
        for trans in sortingTransaksi:
            print("Nama Pelanggan: ",trans.Nama, "SKU: ",trans.Sku, "Jumlah Item Beli: ",trans.jumlah, "Total Harga: ",trans.totalHarga)




def menuUtama():
    print("============== Menu Utama ===============")
    print("1. Kelola Stok Barang")
    print("2. Kelola Transaksi Pelanggan")
    print("0. Keluar Program")

def Menus_stokBranag():
    print("============= Menu Kelola Stok Barang ==============")
    print("1. Input Data Stok Barang")
    print("2. Restok Barang")
    print("0. Kembali ke Menu Utama")

def menu_Transaksi():
    print("============ Menu Transaksi Pelanggan =============")
    print("1. Input Data Transaksi Baru")
    print("2. Lihat Data Seluruh Transaksi Pelnggan")
    print("3. Lihat Data Transaksi Berdasarkan Subtotal")
    print("0. Kemabali ke Menu Utama")



binary = BinaryScrhTree()
transaksiUser = TransaksiList()

while True:
        menuUtama()
        intiPilihan = int(input("Pilih salah satu menu diatas [1,2,0]: "))
        if intiPilihan == 1:
            while True:
                Menus_stokBranag()
                pilihanBrg = int(input("Pilih menu: "))
                if pilihanBrg == 1:
                    Sku = input("Masukkan No. SKU [4 digit]: ")
                    if binary.cari(Sku):
                        print("SKU sudah terdaftar dalam stok barang.")
                    else:
                        Nama = input("Masukkan Nama Barang: ")
                        hargaBarang = float(input("Masukkan Harga Satuan: "))
                        stokItm = int(input("Masukkan Jumlah Stok: "))
                        binary.input(Sku, Nama, hargaBarang, stokItm)
                        print("Barang dengan No. SKU" ,Sku, "telah di tambahkan")

                elif pilihanBrg == 2:
                    Sku = input("Masukkan No. SKU: ")
                    item = binary.cari(Sku)
                    if item:
                        barangBaru = int(input("Masukkan Jumlah Stok Baru: "))
                        binary.pembaruan_stokItem(Sku, barangBaru)
                    else:
                        print("SKU", Sku, "tidak terdftar. Silahkan input data terlebih dahulu.")
                    
                elif pilihanBrg == 0:
                    print("Anda kemabli ke menu utama")
                    break
                
                else:
                    print("Pilihan tidak valid")
                
        elif intiPilihan == 2:
            while True:
                menu_Transaksi()
                pilihanTrans = int(input("Pilih menu: "))
                if pilihanTrans == 1:
                    Nama = input("Masukkan Nama Pelanggan: ")
                    while True:
                        Sku = input("Masukkan No. SKU barang yang dibelli: ")
                        item = binary.cari(Sku)
                        if item:
                            jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
                            if item.stokItm >= jumlah:
                                item.stokItm -= jumlah
                                transaksiUser.tambahTransaksi(Nama, Sku, jumlah, item.hargaBarang)
                                print("Stok Barang dengan No. SKU", Sku, "telah diperbarui. Stok saat ini: ",item.stokItm)
                            else:
                                print("Jumlah stok tidak cukup")
                        else:
                            print("No. SKU yang diinputkan belum terdaftar")
                        
                        lanjutTransaksi = input("Apakah anda ingin melanjutkan transaksi (Y/N)?: ")
                        if lanjutTransaksi.lower() == 'n' or 'N':
                            break
                
                elif pilihanTrans == 2:
                    transaksiUser.lihatSemua_Transaksi()
                elif pilihanTrans == 3:
                    transaksiUser.SemuaTransaksi_by_totalHarga()
                elif pilihanTrans == 0:
                    print("Anda kembali ke menu utama")
                    break
                else:
                    print("Pilihan menu tidak valid")
        
        elif intiPilihan == 0:
            print("Terima Kasih telah menggunakan programm ini :)")
            print("Program Selesai")
            break

        else:
            print("Pilihan menu tidak valid")

    







