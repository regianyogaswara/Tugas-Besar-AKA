import time
import matplotlib.pyplot as plt
from aritmatika import aritmatika_iteratif, aritmatika_rekursif
import sys
sys.setrecursionlimit(55000)

# Fungsi untuk menghitung waktu eksekusi
def hitung_waktu(fungsi, n):
    start_time = time.time()
    fungsi(n)
    end_time = time.time()
    return end_time - start_time

# Analisis untuk berbagai ukuran input
def analisis_efisiensi():
    input_sizes = [1, 10, 100]
    iteratif_times = []
    rekursif_times = []

    for n in input_sizes:
        waktu_iteratif = hitung_waktu(aritmatika_iteratif, n)
        waktu_rekursif = hitung_waktu(aritmatika_rekursif, n)

        iteratif_times.append(waktu_iteratif)
        rekursif_times.append(waktu_rekursif)

    # Membuat Grafik
    fig, ax = plt.subplots(figsize=(10, 6))  # Buat figure dan axis
    ax.plot(input_sizes, iteratif_times, label="Iteratif", marker='o')
    ax.plot(input_sizes, rekursif_times, label="Rekursif", marker='o')
    ax.set_xlabel("Ukuran Input (N)")
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.set_title("Perbandingan Waktu Eksekusi Iteratif vs Rekursif")
    ax.legend()
    ax.grid()

    return fig  # Return figure
