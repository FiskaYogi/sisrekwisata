import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Sistem Rekomendasi Wisata di Pasuruan Jawa Timur")
st.write("Cari rekomendasi Wisata berdasarkan kriteria yang Anda pilih.")

# Membaca dataset langsung dari file lokal
try:
    dataset_path = "data_wisata.csv"  # Pastikan file ini berada di folder yang sama dengan script
    data = pd.read_csv(dataset_path)
    # Input form pencarian
    namawisata = st.text_input("Nama Wisata", placeholder="Masukkan Nama Wisata")
    jeniswisata = st.text_input("Jenis Wisata", placeholder="Masukkan Jenis Wisata")

    # Tombol untuk mencari novel
    if st.button("Cari Wisata"):
        # Filter data berdasarkan input pengguna
        results = data[
            (data['namawisata'].str.contains(namawisata, case=False, na=False) if namawisata else True) &
            (data['jeniswisata'].str.contains(jeniswisata, case=False, na=False) if jeniswisata else True) 
        ]

        # Menampilkan hasil
        if not results.empty:
            st.success(f"Ditemukan {len(results)} wisata yang cocok:")
            st.dataframe(results)
        else:
            st.warning("Tidak ada tempat wisata yang cocok dengan kriteria pencarian.")
except FileNotFoundError:
    st.error("Dataset tidak ditemukan! Pastikan file 'data_wisata.csv' ada di folder yang sama dengan script.")
