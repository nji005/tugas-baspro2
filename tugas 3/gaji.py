def input_karyawan():
    jumlah_karyawan = int(input("Input jumlah karyawan: "))
    daftar_karyawan = []

    for i in range(jumlah_karyawan):
        print(f"\nNama karyawan ke-{i+1}:")
        nama = input("Nama: ")
        id_karyawan = input("ID: ")
        status = input("Status (Tetap/Honor): ").strip().capitalize()
        golongan = input("Golongan (A/B/C): ").strip().upper()

    
        if status not in ["Tetap", "Honor"] or golongan not in ["A", "B", "C"]:
            print("Data yang diinputkan tidak valid")
            return None

        daftar_karyawan.append({
            "nama": nama,
            "id": id_karyawan,
            "status": status,
            "golongan": golongan
        })

    return daftar_karyawan

def hitung_gaji(karyawan):
    if karyawan["status"] == "Tetap":
        gaji_pokok = 1000000
        if karyawan["golongan"] == "A":
            gaji_pokok += 200000
        elif karyawan["golongan"] == "B":
            gaji_pokok += 400000
        elif karyawan["golongan"] == "C":
            gaji_pokok += 550000
    elif karyawan["status"] == "Honor":
        gaji_pokok = 750000
        if karyawan["golongan"] == "A":
            gaji_pokok += 150000
        elif karyawan["golongan"] == "B":
            gaji_pokok += 275000
        elif karyawan["golongan"] == "C":
            gaji_pokok += 480000
    else:
        return "Data yang diinputkan tidak valid"

    return gaji_pokok

def output_gaji(daftar_karyawan):
    if daftar_karyawan is None:
        return

    for karyawan in daftar_karyawan:
        gaji = hitung_gaji(karyawan)
        print(f"\nNama: {karyawan['nama']}")
        print(f"ID: {karyawan['id']}")
        print(f"Status: {karyawan['status']}")
        print(f"Golongan: {karyawan['golongan']}")
        print(f"Gaji: Rp {gaji:,}")


daftar_karyawan = input_karyawan()
output_gaji(daftar_karyawan)