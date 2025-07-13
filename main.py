# EOQ Calculator App
# Simulasi sistem persediaan barang menggunakan model EOQ

import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="EOQ Calculator", layout="centered")

# Judul aplikasi
st.title("Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.write("""
### Deskripsi:
Simulasi ini digunakan untuk menghitung jumlah pemesanan optimal berdasarkan permintaan tahunan,
biaya pemesanan, dan biaya penyimpanan per unit.

### Rumus EOQ:
\[ EOQ = \sqrt{\frac{2DS}{H}} \]
""")

# Input pengguna
st.sidebar.header("Input Parameter")
D = st.sidebar.number_input("Permintaan Tahunan (unit)", min_value=1, value=1000)
S = st.sidebar.number_input("Biaya Pemesanan per Order (Rp)", min_value=1, value=50000)
H = st.sidebar.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1, value=2000)

# Hitung EOQ
def hitung_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

EOQ = hitung_eoq(D, S, H)
jumlah_order_per_tahun = D / EOQ
biaya_total_persediaan = EOQ / 2 * H + (D / EOQ) * S

# Output hasil
st.subheader("Hasil Perhitungan EOQ")
st.write(f"**Jumlah Pemesanan Optimal (EOQ)**: {EOQ:.2f} unit")
st.write(f"**Jumlah Pemesanan per Tahun**: {jumlah_order_per_tahun:.2f} kali")
st.write(f"**Total Biaya Persediaan**: Rp {biaya_total_persediaan:,.2f}")

# Visualisasi sederhana
st.subheader("Interpretasi")
st.markdown(f"Dengan EOQ sebesar **{EOQ:.2f} unit**, perusahaan sebaiknya memesan barang sebanyak itu setiap kali pemesanan dilakukan untuk meminimalkan biaya total persediaan. Dalam satu tahun, diperkirakan akan ada sekitar **{jumlah_order_per_tahun:.2f} kali pemesanan**.")

st.markdown("---")
st.caption("Dibuat untuk simulasi EOQ dalam sistem manajemen persediaan.")
