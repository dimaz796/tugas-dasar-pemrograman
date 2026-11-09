# Nama : Dimas Aditya Herlambang
# NIM : 2604920
# Materi : Perulanagan
# Soal Study Kasus

jumlah = int(input("Masukan Jumlah Hewan Yang Akan Diinput : "))
namaHewan =[]
i = 0
p = 0

for i in range(jumlah) :
    i += 1
    nama = input(f"Masukan Nama Hewan Ke-{i} : ")
    namaHewan.append(nama)


for nama in namaHewan:
    p += 1
    print(f"Nama Hewan Ke-{p} : {nama}")