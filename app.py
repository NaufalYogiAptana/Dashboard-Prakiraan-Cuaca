import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Fungsi untuk mengambil data dari API BMKG
def get_weather_data(kode_wilayah):
    url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={kode_wilayah}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Gagal mengambil data dari API BMKG.")
        return None

# Fungsi untuk mengolah data JSON menjadi DataFrame
def parse_weather_data(data):
    records = []
    desa_info = data['lokasi']
    desa = desa_info['desa']
    kecamatan = desa_info['kecamatan']
    kota = desa_info['kotkab']
    provinsi = desa_info['provinsi']
    
    cuaca_data = data['data'][0]['cuaca']  # Ambil hanya indeks pertama jika hanya ingin hari pertama
    for hari in cuaca_data:
        for jam_data in hari:
            records.append({
                'Waktu Lokal': datetime.fromisoformat(jam_data['local_datetime']),
                'Suhu (°C)': jam_data['t'],
                'Kelembapan (%)': jam_data['hu'],
                'Cuaca': jam_data['weather_desc']
            })

    df = pd.DataFrame(records)
    lokasi = f"{desa}, {kecamatan}, {kota}, {provinsi}"
    return df, lokasi

# Streamlit UI
# Konfigurasi halaman
st.set_page_config(page_title="Prakiraan Cuaca BMKG", layout="wide")

# Referensi & Sumber Data
st.markdown("**Sumber Data:** [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://www.bmkg.go.id/)")
st.markdown("**Referensi Kode Wilayah:** [https://kodewilayah.id](https://kodewilayah.id)")
st.markdown("---")

# Judul Aplikasi
st.title("📡 Dashboard Prakiraan Cuaca 3 Harian - BMKG")

kode_wilayah = st.text_input("Masukkan Kode Wilayah (adm4):", "")

if kode_wilayah:
    data = get_weather_data(kode_wilayah)
    if data:
        df, lokasi = parse_weather_data(data)
        st.subheader(f"Lokasi: {lokasi}")
        st.dataframe(df, use_container_width=True)
        st.line_chart(df.set_index('Waktu Lokal')[['Suhu (°C)', 'Kelembapan (%)']])