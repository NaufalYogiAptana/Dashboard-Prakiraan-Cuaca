# 🌦️ Dashboard Prakiraan Cuaca 3 Harian - BMKG

Aplikasi ini adalah dashboard interaktif berbasis **Streamlit** yang menampilkan prakiraan cuaca 3 harian berdasarkan data dari API **BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)**. Anda cukup memasukkan *kode wilayah* (`adm4`) untuk melihat informasi cuaca seperti suhu, kelembapan, dan deskripsi cuaca dari wilayah yang dipilih.

---

## 🚀 Fitur Utama

- 📍 Menampilkan informasi lokasi lengkap (desa, kecamatan, kota, provinsi)
- 🌡️ Prakiraan suhu dan kelembapan tiap jam selama 3 hari
- 📊 Visualisasi tren cuaca dengan grafik
- 🔗 Menggunakan API publik resmi dari BMKG

---

## 🛠️ Teknologi yang Digunakan

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)
- API Publik [BMKG](https://www.bmkg.go.id/)

---

## 📦 Instalasi & Menjalankan Aplikasi

1. **Clone repositori ini**
    ```bash
    git clone https://github.com/NaufalYogiAptana/nama-repo.git
    cd nama-repo
    ```

2. **Install dependensi**
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi Streamlit**
    ```bash
    streamlit run app.py
    ```

---

## 🔑 Kode Wilayah (adm4)

Anda memerlukan *kode wilayah* `adm4` untuk menampilkan data. Kode dapat ditemukan di situs:
👉 [https://kodewilayah.id](https://kodewilayah.id)

Contoh kode wilayah:
- Jakarta Pusat: `3171`
- Surabaya: `3578`

---

## 📄 Contoh Output

- Tabel prakiraan cuaca (tiap jam selama 3 hari)
- Grafik suhu & kelembapan secara interaktif
- Informasi lokasi berdasarkan input kode wilayah

---

## ⚠️ Perhatian!

**Wajib untuk mencantumkan BMKG (Badan Meteorologi, Klimatologi, dan Geofisika) sebagai sumber data dan menampilkannya pada aplikasi/sistem Anda.**  
Aplikasi ini menggunakan data resmi dari BMKG, dan penyebarannya tetap tunduk pada ketentuan yang berlaku dari lembaga tersebut.

---

## 🙌 Kontribusi

Pull request sangat diterima! Untuk perubahan besar, silakan buka *issue* terlebih dahulu.

---

## 📬 Kontak

Dibuat oleh **Naufal Yogi Aptana**  
🔗 [LinkedIn](https://www.linkedin.com/in/naufalyogiaptana)  
💻 [GitHub](https://github.com/NaufalYogiAptana)
