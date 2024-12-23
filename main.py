import streamlit as st
from aritmatika import aritmatika_iteratif, aritmatika_rekursif
from analisis import analisis_efisiensi

# Judul Aplikasi
st.title("Aplikasi Perbandingan Deret Aritmatika: Iteratif vs Rekursif")
st.write("Masukkan nilai **N** untuk menghitung jumlah deret aritmatika dari 1 ke N.")

# Input dari pengguna
n = st.number_input("Masukkan nilai N:", min_value=1, step=1, value=10)

# Hitung dengan Iteratif
if st.button("Hitung Jumlah Deret"):
    hasil_iteratif = aritmatika_iteratif(n)
    hasil_rekursif = aritmatika_rekursif(n)

    st.success(f"**Versi Iteratif**: Jumlah deret aritmatika dari 1 ke {n} adalah {hasil_iteratif}")
    st.success(f"**Versi Rekursif**: Jumlah deret aritmatika dari 1 ke {n} adalah {hasil_rekursif}")

# Analisis Efisiensi
st.subheader("Analisis Waktu Eksekusi")
if st.button("Lakukan Analisis"):
    st.write("Analisis akan membandingkan waktu eksekusi dari algoritma Iteratif dan Rekursif untuk berbagai ukuran input.")
    fig = analisis_efisiensi()  # Ambil figure dari fungsi analisis_efisiensi
    st.pyplot(fig)  # Tampilkan figure di Streamlit