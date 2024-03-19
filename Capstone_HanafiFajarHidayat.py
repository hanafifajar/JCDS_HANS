from prettytable import PrettyTable
def header():
    print('-'*60)
    print("ALLURE INDUSTRIES".center(60,'='))
    print('-'*60)
list_barang=[
    {'nama':'folding and pivot doors','stock':9,'harga':1000000,'tipe':2},
    {'nama':'sliding doors','stock':12,'harga':1500000,'tipe':2},
    {'nama':'sliding window','stock':8,'harga':2000000,'tipe':2},
    {'nama':'top hung doors','stock':9,'harga':2000000,'tipe':1},
    {'nama':'top hung window','stock':12,'harga':2500000,'tipe':2},
    {'nama':'ultimo doors','stock':5,'harga':1700000,'tipe':3},
    {'nama':'ultimo window','stock':6,'harga':2100000,'tipe':2}
    ]
tampung=[]
def pretty_table():
    pre=PrettyTable()
    pre.field_names=['Index','Nama','Stock','Tipe Daun','Harga']
    for i in range (len(list_barang)):
        pre.add_row([i,list_barang[i]['nama'],list_barang[i]['stock'],list_barang[i]['tipe'],list_barang[i]['harga']])
    pre.align='l'
    print(pre)
def daftar_barang():
        print('-'*60)
        print("DAFTAR PINTU & JENDELA".center(60,'='))
        print('-'*60)
        pretty_table()
def peringatan_kode_salah():
    print("Kode yang anda masukan salah..")
######## Menu Tampil ########
def recall_tampil():
    while True:
        kondisi=input('kembali ke Menu Tampil? (Y/N) : ')
        if kondisi == 'Y' or kondisi == 'y':
            menu_tampil()
            break
        elif kondisi == 'N' or kondisi == 'n':
            daftar_barang()
            break
        else:
            print("Kode Yang Anda Masukan Salah")
            recall_tampil()
            break
def tampil_data_ke():
    while True:
        try:
            kode_ke=int(input('masukkan Index : '))
        except ValueError:
            print('pastikan input anda menggunakan angka. . . .')
            menu_tampil()
            break
        if kode_ke in range(len(list_barang)):
            pre=PrettyTable()
            pre.field_names=['Index','Nama','Stock','Tipe','Harga']
            pre.add_row([kode_ke,list_barang[kode_ke]['nama'],list_barang[kode_ke]['stock'],list_barang[kode_ke]['tipe'],list_barang[kode_ke]['harga']])
            pre.align='l'
            print(pre)  
            menu_tampil()
        else:
            print('Kode Barang Tidak Ada')
            menu_tampil()
        break
def recall_menu_tampil():
    while True:
        recall=input('kembali ke Menu Utama? (Y/N) : ')
        if recall == 'Y' or recall == 'y':
            menu()
            break
        elif recall == 'N' or recall == 'n':
            menu_tampil()
        else:
            print("Kode Yang Anda Masukan Salah")
            recall_menu_tampil()
        break
def menu_tampil():
    while True :
        print('-'*40)
        print("MENU TAMPIL DATA".center(40))
        print('-'*40)
        print('''
            1. Tampilkan data Barang
            2. Tampilkan kode barang ke-
            3. Kembali ke Menu Utama ''')
        pilihan = input("pilih menu \t:")
        if pilihan == "1":
                tampil()
        elif pilihan == "2":
            if len(list_barang)<=0:
                print('Data masih kosong')
                menu_tampil()
                break    
            else:
                tampil_data_ke()
            break    
        elif pilihan == "3" or pilihan == "Menu Utama":
            recall_menu_tampil()
        else:
            peringatan_kode_salah()
            menu_tampil()  
        break
def tampil():
    while True:
        if len(list_barang)<=0:
            print('Data masih kosong')
            menu_tampil()
            break
        else:
            daftar_barang()
            menu_tampil()
        break  
######## Menu Tambah ########
def menu_tambah():
    while True :
        print('_'*40)
        print("MENU MENAMBAHKAN DATA PRODUK".center(40))
        print('_'*40)
        print('''
            1. Tambah Produk
            2. Kembali ke Menu Utama ''')
        pilihan = input("pilih menu \t:").lower()
        if pilihan == "1" or pilihan == "Tambah Barang":
            tambah()
        elif pilihan == "2" or pilihan == "Menu Utama":
            menu()
        else:
            peringatan_kode_salah()
            menu_tambah()
        break
def ulang():
    while True:        
        ulang=input('anda akan mengulang memasukkan data. (Y/T) : ')
        if ulang=='Y' or ulang=='y':
            tambah()
        elif ulang=='T' or ulang=='t':
            print('anda akan kembali "ke Menu Tambah Barang" . . .')
            menu_tambah()
        else:
            print('input salah..\nanda akan kembali ke "Menu Tambah Barang". ')
            menu_tambah()
        break
def isDigit(angka):
    return angka.isdigit()
def inputAngka(teks):
    userInput=input(teks)
    while not isDigit(userInput):
        print('Format Iput Salah\nInput harus Angka. Coba lagi!')
        print('-'*40)
        userInput=input(teks)
    return userInput
def input_(x):
    while True:
        user_input = input(x)
        if user_input.isdigit() and len(user_input) <= 3:
            return int(user_input)
        else:
            print("Input harus berupa angka dan tidak lebih dari 3 karakter. Silakan coba lagi.")
def nomor(x):
    while True:
        user_input = input(x)
        if user_input.isdigit() and len(user_input) == 12:
            return int(user_input)
        else:
            print("Input harus berupa angka dan harus 12 karakter. Silakan coba lagi.")

def input_harga(x):
    while True:
        user_input = input(x)
        if user_input.isdigit() and len(user_input) >=7:
            return int(user_input)
        else:
            print("Input harus berupa angka dan tidak kurang dari 1juta. Silakan coba lagi.")

def tambah():
    while True:
        print('-'*60)
        print(" MENU TAMBAH PRODUK ".center(60,'='))
        print('-'*60)
        daftar_barang()
        print('Menu Tambah Data'.center(60,'='))
        print('-'*40,)
        nama_produk = input('masukkan nama barang :')
        if any(baru['nama'].lower()==nama_produk.lower() for baru in list_barang):
            print('data sudah ada')
            ulang()
            break
        elif len(nama_produk) >= 20:
            print('nama produk yang anda masukkan lebih dari 20 karakter')
            ulang()
            break
        stock_produk = input_('masukkan jumlah stock barang : ')
        tipe_produk = input_('Masukkan tipe daun pintu/jendela : ')
        harga_produk = input_harga('masukkan harga alat berat : ')                  
        list_barang.append({
        'nama':nama_produk,
        'stock':stock_produk,
        'tipe' : tipe_produk,
        'harga':harga_produk})
        daftar_barang()
        print("Data berhasil ditambahkan...")
        print('_'*40)
        kondisi=input('Apakah anda ingin menambah barang lagi? (Y/N)')
        if kondisi == 'Y' or kondisi == 'y':
            tambah()
            break
        elif kondisi == 'N' or kondisi == 'n':
            menu_tambah()
            break
        else:
            print("Kode Yang Anda Masukan Salah")
            menu_tambah()
        break
######## Menu Edit ########
def menu_edit():
    while True :
        print('-'*60)
        print(" MENU EDIT ".center(60,'='))
        print('-'*60)        
        print('''
            1. Edit Barang
            2. Kembali ke Menu Utama ''')
        pilihan = input("pilih menu \t:").lower()
        if pilihan == "1" or pilihan == "Edit Barang":
            edit()
        elif pilihan == "2" or pilihan == "Menu Utama":
            menu()
        else:
            peringatan_kode_salah()
            menu_edit()
        break
def edit():
    while True:
        daftar_barang()
        try:
            index=int(input('Masukkan Index Alat yang ingin di Update : '))
        except ValueError:
            print('index yang anda masukkan salah...')
            menu_edit()
            break
        if len(list_barang)<=0:
            print('Data masih kosong')
            menu_edit()
            break
        elif index in range(len(list_barang)):
            pre=PrettyTable()
            pre.field_names=['Index','nama','stock','Tipe Daun','harga']
            pre.add_row([index,list_barang[index]['nama'],list_barang[index]['stock'],list_barang[index]['tipe'],list_barang[index]['harga']])
            pre.align='l'
            print(pre)
            print('''
                    1. Edit Sesuai Nama Barang
                    2. Update Jumlah Stock
                    3. Edit Tipe Daun (Pintu / Pendela)
                    4. Edit Harga Barang
                    5. Kembali ke Menu Edit ''')
            pil_edit=inputAngka('pilihan menu \t:')
            if pil_edit == '1':
                nama_lama = list_barang[index]['nama']
                nama_baru = input('Nama Alat Baru akan di Edit Menjadi : ')
                new_nama=nama_baru.strip()
                if any(baru['nama'].lower()==nama_baru.lower() for baru in list_barang):
                    print('nama barang sama')
                    edit()
                    break
                elif nama_baru!=new_nama:
                    print('nama mengandung spasi')
                    edit()
                else:
                    list_barang[index]['nama'] = nama_baru
                    print(nama_lama+" telah diganti menjadi "+nama_baru)
                    edit()
            elif pil_edit == '2':
                stock_lama = list_barang[index]['stock']
                stock_baru = input_('Masukkan Jumlah Stock Terbaru : ')
                list_barang[index]['stock'] = stock_baru
                print(f'jumlah stock telah diperbaharui dari {stock_lama} menjadi {stock_baru}')
                edit()
            elif pil_edit == '3':
                tipe_lama = list_barang[index]['tipe']
                tipe_baru = input_('Masukkan Jumlah Tipe Daun Terbaru : ')
                list_barang[index]['tipe'] = tipe_baru
                print(f'jumlah Tipe Daun telah diperbaharui dari {tipe_lama} menjadi {tipe_baru}')
                edit()
            elif pil_edit == '4':
                harga_lama = list_barang[index]['harga']
                harga_baru = input_harga('Masukkan Harga Terbaru : ')
                list_barang[index]['harga'] = harga_baru
                print(f'Harga telah diperbaharui dari Rp. {harga_lama} menjadi Rp. {harga_baru}')
                edit()
            elif pil_edit == '5':
                menu_edit()
            else:
                peringatan_kode_salah()
                edit()
            break
        else:
            peringatan_kode_salah()
            edit()
        break
######## Menu Hapus ########
def menu_hapus():
    while True:
        print('-'*60)
        print(" MENU HAPUS ".center(60,'='))
        print('-'*60)
        print('''
            1. Hapus Barang
            2. Kembali ke Menu Utama ''')
        pilihan = inputAngka("pilih menu \t:").lower()
        if pilihan == "1" or pilihan == "hapus barang":
            hapus()
        elif pilihan == "2" or pilihan == "kembali" or pilihan == "kembali ke menu utama" or pilihan == "menu utama":
            menu()
        else:
            peringatan_kode_salah()
            menu_hapus()
        break
def hapus():
    while True:
        if len(list_barang)<=0:
            print('Data masih kosong')
            menu_hapus()
            break
        else:
            daftar_barang()
            hapus=int(input('Masukkan Index Alat yang ingin dihapus : '))
            if hapus in range(len(list_barang)):
                pre=PrettyTable()
                pre.field_names=['Index','nama','stock','tipe','harga']
                pre.add_row([hapus,list_barang[hapus]['nama'],list_barang[hapus]['stock'],list_barang[hapus]['tipe'],list_barang[hapus]['harga']])
                pre.align='l'
                print(pre)
                yakin=input('yakin ingin menghapus data ini? (Y/N) : ')
                if yakin=='Y' or yakin=='y':
                    del list_barang[hapus]
                    print('DATA TELAH TERHAPUS')
                    menu_hapus()
                    break
                elif yakin=='N' or yakin=='n':
                    print('HAPUS DATA DIBATALKAN')
                    menu_hapus()
                else:
                    print('input yang anda masukkan salah')
                    menu_hapus()
                    break
            else:
                print("Barang yang ingin anda hapus tidak tersedia.")
                menu_hapus()
            break
######## Keluar ########
def keluar():
            print('-'*60)
            print(" TERIMAKASIH ".center(60,'='))
            print('-'*60)
######## PEMESANAN ########
dict_trx={}
dafar_metode_pembayaran={
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash On Delivery",
    4:"Kartu Credit"
}

def owner():
    daftar_barang()
    while True:
        index=int(input('Masukkan Index Barang yang ingin dipesan : '))
        qty=int(input('Masukkan jumlah yang ingin dipesan : '))
        if(qty>list_barang[index]['stock']):
            print(f"Stock tidak cukup, stock {list_barang[index]['nama']} tersedia = {list_barang[index]['stock']}")
        elif(qty<=list_barang[index]['stock']):
            tampung.append([list_barang[index]['nama'],qty,list_barang[index]['tipe'],list_barang[index]['harga'],index])
        else:
            print('input yang anda masukkan salah')
            owner()
            break
        print('Pesanan :')
        pre = PrettyTable()
        pre.field_names = ['Nama', 'Stock', 'Harga','Tipe Daun', 'Total Harga']
        for item in tampung:
            pre.add_row([item[0], item[1], item[2],item[4],item[3]])
        print(pre)
        checker=input('Mau Beli yang Lain? (Y/T)  : ')
        if (checker=='Y') or (checker=='y'):
            continue
        elif(checker=='T') or (checker=='t'):
            print('Daftar Belanja:')
            pre = PrettyTable()
            pre.field_names = ['Nama', 'Stock', 'Harga', 'Total Harga']
            totalHarga = 0
            for item in tampung:
                total_item_harga = item[1] * item[3]
                pre.add_row([item[0], item[1], item[3], total_item_harga])
                totalHarga += total_item_harga
            print(pre)
            ppn=6/100
            harga_setelah_ppn=totalHarga*ppn
            total_keseluruhan=totalHarga+harga_setelah_ppn
            print(f'Total harga + PPN(6%) = {total_keseluruhan}')
            nama    =input("Nama Penerima       : ")
            while not nama.replace(' ','').isalpha():
                print("Nama hanya boleh berisi huruf.")
                nama = input("Nama Penerima       : ")
            alamat  =input("Alamat Penerima     : ")
            telepon =nomor("Nomor HP Penerima   : ")
            dict_trx = {
                "Nama Penerima":nama,
                "Alamat Penerima":alamat,
                "No HP":telepon,
            }
            for i in dafar_metode_pembayaran:
                print("ID Pembayaran : ",i,"\t Metode Pembayaran : ",dafar_metode_pembayaran[i])
            try:
                pilih_metode = int(input("Pilih ID metode Pembayaran : "))[:1]
                if pilih_metode in dafar_metode_pembayaran:
                    print("Nama Penerima    : ", dict_trx["Nama Penerima"])
                    print("Alamat Penerima  : ", dict_trx["Alamat Penerima"])
                    print("No HP            : ", dict_trx["No HP"])
                    print("Total Harga      : ", total_keseluruhan)
                    print("Metode Pembayaran: ", dafar_metode_pembayaran[pilih_metode])
                    pemesanan()
                    break
                else:
                    print("ID metode pembayaran tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid untuk ID metode pembayaran.\tAnda akan kembali ke menu pemesanan")
                pemesanan()
            break
        else:
            print('inputan salah\tAnda akan mengulang proses pemesanan')
            tampung.clear()
            owner()
            break
def pemesanan():
    print('-'*60)
    print(" MENU PEMESANAN ".center(60,'='))
    print('-'*60)
    while True:  
        print('''
            *PILIH CUSTOMER*
                1. Owner 
                2. Kembali ke Menu Utama ''')
        pil_cus = inputAngka('pilih Menu \t: ')
        if pil_cus == '1' :
            owner()
            break
        elif pil_cus == '2' :
            menu()
        else:
            peringatan_kode_salah()
            pemesanan()
        break
######## Menu Utama ########
def menu():
    while True :
        header()
        print('''
            1. Menu Tampil 
            2. Menu Tambah Barang
            3. Menu Update Barang
            4. Menu Hapus Barang 
            5. Pemesanan                          
            6. Keluar ''')
        pilihan = inputAngka("pilih menu \t:")
        if pilihan == "1" :
            menu_tampil()
        elif pilihan == "2" :
            menu_tambah()
        elif pilihan == "3" :
            menu_edit()
        elif pilihan == "4" :
            menu_hapus()
        elif pilihan == "5" :
            pemesanan()
        elif pilihan == "6" :
            keluar()
        else:
            print('input yang anda masukkan tidak tersedia')
            menu()
        break
######## Menu ########
menu()