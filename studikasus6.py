import json

path = r"D:\Fahry\code\python-handtrack\fahry\studi_kasus_6.py\data_barang.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def tampilkan_data():
    print("\n===== DATA INVENTARIS BARANG =====")

    for barang in data:
        print(barang)


def tambah_data(nama, stok, harga):
    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga
    })

    return "Data berhasil ditambahkan!"


def simpan_data():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Data berhasil disimpan ke data_barang.json"


while True:
    print("\n================================")
    print(" SISTEM MANAJEMEN INVENTARIS")
    print("================================")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        tampilkan_data()

    elif pilihan == "2":

        nama = input("Masukkan nama barang : ")
        stok = int(input("Masukkan stok barang : "))
        harga = int(input("Masukkan harga barang : "))

        print("\n", tambah_data(nama, stok, harga))
        print(simpan_data())

    elif pilihan == "3":

        print("\nTerima kasih telah menggunakan program.")
        break

    else:

        print("\nPilihan tidak valid!")