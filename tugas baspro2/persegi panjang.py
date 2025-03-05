def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Meminta input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
luas = hitung_luas_persegi_panjang(panjang, lebar)

print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas:.2f}")
