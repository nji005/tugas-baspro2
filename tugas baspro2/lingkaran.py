import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = hitung_luas_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
