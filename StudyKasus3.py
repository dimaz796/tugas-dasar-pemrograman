# Nama : Dimas Aditya Herlambang
# NIM : 2604920
# Materi : Perulanagan
# Soal Study Kasus

jumlah = int(input("Masukan Jumlah Bilangan Yang Akan Dibuah : "))
bilangan =[]
i = 0
p = 0

for i in range(jumlah) :
    i += 1
    angka = int(input(f"Masukan Bilangan Ke-{i} : "))
    bilangan.append(angka)


for angka in bilangan:
    p += 1

    if angka % 2 == 0:
        print(f"Bilangan Ke-{p} Nilainya {angka} Adalah Genap")
    else:
        print(f"Bilangan Ke-{p} Nilainya {angka} Adalah Ganjil")