def MethodGarisLurus():
    print ("-_-_-_-Metode Garis Lurus-_-_-_-")
    Harga = int(input("Masukan Harga Perolehan: Rp "))
    NilaiResidu = int(input("Masukan Nilai Residu: Rp "))
    UmurEkom = int(input("Masukan Umur Ekonomis: "))
    print("Depresiasi = " + str((Harga - NilaiResidu)/ UmurEkom))


def MethodJamJasa():
    print ("-_-_-_-Metode Jam jasa-_-_-_-")
    HargaJJ = int(input("Masukan Harga Perolehan Jam : Rp "))
    NilaiResiduJJ = int(input("Masukan Nilai Residu: Rp "))
    TaksiranHasil = int(input("Taksiran Hasil Produksi (unit):"))
    print("Depresiasi = " + str((HargaJJ - NilaiResiduJJ)/ TaksiranHasil)
    )

print("-_-_-_-Menu Metode Menghitung Depresiasi-_-_-_-")
print("1. Metode Garis Lurus")
print("2. Metode Jam Jasa")

menu = int(input("Masukan Metode Yang Dipilih: "))
if menu == 1:
    MethodGarisLurus()
elif menu == 2:
    MethodJamJasa()