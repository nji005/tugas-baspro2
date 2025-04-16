

def buat_matriks_5x5(nilai_awal):
    """Membuat matriks 5x5 dengan angka berurutan mulai dari nilai_awal"""
    matriks = []
    angka = nilai_awal
    for i in range(5):
        baris = []
        for j in range(5):
            baris.append(angka)
            angka += 1
        matriks.append(baris)
    return matriks

def cetak_matriks(matriks, nama="Matriks"):
    print(f"{nama}:")
    for baris in matriks:
        print(baris)
    print()

def perkalian_matriks_5x5(A, B):
    """Mengalikan dua matriks 5x5 tanpa menggunakan numpy"""
    hasil = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

if __name__ == "__main__":
    
    matriks_A = buat_matriks_5x5(1)

    
    matriks_B = buat_matriks_5x5(26)

    
    cetak_matriks(matriks_A, "Matriks A")
    cetak_matriks(matriks_B, "Matriks B")

    
    hasil = perkalian_matriks_5x5(matriks_A, matriks_B)

    
    cetak_matriks(hasil, "Hasil A x B")