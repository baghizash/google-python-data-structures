# Struktur Data Python untuk Analisis

Project ini merangkum bagian struktur data dari Module 4 course Introduction to Data Analysis Using Python (Google Data Analytics Professional Certificate). Latihan dijalankan ulang dari awal sampai akhir lewat satu script: `analyze_structures.py`.

## Materi yang dipelajari

1. Lists dan tuples: membuat list, list comprehension jadi list of lists, dan unpacking
2. Dictionaries: menyimpan dan mengambil informasi, menghitung dengan fungsi `county_counter`
3. Sets: mencari county yang namanya dipakai di lebih dari satu state

## Dataset

* `train.csv`: 891 penumpang Titanic (nama, umur, kelas, status selamat)
* `c2_epa_air_quality.csv`: 1725 pembacaan indeks kualitas udara EPA dari berbagai state

## Cara menjalankan

```bash
python analyze_structures.py
```

Script akan mencetak semua hasil latihan, menyimpan 4 chart di folder `charts/`, dan menulis ringkasan angka di `findings.json`.

## Hasil utama

* Rata rata selamat Titanic: kelas 1 sebesar 0.630, kelas 2 sebesar 0.473, kelas 3 sebesar 0.242
* 72 pembacaan tercatat di Arizona; rata rata AQI California 9.41
* Washington County di Pennsylvania tercatat 7 kali; county tersibuk di Indiana adalah Marion dengan 8 pembacaan
* Dari 254 nama county yang unik, 18 nama dipakai di lebih dari satu state

## Struktur folder

* `analyze_structures.py`: script utama berisi semua latihan
* `charts/`: 4 visualisasi hasil latihan
* `data/`: kedua dataset asli dari course
* `findings.json`: ringkasan angka hasil eksekusi
