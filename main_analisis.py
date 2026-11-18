"""
Program utama untuk demonstrasi modularisasi fungsi analisis penjualan toko.

Simpan file ini dalam satu folder bersama `analisis_penjualan.py`, 
kemudian jalankan: python main.py
"""

from analisis_penjualan import (
    hitung_rata_rata_penjualan,
    cari_penjualan_minimum,
    cari_penjualan_maksimum,
    klasifikasi_performa_penjualan
)


def tampilkan_ringkasan_cabang(nama_cabang, data_penjualan):
    """Menampilkan ringkasan laporan analisis penjualan untuk satu cabang toko.

    Fungsi ini memanfaatkan fungsi-fungsi reusable dari modul `analisis_penjualan`.
    """
    print("\n" + "=" * 60)
    print(f"LAPORAN PERFORMA PENJUALAN: {nama_cabang.upper()}")
    print("=" * 60)
    print("Data Omset Harian (Juta Rp):", data_penjualan)

    rata_rata = hitung_rata_rata_penjualan(data_penjualan)
    minimum = cari_penjualan_minimum(data_penjualan)
    maksimum = cari_penjualan_maksimum(data_penjualan)

    if rata_rata is None:
        print("Peringatan: Tidak ada data transaksi yang dapat diolah.")
        return

    print("Jumlah Hari Transaksi     :", len(data_penjualan), "hari")
    print(f"Rata-rata Omset Harian    : Rp {rata_rata:.2f} Juta")
    print(f"Omset Terendah            : Rp {minimum:.2f} Juta")
    print(f"Omset Tertinggi           : Rp {maksimum:.2f} Juta")
    print("Kategori Performa Cabang  :", klasifikasi_performa_penjualan(rata_rata))


def demo_pengujian_klasifikasi():
    """Demonstrasi pengujian klasifikasi performa untuk berbagai kondisi nilai batas."""
    print("\n" + "=" * 60)
    print("PENGUJIANKLASIFIKASI PERFORMA OMSET (NILAI BATAS)")
    print("=" * 60)
    
    kasus_uji = [10, 15, 29.5, 30, 49.9, 50, -5]
    for omset in kasus_uji:
        label = klasifikasi_performa_penjualan(omset)
        print(f"Omset Rp {omset:>5} Juta -> Kategori: {label}")


def main():
    """Menjalankan alur demonstrasi utama program analisis penjualan."""
    print("SISTEM ANALISIS OPERASIONAL RETAIL E-COMMERCE")
    print("PENERAPAN KONSEP FUNCTION DAN MODULARISASI PYTHON")

    # Dataset simulasi penjualan harian (dalam juta Rupiah) untuk beberapa cabang
    cabang_jakarta = [45.5, 52.0, 60.0, 48.0, 55.5]
    cabang_bandung = [20.0, 25.5, 18.0, 32.0, 22.0]
    cabang_surabaya = [12.0, 10.5, 14.0, 8.5]
    cabang_baru = []  # Data kosong untuk uji kondisi edge case

    # Pemanggilan fungsi ringkasan untuk setiap dataset (Reusable Function)
    tampilkan_ringkasan_cabang("Cabang Jakarta", cabang_jakarta)
    tampilkan_ringkasan_cabang("Cabang Bandung", cabang_bandung)
    tampilkan_ringkasan_cabang("Cabang Surabaya", cabang_surabaya)
    tampilkan_ringkasan_cabang("Cabang Baru (Belum Operasional)", cabang_baru)

    # Pengujian kondisi khusus / nilai batas
    demo_pengujian_klasifikasi()

    print("\n" + "=" * 60)
    print("Analisis selesai. Seluruh fungsi dipanggil secara reusable dari modul terpisah.")


if __name__ == "__main__":
    main()