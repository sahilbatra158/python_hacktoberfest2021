# Mantapkan kode dengan adanya input nomor !
n = int(input("Masukkan Angka : "))
for i in range(n):
    for j in range(i):
        print(j+1, end="")
    print()
