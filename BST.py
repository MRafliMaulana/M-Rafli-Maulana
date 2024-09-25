

# Sample classes for binary and transaksiUser, adjust as per your actual implementation
class Item:
    def __init__(self, sku, hargaBarang, stokItm):
        self.sku = sku
        self.hargaBarang = hargaBarang
        self.stokItm = stokItm

class Binary:
    def __init__(self):
        self.items = {}

    def tambahItem(self, sku, hargaBarang, stokItm):
        self.items[sku] = Item(sku, hargaBarang, stokItm)

    def cari(self, sku):
        return self.items.get(sku)

class Transaksi:
    def __init__(self):
        self.transaksi_list = []

    def tambahTransaksi(self, nama, sku, jumlah, harga):
        self.transaksi_list.append({'nama': nama, 'sku': sku, 'jumlah': jumlah, 'harga': harga})

    def lihatSemua_Transaksi(self):
        table =()
        table.field_names = ["Nama", "SKU", "Jumlah", "Harga"]

        for trans in self.transaksi_list:
            table.add_row([trans['nama'], trans['sku'], trans['jumlah'], trans['harga']])
        
        print(table)

    def SemuaTransaksi_by_totalHarga(self):
        # Implement sorting and display by total harga
        pass

# Initialize classes
binary = Binary()
transaksiUser = Transaksi()

# Add some sample items
binary.tambahItem('12345', 10000, 10)
binary.tambahItem('67890', 20000, 5)

# Main menu loop
while True:
    # Assuming menu_Transaksi is a function that displays the menu
      # Replace with the actual function

    pilihanTrans = int(input("Pilih menu: "))
    if pilihanTrans == 1:
        Nama = input("Masukkan Nama Pelanggan: ")
        while True:
            Sku = input("Masukkan No. SKU barang yang dibeli: ")
            item = binary.cari(Sku)
            if item:
                jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
                if item.stokItm >= jumlah:
                    item.stokItm -= jumlah
                    transaksiUser.tambahTransaksi(Nama, Sku, jumlah, item.hargaBarang)
                    print("Stok Barang dengan No. SKU", Sku, "telah diperbarui.")
                    print("Stok barang saat ini ada: ", item.stokItm)
                else:
                    print("Maaf. Jumlah stok tidak cukup")
            else:
                print("No. SKU yang diinputkan belum terdaftar")
            
            lanjutTransaksi = input("Apakah anda ingin melanjutkan transaksi (y/n)?: ")
            if lanjutTransaksi.lower() != 'y':
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
