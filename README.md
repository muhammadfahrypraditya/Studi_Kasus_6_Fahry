<h1 align="center">STUDI KASUS 6</h1>

<h2 align="center">SISTEM MANAJEMEN INVENTARIS BARANG</h2>

<p align="center">
  <b>Nama:</b> Muhammad Fahry Praditya<br>
  <b>NIM:</b> 2609116104<br>
  <b>Kelas:</b> C
</p>

---



# CODINGAN

```python
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
```

---

# 📝 PENJELASAN KODE

<table>
<tr>
<th width="50%">Kode</th>
<th width="50%">Penjelasan</th>
</tr>

<tr>
<td>

```python
import json

path = r"D:\Fahry\code\python-handtrack\fahry\studi_kasus_6.py\data_barang.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)
```

</td>
<td>

`import json` digunakan untuk menggunakan fitur JSON pada Python.

Variabel `path` digunakan untuk menentukan lokasi file `data_barang.json`.

`open()` digunakan untuk membuka file JSON.

`json.load(f)` digunakan untuk membaca data yang terdapat di dalam file JSON dan memasukkannya ke dalam variabel `data`.

</td>
</tr>

<tr>
<td>

```python
def tampilkan_data():

    print("\n===== DATA INVENTARIS BARANG =====")

    for barang in data:
        print(barang)
```

</td>
<td>

Fungsi `tampilkan_data()` digunakan untuk menampilkan data barang.

`for barang in data` digunakan untuk melakukan perulangan pada data yang terdapat dalam variabel `data`.

Kemudian `print(barang)` digunakan untuk menampilkan setiap data barang.

</td>
</tr>

<tr>
<td>

```python
def tambah_data(nama, stok, harga):

    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga
    })

    return "Data berhasil ditambahkan!"
```

</td>
<td>

Fungsi `tambah_data()` digunakan untuk menambahkan barang baru.

Fungsi menerima tiga data yaitu `nama`, `stok`, dan `harga`.

`data.append()` digunakan untuk menambahkan data baru ke dalam list `data`.

Data barang disimpan dalam bentuk dictionary.

</td>
</tr>

<tr>
<td>

```python
def simpan_data():

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Data berhasil disimpan ke data_barang.json"
```

</td>
<td>

Fungsi `simpan_data()` digunakan untuk menyimpan data ke dalam file JSON.

`json.dump()` digunakan untuk memasukkan data dari Python ke dalam file JSON.

`indent=4` digunakan agar isi file JSON terlihat lebih rapi.

</td>
</tr>

<tr>
<td>

```python
while True:

    print("\n================================")
    print(" SISTEM MANAJEMEN INVENTARIS")
    print("================================")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu : ")
```

</td>
<td>

`while True` digunakan agar program dapat berjalan terus menerus.

Program menampilkan tiga pilihan menu.

`input()` digunakan untuk menerima pilihan dari pengguna dan menyimpannya ke dalam variabel `pilihan`.

</td>
</tr>

<tr>
<td>

```python
if pilihan == "1":

    tampilkan_data()
```

</td>
<td>

Jika pengguna memilih menu `1`, maka fungsi `tampilkan_data()` akan dijalankan untuk menampilkan seluruh data barang.

</td>
</tr>

<tr>
<td>

```python
elif pilihan == "2":

    nama = input("Masukkan nama barang : ")
    stok = int(input("Masukkan stok barang : "))
    harga = int(input("Masukkan harga barang : "))

    print("\n", tambah_data(nama, stok, harga))
    print(simpan_data())
```

</td>
<td>

Jika pengguna memilih menu `2`, program meminta nama, stok, dan harga barang.

`input()` digunakan untuk menerima data.

`int()` digunakan untuk mengubah stok dan harga menjadi angka.

Setelah itu `tambah_data()` digunakan untuk menambahkan barang dan `simpan_data()` digunakan untuk menyimpan data ke file JSON.

</td>
</tr>

<tr>
<td>

```python
elif pilihan == "3":

    print("\nTerima kasih telah menggunakan program.")
    break
```

</td>
<td>

Jika pengguna memilih menu `3`, program akan menampilkan pesan terima kasih.

`break` digunakan untuk menghentikan perulangan `while` sehingga program selesai.

</td>
</tr>

<tr>
<td>

```python
else:

    print("\nPilihan tidak valid!")
```

</td>
<td>

Bagian `else` digunakan jika pengguna memasukkan pilihan selain `1`, `2`, atau `3`.

Program akan menampilkan pesan bahwa pilihan tidak valid dan kembali ke menu.

</td>
</tr>

</table>

---

# 📄 DATA BARANG

File yang digunakan dalam program adalah `data_barang.json`.

Contoh isi file:

```json
[
    {
        "nama": "Beras",
        "stok": 20,
        "harga": 15000
    },
    {
        "nama": "Minyak Goreng",
        "stok": 15,
        "harga": 18000
    },
    {
        "nama": "Gula",
        "stok": 25,
        "harga": 17000
    }
]
```

---

# 🖥️ HASIL OUTPUT PROGRAM

## 1. Menampilkan Data Barang

Masukkan screenshot hasil ketika memilih menu **1** di bawah ini.

Contoh:

```text
================================
 SISTEM MANAJEMEN INVENTARIS
================================
1. Tampilkan Data Barang
2. Tambah Data Barang
3. Keluar
Pilih menu : 1

===== DATA INVENTARIS BARANG =====
{'nama': 'Beras', 'stok': 20, 'harga': 15000}
{'nama': 'Minyak Goreng', 'stok': 15, 'harga': 18000}
{'nama': 'Gula', 'stok': 25, 'harga': 17000}
```

---

## 2. Menambahkan Data Barang

Masukkan screenshot ketika menambahkan data barang di bawah ini.

Contoh:

```text
Pilih menu : 2

Masukkan nama barang : Indomie
Masukkan stok barang : 30
Masukkan harga barang : 3500

Data berhasil ditambahkan!
Data berhasil disimpan ke data_barang.json
```

---

## 3. Data Tetap Tersimpan

Setelah menambahkan barang, program ditutup dan dijalankan kembali.

Kemudian pilih menu **1**.

Masukkan screenshot yang menunjukkan bahwa barang yang baru ditambahkan masih muncul.

Hal tersebut membuktikan bahwa data barang telah berhasil disimpan secara permanen ke dalam file `data_barang.json`.

---

# 📌 KESIMPULAN

Program Sistem Manajemen Inventaris Barang dibuat untuk membaca, menampilkan, dan menambahkan data barang menggunakan file JSON.

Program menggunakan beberapa konsep dasar Python seperti `function`, `list`, `dictionary`, `for`, `while`, `if`, `input()`, `json.load()`, dan `json.dump()`.

Data barang yang ditambahkan akan disimpan kembali ke dalam file JSON sehingga data tidak hilang ketika program dijalankan kembali.
