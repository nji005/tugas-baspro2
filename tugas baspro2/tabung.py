import math

def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

# Meminta input dari pengguna
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))
volume = hitung_volume_tabung(jari_jari, tinggi)

print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume:.2f}")