print("Selamat Datang Di Dafun")
nama = input("Masukan Nama :")
umur = int(input("Masukan Umur :"))
print("Haloo" , nama , "Selamat Menikmati Wahana Di Dafun")

print("Daftar Wahana")
wahana = ["Biang Lala RP. 13.0000" , "Istana Boneka RP. 10.000 " , "Rumah Kaca RP. 15.000" , "Roller Coaster RP. 20.000" ]

angka = 1
total_pembelian = 0
for daftar in wahana :
    print(str(angka) , "." ,  daftar)
    angka = int(angka) + 1
nomer_wahana = int(input("Pilih Nomer Wahana :"))

if (nomer_wahana == 1) :
    print("pilihan wahana nomer 1")
    total_pembelian += 13000
elif (nomer_wahana == 2) :
    print("pilhan wahana nomer 2")
    total_pembelian += 10000
elif (nomer_wahana == 3) :
    print("pilihan nomer 3")
    total_pembelian += 15000
elif (nomer_wahana == 4) :
    print("pilihan wahana 4")
    total_pembelian += 20000
      if(int(umur) > 18) :
   print("umur anda belum mencukupi")
else :
    print("pilihan anda tidak ada di list")

total_pembelian += 2000
print(" + pajak 2000")
print( total_pembelian)