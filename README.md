# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

> Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Tingginya tingkat pengunduran diri (attrition) menyebabkan gangguan operasional dan biaya perekrutan ulang yang tinggi. Untuk itu, dibutuhkan pendekatan prediktif berbasis data untuk mengidentifikasi karyawan yang berpotensi resign, sehingga HRD dapat mengambil tindakan preventif.

### Permasalahan Bisnis

Permasalahan yang ingin diselesaikan antara lain:
- Mendeteksi secara dini karyawan yang berisiko tinggi untuk resign.
- Mengidentifikasi faktor-faktor utama penyebab pengunduran diri.
- Menyusun strategi retensi berdasarkan data.
- Mengurangi beban HR dalam merekrut dan melatih kembali karyawan.

### Cakupan Proyek

- Memprediksi kemungkinan karyawan akan resign atau tidak.
- Menggunakan model XGBoost serta teknik SMOTE untuk mengatasi data imbalance.
- Menyajikan visualisasi data melalui Metabase Dashboard.
- Memberikan insight dan rekomendasi kepada perusahaan berdasarkan fitur penting yang memengaruhi attrition.

### Persiapan

Sumber data: Dataset karyawan berisi informasi demografis, pekerjaan, status attrition, dll. yang tersimpan dalam file **employee_data.csv**.

Setup environment:

```
pip install -r requirements.txt
```

## Business Dashboard

**Dashboard disusun secara berurutan untuk memberikan narasi yang jelas:**

1. Jumlah Total Karyawan: Menunjukkan total data sebanyak 1.470 karyawan.
2. Prediksi Resign: Menampilkan jumlah karyawan yang diprediksi resign (236 atau ~16%).
3. Distribusi Resign per Departemen: R&D memiliki jumlah potensi resign terbanyak, diikuti oleh Sales dan Human Resources.
4. Top 10 Faktor Penyebab: Fitur paling berpengaruh adalah status lembur (OverTime), jabatan, keterlibatan kerja, dan kepemilikan saham.
5. Pengaruh Lembur: 58.1% karyawan yang resign merupakan mereka yang melakukan lembur.
6. Strategi Retensi: Disusun berdasarkan insight yang ditemukan dari fitur-fitur penting.

(Dashboard dapat diakses melalui Metabase lokal: predicted_resign.db (Username : Tsamarah Abdullah, Pass : Tsamarah192) atau melihat dalam bentuk image).

## Conclusion

Proyek ini berhasil mengidentifikasi potensi attrition dengan pendekatan machine learning, khususnya XGBoost dan SMOTE dengan akurasi mencapai 92% serta melakukan threshold untuk meningkatkan akurasi prediksi. Ditemukan bahwa faktor lembur, jabatan, keterlibatan kerja, dan insentif memiliki peran penting dalam prediksi karyawan resign. Visualisasi dan dashboard yang dibangun dapat membantu manajemen dalam pengambilan keputusan berbasis data.

### Rekomendasi Action Items (Optional)

**Berikut beberapa langkah strategis yang dapat dilakukan HR:**

1. Evaluasi Kebijakan Lembur

Kurangi lembur berlebihan dan atur keseimbangan kerja-hidup yang sehat.

2. Tinjau Sistem Insentif

Optimalkan stock option dan jenjang karier agar karyawan lebih termotivasi.

3. Tingkatkan Keterlibatan Karyawan

Lakukan survei rutin dan kegiatan peningkatan engagement.

4. Perhatikan Departemen Rawan Resign

Fokus pada R&D, Sales, dan HR untuk program retensi karyawan.

5. Terapkan Sistem Peringatan Dini

Gunakan dashboard sebagai alat pemantauan rutin untuk mendeteksi risiko resign.
