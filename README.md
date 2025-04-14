# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

> Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Tingginya tingkat pengunduran diri (attrition) menyebabkan gangguan operasional dan biaya perekrutan ulang yang tinggi. Untuk itu, dibutuhkan pendekatan prediktif berbasis data untuk mengidentifikasi karyawan yang berpotensi resign, sehingga HRD dapat mengambil tindakan preventif.

### Permasalahan Bisnis

Permasalahan yang ingin diselesaikan antara lain:
- Mendeteksi secara dini karyawan yang berisiko tinggi untuk resign.
- Mengidentifikasi faktor-faktor utama penyebab pengunduran diri.
- Menyusun strategi retensi berdasarkan data.

### Cakupan Proyek

- Memprediksi kemungkinan karyawan akan resign atau tidak.
- Menggunakan model XGBoost serta teknik SMOTE untuk mengatasi data imbalance.
- Menyajikan visualisasi data melalui Metabase Dashboard.
- Memberikan insight dan rekomendasi kepada perusahaan berdasarkan fitur penting yang memengaruhi attrition.

### Persiapan

Sumber data: Dataset karyawan berisi informasi demografis, pekerjaan, status attrition, dll. yang tersimpan dalam file ![**employee_data.csv**](Dataset/employee_data.csv) atau unduh langsung dari [dicoding_dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv).

Setup environment:

## ⚙️Instalasi
Pastikan Anda telah menginstal semua dependensi yang dibutuhkan:
```
pip install -r requirements.txt
```
---
## 🎞️Menjalankan Proyek
1️⃣ Jalankan notebook Jupyter atau Google Colab:
   ```
   jupyter notebook Proyek_System_Recommendation_Tsamarah_Muthi'ah_A.ipynb
   ```
2️⃣ Ikuti langkah-langkah di dalam notebook untuk melakukan pelatihan dan evaluasi model XGBoost.
3️⃣ Simpan model XGBoost yang telah dilatih, atau jika ingin melewati proses pelatihan model pada tahap no.2, Anda dapat langsung mengunduh file-file berikut: [xgboost_model.pkl](model/xgboost_model.pkl), [pipeline.pkl](others/pipeline.pkl), [optimal_threshold.json](others/optimal_threshold.json), dan [top_10_feature_importance.csv](others/top_10_feature_importance.csv).

- ```xgboost_model.pkl:``` berisi model XGBoost yang telah dilatih untuk memprediksi karyawan yang berpotensi resign.
- ```pipeline.pkl:``` berisi preprocessing pipeline (seperti encoding dan scaling) yang diperlukan sebelum model melakukan prediksi.
- ```optimal_threshold.json:``` menyimpan nilai threshold optimal (yaitu **0.28**) yang digunakan untuk mengubah probabilitas prediksi menjadi kelas akhir (resign(1) atau tidak/bertahan(0).
- ```top_10_feature_importance.csv:``` berisi daftar 10 fitur paling berpengaruh terhadap prediksi resign, yang berguna untuk memahami faktor-faktor utama yang mempengaruhi attrition.

File-file ini diperlukan untuk menjalankan [prediction.py](Predict/predict.py) tanpa perlu melatih ulang model.

4️⃣ Selanjutnya jalankan file [prediction.py](Predict/predict.py) Berikut penjelasan mengenai tahapan dalam file tersebut:

### **📄 Penjelasan Proses dalam prediction.py:**
```
1. Import Library
- Mengimpor library yang diperlukan untuk pemrosesan data, pemuatan model, dan prediksi.

2. Load Model dan File Terkait
- pipeline.pkl: untuk preprocessing data (seperti encoding dan scaling).
- xgboost_model.pkl: model XGBoost yang sudah dilatih untuk memprediksi apakah karyawan akan resign.
- optimal_threshold.json: nilai threshold optimal (0.28) untuk mengubah probabilitas menjadi label prediksi (0 = bertahan, 1 = resign).

3. Load Data Karyawan

Membaca file employee_data.csv yang berisi data karyawan yang ingin diprediksi. Jika kolom Attrition ada, akan dihapus agar tidak mengganggu proses prediksi.

4. Preprocessing Data

Data karyawan diproses menggunakan pipeline yang sama dengan saat pelatihan model.

5. Prediksi
- Model menghasilkan probabilitas kemungkinan karyawan resign.
- Probabilitas tersebut dikonversi menjadi label biner berdasarkan threshold (0.28).

6. Hasil Prediksi
- Kolom baru ditambahkan ke DataFrame:
- Attrition_Predicted: hasil prediksi apakah karyawan akan resign.
- Probability: probabilitas prediksi dari model.

7. Simpan Hasil

Hasil akhir disimpan ke file predictions.csv.
```

## Business Dashboard

**Dashboard disusun secara berurutan untuk memberikan narasi yang jelas:**

1. Jumlah Total Karyawan: Menunjukkan total data sebanyak 1.470 karyawan.
2. Prediksi Resign: Menampilkan jumlah karyawan yang diprediksi resign (236 atau ~16%).
3. Distribusi Resign per Departemen: R&D memiliki jumlah potensi resign terbanyak, diikuti oleh Sales dan Human Resources.
4. Top 10 Faktor Penyebab: Fitur paling berpengaruh adalah status lembur (OverTime), jabatan, keterlibatan kerja, dan kepemilikan saham.
5. Pengaruh Lembur: 58.1% karyawan yang resign merupakan mereka yang melakukan lembur.
6. Strategi Retensi: Disusun berdasarkan insight yang ditemukan dari fitur-fitur penting.

_Dashboard dapat diakses melalui Metabase lokal: predicted_resign.db (Username : Tsamarah Abdullah, Pass : Tsamarah192) atau melihat dalam bentuk image_.

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
