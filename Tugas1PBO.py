import psycopg2
#koneksiect Database
koneksi = psycopg2.connect(
         host="localhost",
         database="kampus",
         user="namauser",
         password="123")

#Menyimpan Data Baru
def insert_data(koneksi):
   idmhs = int(input("Masukan ID Mahasiswa: "))
   nim = input("Masukan NIM Mahasiswa: ")
   nama = input("Masukan Nama Mahasiswa: ")
   idfakultas = int(input("Masukan ID Fakultas Mahasiswa: "))
   idprodi = int(input("Masukan ID Prodi: "))
   validasi = (idmhs,nim,nama,idfakultas,idprodi)
   sql = "INSERT INTO mahasiswa (idmhs, nim, nama, idfakultas, idprodi) VALUES (%s, %s, %s, %s, %s)"
   kursor = koneksi.cursor()
   kursor.execute(sql, validasi)
   koneksi.commit()
   print("==================================")
   print("{} Data Berhasil Disimpan".format(kursor.rowcount))

#Menampilkan Data
def show_data(koneksi):
   kursor = koneksi.cursor()
   sql = "SELECT * FROM mahasiswa"
   kursor.execute(sql)
   result = kursor.fetchall()

   if kursor.rowcount < 0:
      print("==================================")
      print("DATA TIDAK ADA ATAU BELUM TERISI")
   else:
      print("==================================")
      print("-{} DATA BERHASIL DITEMUKAN".format(kursor.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(koneksi):
   kursor = koneksi.cursor()
   show_data(koneksi)
   idmhs = input("Pilih ID Mahasiswa: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   nama = input("Masukan Nama Mahasiswa Yang Baru: ")
   idfakultas = int(input("Masukan Id Fakultas yang Baru: "))
   idprodi = int(input("Masukan Id Prodi Yang Baru: "))
   sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE idmhs=%s"
   validasi = (nim, nama, idfakultas, idprodi, idmhs)
   kursor.execute(sql, validasi)
   koneksi.commit()
   print("==================================")
   print("{} Data Berhasil Diupdate".format(kursor.rowcount))

#Menghapus Data
def delete_data(koneksi):
   kursor = koneksi.cursor()
   show_data(koneksi)
   idmhs = str(input("Pilih ID Mahasiswa Yang Akan Dihapus: "))
   slc = "SELECT * FROM mahasiswa WHERE idmhs= %s"
   validasi = (idmhs)
   kursor.execute(slc, validasi)
   con = kursor.rowcount
   if (con == 1):
      inp = input("Apakah Anda Yakin Ingin Menghapus Data Tersebut? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
         validasi = (idmhs)
         kursor.execute(sql, validasi)
         koneksi.commit()
         print("==================================")
         print("\b{} DATA BERHASIL DIHAPUS".format(kursor.rowcount))
      else:
         print("data batal dihapus")
   else:
      print("TIDAK ADA ID YANG DIMAKSUD")
   """sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
   validasi = (idmhs)
   kursor.execute(sql, validasi)
   koneksi.commit()
   print("{} Data Berhasil Dihapus".format(kursor.rowcount))"""

#Mencari Data
def search_data(koneksi):
   kursor = koneksi.cursor()
   keyword = input("MASUKAN NIM ATAU NAMA DATA YANG DICARI: ")
   sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   validasi = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   kursor.execute(sql, validasi)
   result = kursor.fetchall()

   if kursor.rowcount <= 0:
      print("==================================")
      print("TIDAK ADA DATA YANG DIMAKSUD")
   else:
      print("==================================")
      print("{} DATA YANG DIMAKSUD BERHASIL DITEMUKAN".format(kursor.rowcount))
      for data in result:
         print(data)
#FAQIHUDDIN SHOLEH_200511050_R2
#Menampilkan Menu
def show_menu(koneksi):
   print("============================================")
   print("==== TUGAS 1 PEMBUATAN CRUD MELALUI CLI ====")
   print("== DIBUAT OLEH FAQIHUDDIN SHOLEH ==")
   print("1. Insert Data")
   print("2. Show Data")
   print("3. Update Data")  
   print("4. Delete Data")
   print("5. Search Data")
   print("0. Keluar")
   print("------------------")
   menu = input("Pilih Menu: ")

   if menu == "1":
      insert_data(koneksi)
   elif menu == "2":
      show_data(koneksi)
   elif menu == "3":
      update_data(koneksi)
   elif menu == "4":
      delete_data(koneksi)
   elif menu == "5":
      search_data(koneksi)
   elif menu == "0":
      exit()
   else:
      print("Menu salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(koneksi)
