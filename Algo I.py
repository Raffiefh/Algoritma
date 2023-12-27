# # Mengimport CSV
import csv
# # Mengimport sistem fitur Clear()
import os
import collections
# # Mengimport pandas 
import pandas as pd
# # Mengimport sistem waktu
import datetime
# # Fungsi Clear 
def Clear():
    import platform

    if platform.system() == "Linux":
        print("\x1b[H\x1b[2J")
    elif platform.system() == "Darwin":
        print("\033[2J\033[;H")
    elif platform.system() == "Windows":
        os.system("cls")
Clear()
# # Pembuka 
def Logo():
    print("            ")
    print("            ")
    print("           ███╗░░░███╗░█████╗░░██████╗░██╗░░░██╗")
    print("           ████╗░████║██╔══██╗██╔════╝░██║░░░██║")
    print("           ██╔████╔██║███████║██║░░██╗░██║░░░██║")
    print("           ██║╚██╔╝██║██╔══██║██║░░╚██╗██║░░░██║")
    print("           ██║░╚═╝░██║██║░░██║╚██████╔╝╚██████╔╝")
    print("           ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░")
    print("            ")
Logo()
print(f"{'='*7}=============================================={'='*7}")
print(f"{'='*7}   Selamat datang di Manajemen Gudang Utama   {'='*7}")
print(f"{'='*7}=============================================={'='*7}")

# # Fungsi Register dipaling awal
def Register():
    Clear()
    Logo()
    print(f"{'='*7}=========================================={'='*7}")
    print(f"{'='*7} Selamat datang di Regis Manajemen Gudang {'='*7}")
    print(f"{'='*7}=========================================={'='*7}")
    Username  = input("Daftarkan Username     : ")
    Password  = input("Beri Password          : ")
    N_Pekerja = input("Pekerjaan[Admin]/[Staf]: ")
    
    #
    if len(Username) < 5:
        print(" ")
        print("Data Akun Gagal terinput, Username harus lebih dari 5 huruf")
        print(" ")
        return
    
    # Membaca file CSV
    with open('Gudang_Akun.csv', "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        data_akun = []
        for row in csv_reader:
            data_akun.append({"Username": row[0], "Password": row[1], "Pekerjaan": row[2]})

    # Memeriksa username apa sudah ada
    username_tersedia = False
    for akun in data_akun:
        if Username == akun["Username"]:
            print("Mohon maaf username sudah ada, harap ganti kembali")
            username_tersedia = True
            

    # Menambahkan data baru di file CSV
    if not username_tersedia:
        data_baru = {"Username": Username, "Password": Password, "Pekerjaan": N_Pekerja}
        with open('Gudang_Akun.csv', "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data_baru.keys())
            writer.writerow(data_baru)
 
    
# # # Tempat Penyimpanan Fungsi fitur Homepage dan Homepagenya
# # Fungsi-fungsi fitur Pertama membuat fitur Login
waktu_login = datetime.datetime.now()
tanggal_login = waktu_login.date()


# # Fungsi-fungi fitur ke-2 Manage_barang
def tampilkan_data():
    Clear()
    print(f"{'='*5}      Data Barang Gudang Utama     {'='*5}")
    Gudang_Barang =[]

    with open('Gudang_Barang.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
            Gudang_Barang.append({'Kode':row[0],'Nama':row[1], 'Indeks' :row[2],'Asal' :row[3],'Gudang' :row[4]})
    df = pd.DataFrame(Gudang_Barang)
    print(df)

def tambah_data():
    Clear()
    print(f"{'='*5}================================================={'='*5}")
    print(f"{'='*5}   Anda Berada di Menu Tambah Data atau Barang   {'='*5}")
    print(f"{'='*5}================================================={'='*5}")
    print(f"{'='*5}        Sebelum melakukan penambahan barang      {'='*5}")
    print(f"{'='*5}          Harap baca syarat-syarat berikut       {'='*5}")
    print(f"{'='*5} 1.)Nomor dan nama barang tidak boleh sama       {'='*5}")
    print(f"{'='*5} 2.)Harap dilihat data sebelum melakukan + barang{'='*5}")
    print(f"{'='*5} 3.)Lokasi barang diisi dengan kata 'Utama'      {'='*5}")
    print(f"{'='*5} 4.)Data yang masuk akan diberikan informasi     {'='*5}")
    print(f"{'='*5}================================================={'='*5}")
    print("BARANG YANG ADA DIGUDANG UTAMA:")
    Gudang_Barang =[]

    with open('Gudang_Barang.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
            Gudang_Barang.append({'Kode':row[0],'Nama':row[1], 'Indeks' :row[2],'Asal' :row[3],'Gudang' :row[4]})
    df = pd.DataFrame(Gudang_Barang)
    print(df)

            
    while(True) :
        Penambahan= input("Lanjutkan menambahkan barang [Y/N] :")
        if Penambahan== "Y" :
            Kode_Barang  = input("Masukkan Nomor Kode Barang: ")
            Nama_Barang  = input("Masukkan Nama Barang      : ")
            Indeks_Barang= input("Masukkan Berat Barang     : ")
            Asal_Barang  = input("Masukkan Asal mula Barang : ")
            Gudang_Barang= input("Masukkan Lokasi Barang    : ")
            
            if Kode_Barang == " ":
                print(" ")
            if Nama_Barang == " ":
                print(" ")
            if Indeks_Barang == " ":
                print(" ")
            if Asal_Barang == " ":
                print(" ")
            if Gudang_Barang == " ":
                print(" ")
            
            new_data = {'Kode': Kode_Barang, 'Nama': Nama_Barang, 'Indeks ' : Indeks_Barang, 'Asal': Asal_Barang, 'Gudang': Gudang_Barang }
            with open ('Gudang_Barang.csv', 'a', newline='') as file :
                write = csv.DictWriter(file, fieldnames=new_data.keys())
                write.writerow(new_data)
            print("Data anda berhasil dimasukkan")
            

        elif Penambahan == "N" :
            Clear()
            break
def hapus_data():
  while True:
    Clear()
    print(f"{'='*5}=================================================={'='*5}")
    print(f"{'='*5}   Anda berada di Menu Hapus Barang atau Data     {'='*5}")
    print(f"{'='*5}=================================================={'='*5}")
    print(f"{'='*5}        Sebelum melakukan pembuangan barang       {'='*5}")
    print(f"{'='*5}          Harap baca syarat-syarat berikut        {'='*5}")
    print(f"{'='*5} 1.)Kode &barang digunakan untuk menghapus1 baris {'='*5}")
    print(f"{'='*5} 2.)Barang yang dihapus tidak bisa dikembalikan   {'='*5}")
    print(f"{'='*5} 3.)Sesuaikan Kode &Barang yang akan dihapus      {'='*5}")
    print(f"{'='*5} 4.)Data yang tersisa akan diberikan informasi    {'='*5}")
    print(f"{'='*5}=================================================={'='*5}")
    print("DATA BARANG YANG TERSISA DIGUDANG UTAMA: ")
    Gudang_Barang =[]

    with open('Gudang_Barang.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
            Gudang_Barang.append({'Kode':row[0],'Nama':row[1], 'Indeks' :row[2],'Asal' :row[3],'Gudang' :row[4]})
    df = pd.DataFrame(Gudang_Barang)
    print(df)
    print(f"{'='*5}================================================{'='*5}")
    Perintah=input("Lanjutkan pembuangan barang[Y/N]: ")
    if Perintah == "Y":   
     Kode   =input("Masukkan kode barang yang ingin dihapus        : ")
     Nama   =input("Masukkan nama barang yang ingin dihapus        : ")
     # Mencarinya menggunakan ini
     with open("Gudang_Barang.csv", "r") as f:
        data = f.readlines()    
     baris_dihapus = None
     # Digunakan untuk mencari barisan i daam data list
     for i in range(len(data)):
         if data[i].split(",")[0] == Kode and data[i].split(",")[1] == Nama:
             baris_dihapus = data[i]
             break
     if baris_dihapus is not None:
        data.remove(baris_dihapus)
     # Melakukan penghapusan menggunakan metode write dalam csv 
     with open("Gudang_Barang.csv", "w") as f:
        for baris in data:
            f.write(baris)
     print(f"{'='*5}============ Data berhasil dihapus ============={'='*5}")
     Perintah=input("Lanjutkan pembuangan barang[Y/N]:")
     Clear()
     break
    else:
     Clear()
     break  
# #Homepage fitur ke-2
def Manage_Barang():
 while True:
    print(f"{'='*5}===================================={'='*5}")
    print(f"{'='*5}         Menu Manage Barang         {'='*5}")
    print(f"{'='*5}===================================={'='*5}")
    print(f"{'='*5}   Menampilkan barang Gudang [1]    {'='*5}")
    print(f"{'='*5}   Menambahkan barang Gudang [2]    {'='*5}")
    print(f"{'='*5}    Membuang barang Gudang   [3]    {'='*5}")
    print(f"{'='*5}            Keluar [0]              {'='*5}")
    print(f"{'='*5}===================================={'='*5}")
    Perintah = str(input("Perintah :"))

    if Perintah == "1":
        Clear()
        tampilkan_data()
        Manage_Barang()
        break
    elif Perintah == "2":
        Clear()
        tambah_data()
        Manage_Barang()
        break
    elif Perintah == "3":
        Clear()
        hapus_data()
        Manage_Barang()
        break
    elif Perintah == "0":
        Clear()
        break      
    else:
        print("Pilihan tidak valid")
        Manage_Barang() 
# # Batas-2

# # Fungsi-fungsi fitur ke-3 Manage_Pengiriman
def kirimkan_barang():
   Clear()
   while True:
    print(f"{'='*5}============================================={'='*5}")
    print(f"{'='*5}    Anda berada di Menu Pengiriman Barang    {'='*5}")
    print(f"{'='*5}============================================={'='*5}")
    print(f"{'='*5} 1.) Sebelum melakukan pengiriman Harap Cek  {'='*5}")
    print(f"{'='*5} dan persiapkan Kode dan Nama barang         {'='*5}")
    print(f"{'='*5} 2.) Barang yang dikirim tidak dapat di -    {'='*5}")
    print(f"{'='*5} kembalikan.Siapkan tujuan ex :[Gudang.csv]  {'='*5}")
    print(f"{'='*5} 3.) Barang yang tercatat akan terkirim  dan {'='*5}")
    print(f"{'='*5} tercatat di riwayat pengiriman              {'='*5}")
    print(f"{'='*5}============================================={'='*5}")
    Perintah = str(input("Lanjutkan pengiriman barang[Y/N]: "))
    if Perintah == "Y":
     Clear()
    #  Untuk menampilkan Data Gudang yang tersedia saat ini.
     print(f"{'='*5}================================================{'='*5}")
     print("Gudang yang terkontrak saat ini :")
     Total_Gudang=[]
     with open('Total_Gudang.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
          Total_Gudang.append({'Jenis_Gudang':row[0]})
     df = pd.DataFrame(Total_Gudang)
     print(df)
     print(f"{'='*5}================================================{'='*5}")
     # Bagian coding untuk mengcopy dan mengirimkan barang
     print("Contoh Tujuan Gudang : Gudang_Bekasi.csv")
     Tujuan=str(input("Tujuan Pengiriman barang: "))
     print(f"{'='*5}================================================{'='*5}")
     print("DATA BARANG YANG ADA DI GUDANG UTAMA: ")
     Gudang_Barang =[]

     with open('Gudang_Barang.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
            Gudang_Barang.append({'Kode':row[0],'Nama':row[1], 'Indeks' :row[2],'Asal' :row[3],'Gudang' :row[4]})
        df = pd.DataFrame(Gudang_Barang)
        print(df)
     print(f"{'='*5}================================================{'='*5}")
     print("Tuliskan sesuai data yang ada,\nKesalahan penulisan akan menyebabkan kehilangan DATA!!!")
     Kode_Barang= input("Masukkan kode Barang yang akan dikirimkan: ")
     Nama_Barang= input("Masukkan nama Barang yang akan dikirimkan: ")
     # Mencari data barang berdasarkan kode dan nama
     for barang in Gudang_Barang:
      if barang["Kode"] == Kode_Barang and barang["Nama"] == Nama_Barang:
          
        with open( Tujuan , "a") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([barang["Kode"], barang["Nama"], barang["Indeks"], barang["Asal"], barang["Gudang"],Tujuan])


        # Menambahkan data barang ke file Riwayat_Pengiriman.csv
        with open("Riwayat_Pengiriman.csv", "a") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([barang["Kode"], barang["Nama"], barang["Indeks"], barang["Asal"], barang["Gudang"], Tujuan])
        
        # Menghapus data barang dari file Gudang_Barang.csv
        with open("Gudang_Barang.csv", "r") as f:
            data = f.readlines()    
            baris_dihapus = None
            for i in range(len(data)):
                if data[i].split(",")[0] == Kode_Barang and data[i].split(",")[1] == Nama_Barang:
                    baris_dihapus = data[i]
                    break
        if baris_dihapus is not None:
            data.remove(baris_dihapus)
        with open("Gudang_Barang.csv", "w") as f:
            for baris in data:
                f.write(baris)
        Clear()
        # Menampilkan data barang yang telah dikirim
        print(f"Data barang yang telah dikirim: \n{barang}")
        break
    else :
        Clear()
        break
def data_kirim():
   while True:
    Clear()
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5}     Informasi Riwayat Pengiriman    {'='*5}")
    print(f"{'='*5}====================================={'='*5}")
    Pertanyaan = input("Melanjutkan melihat Riwayat[Y]/[N]:")
    if Pertanyaan =="Y":
      print(f"Membuka Riwayat Pengiriman : ....")
      print(f"{'='*5}====================================={'='*5}")
      with open("Riwayat_Pengiriman.csv", "r") as file:
        reader = csv.reader(file)
        # Membuat DataFrame dari data pengiriman
        df = pd.DataFrame(reader)
        print(df) 
      print(f"{'='*5}====================================={'='*5}")
      Pertanyaan = input("Melanjutkan melihat isi gudang [Y]/[N]:")
      Clear()
      break
    else:
      Clear()
      break
def Tampilkan_Gudang():
    Clear()
    while True:
        print(f"{'='*5}====================================={'='*5}")
        print(f"{'='*5}       Informasi Total Gudang        {'='*5}")
        print(f"{'='*5}====================================={'='*5}")
        Pertanyaan = input("Melanjutkan Informasi Total Gudang[Y]/[N]:")
        if Pertanyaan =="Y":
         print(f"Membuka Informasi banyak gudang : ....")
         print(f"{'='*5}====================================={'='*5}")
         Total_Gudang=[]
         with open('Total_Gudang.csv','r') as file:
          read = csv.reader(file, delimiter=",")
          for row in read:
           Total_Gudang.append({'Jenis_Gudang':row[0]})
         df = pd.DataFrame(Total_Gudang)
         print(df)
         print(f"{'='*5}====================================={'='*5}")
         Pertanyaan = input("Melanjutkan Informasi Total Gudang [Y]/[N]:")
         Clear()
         break
        else:
           Clear()
           break
# # Homepage fitur ke-3
def Manage_Pengiriman():
   Clear()
   while True:
    print(f"{'='*5}======================================={'='*5}")
    print(f"{'='*5}          Menu Manage Pengiriman       {'='*5}")
    print(f"{'='*5}======================================={'='*5}")
    print(f"{'='*5}          Pengiriman Barang      [1]   {'='*5}")
    print(f"{'='*5}          Riwayat Pengiriman     [2]   {'='*5}")
    print(f"{'='*5}              Total Gudang       [3]   {'='*5}")
    print(f"{'='*5}               Keluar [0]              {'='*5}")
    print(f"{'='*5}======================================={'='*5}")
    Perintah = str(input("Perintah :"))
    if Perintah == "1":
        Clear()
        kirimkan_barang()
        Manage_Pengiriman()
        break
    elif Perintah == "2":
        Clear()
        data_kirim()  
        Manage_Pengiriman()  
        break
    elif Perintah == "3":
        Clear()
        Tampilkan_Gudang()
        Manage_Pengiriman()
        break
    else:
        Clear()
        break
# # Batas-3

# # Fungsi-fungsi fitur ke-4 Manage_Gudang
# # Homepage fitur ke-4
def Tampil_Gudang():
    print(f"{'='*5}====================================={'='*5}")
    Total_Gudang = []

    with open('Total_Gudang.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            Total_Gudang.append({'Jenis_Gudang': row[0]})
    df = pd.DataFrame(Total_Gudang)
    print(df)
    print(f"{'='*5}====================================={'='*5}")
def Manage_Gudang_Lain():
  while True:     
   print(f"{'='*5}==================================={'='*5}")
   print(f"{'='*5}      Menu Manage Gudang Lain      {'='*5}")
   print(f"{'='*5}==================================={'='*5}")
   print(f"{'='*5}      Penambahan Gudang Lain   [1] {'='*5}")
   print(f"{'='*5} Informasi Barang Gudang Lain  [2] {'='*5}")
   print(f"{'='*5}       Menghapus Gudang lain   [3] {'='*5}")
   print(f"{'='*5}            Keluar   [0]           {'='*5}")
   print(f"{'='*5}==================================={'='*5}")
   Perintah=input("Perintah: ")
   if Perintah == "1" :
      Clear()
      Tampil_Gudang()
      print(f"{'='*5}====================================={'='*5}")
      print(f"{'='*5}    Syarat Mengkontrak Gudang Lain   {'='*5}")
      print(f"{'='*5}====================================={'='*5}")
      print(f"{'='*5}  1.) Nama Gudang tidak boleh sama   {'='*5}")
      print(f"{'='*5}  2.) Akhir nama Gudang dilengkapi   {'='*5}")
      print(f"{'='*5}   dengan contoh [ Nama.csv ]        {'='*5}")
      print(f"{'='*5}  3.) Contoh : Gudang_Bekasi.csv     {'='*5}")
      print(f"{'='*5}====================================={'='*5}")  
      Pertanyaan=input("Lanjutkan menambahkan Gudang[Y]/[N]: ")
      if Pertanyaan == "Y" : 
        Tambah_Gudang = input("Masukkan nama Gudang :")
        with open(Tambah_Gudang, "w") as f:
          f.write("'Kode','Nama', 'Indeks','Asal','Gudang'\n")
          new_data = {"Jumlah_Gudang" : Tambah_Gudang}
        with open ('Total_Gudang.csv', 'a', newline='') as f :
            write = csv.DictWriter(f, fieldnames=new_data.keys())
            write.writerow(new_data)
        print(f"{'='*4}==========================================={'='*4}")
        print(f"{'='*4} Gudang berhasil dikontrak / ditambahkan $ {'='*4}")
        print(f"{'='*4}==========================================={'='*4}")
        Pertanyaan=input("Lanjutkan menambahkan Gudang[Y]/[N]: ")
        Clear()
        Manage_Gudang_Lain()
      else:
           Clear()
           Manage_Gudang_Lain()
           break
           
   elif Perintah == "2" :
    Clear()
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5}    Informasi Barang Gudang Lain     {'='*5}")
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5} Untuk melihat Informasi Gudang lain {'='*5}")
    print(f"{'='*5}  Masukkan nama Gudang Cabang dengan {'='*5}")  
    print(f"{'='*5}  Contoh: Gudang_Bekasi.csv          {'='*5}")
    print(f"{'='*5}====================================={'='*5}") 
    Tampil_Gudang()
    Pertanyaan = input("Melanjutkan melihat isi Gudang[Y]/[N]:")
    if Pertanyaan =="Y":
      Buka_Gudang=input("Masukkan nama Gudang : ")
      try:
        with open(Buka_Gudang, "r") as file:
            pass
      except FileNotFoundError:
        Clear()
        print("Gudang tidak tersedia")
        Manage_Gudang_Lain()
        break
        
      print(f"Membuka {Buka_Gudang}: ....")
      print(f"{'='*5}==============================================={'='*5}")
      with open(Buka_Gudang, "r") as file:
            reader = csv.reader(file)
            df = pd.DataFrame(reader)
            print(df)
      print(f"{'='*5}==============================================={'='*5}")
    
      Pertanyaan = input("Melanjutkan melihat isi gudang [Y]/[N]:")
      Clear()
    else:
        Clear()
        Manage_Gudang_Lain()
        break
        
   
   elif Perintah =="3":
      Clear()
      print(f"{'='*5}===================================={'='*5}")
      print(f"{'='*5}    Menghapus Kontrak Gudang Lain   {'='*5}")
      print(f"{'='*5}===================================={'='*5}")
      print(f"{'='*5} Untuk menghapus Gudang lainnya     {'='*5}")
      print(f"{'='*5} Masukkan nama Gudang Cabang dengan {'='*5}")
      print(f"{'='*5} Contoh: Gudang_Bekasi.csv          {'='*5}")
      print(f"{'='*5} Untuk menghapus.                   {'='*5}")
      print(f"{'='*5}===================================={'='*5}") 
      Tampil_Gudang()
      Pertanyaan = input("Lanjutkan menghapus kontrak [Y]/[N]: ")
      if Pertanyaan =="Y":
        Nama=      input("Masukkan nama Gudang : ")
        with open("Total_Gudang.csv", "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            gudang = []
            for row in csv_reader:
             gudang.append(row[0])
             if Nama not in gudang:
                Clear()
                print("Gudang tidak terdata")
                break

        try:
            os.remove(Nama)
            Clear()
            with open("Total_Gudang.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                gudang = []
                for row in reader:
                    gudang.append(row)

            index_gudang = 0
            for i in range(len(gudang)):
                if gudang[i][0] == Nama:
                    index_gudang = i
                    break

            del gudang[index_gudang]

            with open("Total_Gudang.csv", "w", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                for gudang in gudang:
                    writer.writerow(gudang)

            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5}  Data berhasil dihapus kontraknya  {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
        except FileNotFoundError:
            Clear()
            Tampil_Gudang()
            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5}        File tidak ditemukan        {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
            Pertanyaan = input("Lanjutkan menghapus kontrak[Y]/[N]:")       
            Clear()
        
      else:
        Clear()
        Manage_Gudang_Lain()
        break
        
      
   else:
       Clear()
       break
# # Batas-4

# # Fungsi-fungsi fitur ke-5 Manage_Staf
def Data_Pekerja():
  while True:
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5}        Informasi Data Pekerja       {'='*5}")
    print(f"{'='*5}====================================={'='*5}")
    Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
    if Pertanyaan =="Y":
      print(f"Membuka Data para pekerja: ....")
      print(f"{'='*5}======================================{'='*5}")
      data_akun =[]
      with open('Gudang_Akun.csv','r') as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_akun.append({'Username':row[0],'Password':row[1], 'Pekerjaan' :row[2]})
      df = pd.DataFrame(data_akun)
      print(df)
      print(f"{'='*5}======================================{'='*5}")
      Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
      Clear()
    else :
        Clear()
        break
def Akumulasi_Akun():
 while True:
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5}       Informasi Akumulasi Akun      {'='*5}")
    print(f"{'='*5}====================================={'='*5}")
    Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
    Clear()
    if Pertanyaan == "Y":
     print(f"{'='*5}====================================={'='*5}")
     print(f"{'='*5}       Informasi Akumulasi Akun      {'='*5}")
     print(f"{'='*5}====================================={'='*5}")
     print(f"Membuka Data para pekerja: ....")
     print(f"{'='*5}======================================{'='*5}")
    #  Jumlah baris Akun
     def Akun1 () :
      with open('Gudang_Akun.csv', 'r') as f:
        return len(f.readlines())
     print(f"Jumlah Akun       : {Akun1()}")
    # Jumlah baris Staf
     def Akun2() : 
        with open('Gudang_Akun.csv', 'r') as f:
         csv_reader = csv.reader(f, delimiter=',')
         count = 0
         for row in csv_reader:
            if row[2] == "Staf":
                count += 1
        return count
     print(f"Jumlah Akun Staf  : {Akun2()}")
    # Jumlah baris Admin
     def Akun3() :
        with open('Gudang_Akun.csv', 'r') as f:
         csv_reader = csv.reader(f, delimiter=',')
         count = 0
         for row in csv_reader:
            if row[2] == "Admin":
                count += 1
        return count
     print(f"Jumlah Akun Admin : {Akun3()}")
     print(f"{'='*5}======================================{'='*5}")
     Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
     Clear()
    else:
     Clear()
     break
def Data_Hadir():
 while True:
    print(f"{'='*5}====================================={'='*5}")
    print(f"{'='*5}  Informasi Kehadiran Para Pekerja   {'='*5}")
    print(f"{'='*5}====================================={'='*5}")
    Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
    Clear()
    if Pertanyaan == "Y":
     print(f"{'='*5}====================================={'='*5}")
     print(f"{'='*5}  Informasi Kehadiran Para Pekerja   {'='*5}")
     print(f"{'='*5}====================================={'='*5}")
     print(f"Membuka Kehadiran para pekerja: ....")
     print(f"{'='*5}====================================={'='*5}")
     data_hadir =[]

     with open('Riwayat_Kehadiran.csv','r') as file:
        read = csv.reader(file, delimiter=",")
        for row in read:
            data_hadir.append({'Nama_Akun':row[0],'Password':row[1], 'Pekerjaan' :row[2], 'Tanggal':row[3]})

     df = pd.DataFrame(data_hadir)
     print(df)
     print(f"{'='*5}====================================={'='*5}")
     Pertanyaan = input("Melanjutkan melihat Data[Y]/[N]:")
     Clear()
    else:
     Clear()
     break
     
# # Homepage fitur ke-5
def Info_Akun(): 
  Clear()
  while True:     
   print(f"{'='*5}==================================={'='*5}")
   print(f"{'='*5}    Menu Informasi Akun Pekerja    {'='*5}")
   print(f"{'='*5}==================================={'='*5}")
   print(f"{'='*5}       Melihat Data Pekerja    [1] {'='*5}")
   print(f"{'='*5}     Akumulasi Akun Pekerja    [2] {'='*5}")
   print(f"{'='*5}    Informasi Kehadiran Pekerja[3] {'='*5}")
   print(f"{'='*5}            Keluar   [0]           {'='*5}")
   print(f"{'='*5}==================================={'='*5}")
   Perintah=input("Perintah: ")
   if Perintah == "1":
      Clear()
      Data_Pekerja()
      Info_Akun()
      break
   elif Perintah == "2":
      Clear()
      Akumulasi_Akun()
      Info_Akun()
      break
   elif Perintah == "3":
       Clear()
       Data_Hadir()
       Info_Akun()
       break
   else:
       Clear()
       break
# # Batas-5


# # Batas penyimpanan Fungi


# # # Fungsi-fungsi pada Login dan juga Homepagesnya
def Login():
    Logo()
    print(f"{'='*7}=========================================={'='*7}")
    print(f"{'='*7} Selamat datang di Login Manajemen Gudang {'='*7}")
    print(f"{'='*7}=========================================={'='*7}")   
    Username  = input("Username Anda            : ")
    Password  = input("Masukkan Password        : ")
    N_Pekerja = input("Pekerjaan [Admin]/[Staf] : ")
    # Membaca data dari file CSV
    with open('Gudang_Akun.csv', "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        data_akun = []
        for row in csv_reader:
            data_akun.append({"Username": row[0], "Password": row[1], "Pekerjaan": row[2] })
            
    # Memeriksa apakah username dan password sudah ada
    data_login = []
    for akun in data_akun:
        if Username == akun["Username"] and Password == akun["Password"] and N_Pekerja == akun["Pekerjaan"]:
            data_login.append(akun)
            
    # Pesan Login
    if len(data_login) != 0:
      Clear()
      print("Anda berhasil login")
      
    #   Fungsi Homepage Admin
      if N_Pekerja == "Admin":
         def HomepageAdmin():
          while True :
            print(f"")
            print(f"{' '*5}        █▀▄▀█ ▄▀█ █▀▀ █░█           {' '*5}")
            print(f"{' '*5}        █░▀░█ █▀█ █▄█ █▄█           {' '*5}")
            print(f"")
            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5}    Selamat datang Dimenu Admin     {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5} Klik perintah dengan nomor berikut {'='*5}")
            print(f"{'='*5}        Informasi Pribadi    [1]    {'='*5}")
            print(f"{'='*5}      Manage Barang Gudang   [2]    {'='*5}")
            print(f"{'='*5}        Manage Pengiriman    [3]    {'='*5}")
            print(f"{'='*5}       Manage Gudang Lain    [4]    {'='*5}")
            print(f"{'='*5}    Informasi Akun Pekerja   [5]    {'='*5}")
            print(f"{'='*5}            Keluar [0]              {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
            Perintah = str(input("Perintah :"))
            if Perintah == "1":
             Clear()
             def IP():
              print(f"{'='*5}==================================={'='*5}")
              print(f"{'='*5}      Menu Informasi Pribadi       {'='*5}")
              print(f"{'='*5}==================================={'='*5}")
              print(f"{'='*5}  Lihat Bio/Informasi Pribadi[1]   {'='*5}")
              print(f"{'='*5}            Kehadiran        [2]   {'='*5}")
              print(f"{'='*5}            Keluar           [0]   {'='*5}")
              print(f"{'='*5}==================================={'='*5}")
             IP()
             Perintah = str(input("Perintah :"))
             while True:
              if Perintah == "1":
                 Clear()
                 IP()
                 print(f"Nama Anda             : {Username} ")
                 print(f"Password Terbaru Anda : {Password} ")
                 print(f"Pekerjaan Anda        : Seorang Admin Gudang")
                 print(f"Waktu login           : {waktu_login}")
                 Perintah = str(input("Perintah :"))
              elif Perintah =="2":
                  Clear()
                  IP()
                  print(f"{'='*5}==========  Catatan Kehadiran  =============={'='*5}")
                  print(f"Nama anda  {Username} dengan Password {Password} \nMelakukan kehadiran pada tanggal {tanggal_login}")
                  print(f"{'='*5}============================================={'='*5}")
                  Simpan_Data=input("Catat kehadiran [Y]/[N]: ")
                  if Simpan_Data == "Y" :
                    Work = "Admin"
                    data_hadir = {'Nama_Akun': Username, 'Password': Password, 'Pekerjaan': Work,'Tanggal' : tanggal_login}
                    with open ('Riwayat_Kehadiran.csv', 'a', newline='') as file :
                        write = csv.DictWriter(file, fieldnames=data_hadir.keys())
                        write.writerow(data_hadir)
                    print("Kehadiran Akun anda telah tercatat")
                    Perintah = str(input("Perintah :"))
                    Clear()
                    break
                  else:
                    Perintah = str(input("Perintah :"))
                    Clear()
                    break
              elif Perintah == "0":
                 Clear()
                 break    
            elif Perintah == "2": 
             Clear()  
             Manage_Barang()
             Clear()
             HomepageAdmin()
             Clear()
             break
            elif Perintah == "3":
             Clear()
             Manage_Pengiriman()
             Clear()
             HomepageAdmin()
             Clear()
             break
            elif Perintah == "4":
             Clear()
             Manage_Gudang_Lain()
             Clear()
             HomepageAdmin()
             Clear()
             break
            elif Perintah == "5":
             Clear()
             Info_Akun()
             Clear()
             HomepageAdmin()
             Clear()
             break
            elif Perintah == "0" :
             Clear()
             break
            
            else : 
             print("Mohon maaf terdapat kesalahan perintah \nMohon Isikan sesuai dengan nomor yang ada")
             Clear()
             HomepageAdmin()
             break
         HomepageAdmin()
    #  Batas Fungsi Homepage Admin
    
    #  Fungsi Homepage Staf
      elif N_Pekerja == "Staf":
        def HomepageStaf():
          while True :
            print(f"")
            print(f"{' '*5}         █▀▄▀█ ▄▀█ █▀▀ █░█          {' '*5}")
            print(f"{' '*5}         █░▀░█ █▀█ █▄█ █▄█          {' '*5}")
            print(f"")
            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5}      Selamat datang Dimenu Staf    {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
            print(f"{'='*5} Klik perintah dengan nomor berikut {'='*5}")
            print(f"{'='*5}        Informasi Pribadi     [1]   {'='*5}")
            print(f"{'='*5}      Manage Barang Gudang    [2]   {'='*5}")
            print(f"{'='*5}        Manage Pengiriman     [3]   {'='*5}")
            print(f"{'='*5}             Keluar [0]             {'='*5}")
            print(f"{'='*5}===================================={'='*5}")
            Perintah = str(input("Perintah :"))
            if Perintah == "1":
             Clear()
             print(f"{'='*5}==================================={'='*5}")
             print(f"{'='*5}       Menu Informasi Pribadi      {'='*5}")
             print(f"{'='*5}==================================={'='*5}")
             print(f"{'='*5}  Lihat Bio/Informasi Pribadi[1]   {'='*5}")
             print(f"{'='*5}            Kehadiran        [2]   {'='*5}")
             print(f"{'='*5}             Keluar          [0]   {'='*5}")
             print(f"{'='*5}==================================={'='*5}")
             Perintah = str(input("Perintah :"))
             while True:
              if Perintah == "1":
                 print(f"Nama Anda             : {Username} ")
                 print(f"Password Terbaru Anda : {Password} ")
                 print(f"Pekerjaan Anda        : Seorang Staf Gudang")
                 print(f"Waktu login           : {waktu_login}")
                 Perintah = str(input("Perintah :"))
              elif Perintah =="2": 
                  print(f"{'='*5}============ Catatan Kehadiran ==========={'='*5}")
                  print(f"Nama anda : {Username} dengan nomor Password : {Password}.\nMelakukan kehadiran pada tanggal {tanggal_login}")
                  print(f"{'='*5}=========================================={'='*5}")
                  Simpan_Data=input("Catat kehadiran [Y]/[N]: ")
                  if Simpan_Data == "Y" :
                    Work = "Staf"
                    data_hadir = {'Nama_Akun': Username, 'Password': Password, 'Pekerjaan': Work,'Tanggal' : tanggal_login}
                    with open ('Riwayat_Kehadiran.csv', 'a', newline='') as file :
                        write = csv.DictWriter(file, fieldnames=data_hadir.keys())
                        write.writerow(data_hadir)
                    print("Kehadiran Akun anda telah tercatat")
                    Perintah = str(input("Perintah :"))
                    Clear()
                    break
                  else:
                    Perintah = str(input("Perintah :"))
                    Clear()
                    break
              elif Perintah == "0":
                 Clear()
                 break
            elif Perintah == "2":
             Clear()
             Manage_Barang()
             Clear()
             HomepageStaf()
             Clear()
             break
            elif Perintah == "3":
             Clear()
             Manage_Pengiriman()
             Clear()
             HomepageStaf()
             Clear()
             break
            elif Perintah == "0" :
             Clear()
             break
            else : 
             Clear()
             print("Mohon maaf terdapat kesalahan perintah \nMohon Isikan sesuai dengan nomor yang ada")
             HomepageStaf()
             break
        HomepageStaf()
    else:
        Clear()
        print("Mohon maaf akun tidak dapat ditemukan,\nMohon masukkan Data kembali !!!")
    
# # # Batas fungsi login   
        
# # Perintah-perintah awalan untuk Login atau Register
PilihanAwal = input("Login atau Register [L/R]: ")
# Melakukan Validasi Informasi
while PilihanAwal != "L" and PilihanAwal != "R":
    Clear()
    print(f"{'='*7}========================================{'='*7}")
    print(f"{'='*7} Selamat datang di App Manajemen Gudang {'='*7}")
    print(f"{'='*7}========================================{'='*7}")
    print("Pilihan anda salah, harap isikan sesuai perintah")
    PilihanAwal = input("Login atau Register [L/R]: ")
# Menjalankan fungsi berdasarkan Pilihan
while True:
 if PilihanAwal == "L":
      Clear()
      Login()
      Logo()
      print(f"{'='*7}========================================{'='*7}")
      print(f"{'='*7} Selamat datang di App Manajemen Gudang {'='*7}")
      print(f"{'='*7}========================================{'='*7}")
      PilihanAwal = input("Login atau Register [L/R]: ")
 elif PilihanAwal == "R":
      Clear()
      Register()
      PilihanAwal = input("Login atau Register [L/R]: ")
    

# Membuat fungsi Homepage agar berjalan sesuai untuk Admin atau Staff
