"""
Modul fungsi analisis penjualan harian untuk operasional toko retail/e-commerce.

Modul ini berisi fungsi-fungsi reusable untuk mengolah data nominal penjualan
harian cabang toko, meliputi rata-rata penjualan, omset minimum, omset maksimum,
serta klasifikasi performa penjualan.
"""

def hitung_rata_rata_penjualan(data_penjualan):
    """Menghitung rata-rata penjualan harian dari kumpulan data nominal.

    Args:
        data_penjualan (list): Kumpulan angka nominal penjualan dalam juta Rp.

    Returns:
        float | None: Nilai rata-rata penjualan. Mengembalikan None jika data kosong.
    """
    if len(data_penjualan) == 0:
        return None
    return sum(data_penjualan) / len(data_penjualan)


def cari_penjualan_minimum(data_penjualan):
    """Mengembalikan nilai penjualan terkecil dalam periode tersebut.

    Args:
        data_penjualan (list): Kumpulan angka nominal penjualan.

    Returns:
        int | float | None: Nominal penjualan terkecil, atau None jika data kosong.
    """
    if len(data_penjualan) == 0:
        return None
    return min(data_penjualan)


def cari_penjualan_maksimum(data_penjualan):
    """Mengembalikan nilai penjualan terbesar dalam periode tersebut.

    Args:
        data_penjualan (list): Kumpulan angka nominal penjualan.

    Returns:
        int | float | None: Nominal penjualan terbesar, atau None jika data kosong.
    """
    if len(data_penjualan) == 0:
        return None
    return max(data_penjualan)


def klasifikasi_performa_penjualan(rata_rata_omset):
    """Mengelompokkan performa rata-rata penjualan ke dalam kategori bisnis.

    Aturan Kategori (dalam Juta Rupiah):
        >= 50    : Sangat Tinggi (Target Terlampaui)
        30 - <50 : Tinggi (Memenuhi Target)
        15 - <30 : Cukup (Stabil)
        0  - <15 : Rendah (Perlu Evaluasi & Promosi)

    Args:
        rata_rata_omset (int | float): Rata-rata omset harian dalam juta rupiah.

    Returns:
        str: Kategori performa toko atau 'Nilai tidak valid' jika di luar rentang.
    """
    if rata_rata_omset is None or rata_rata_omset < 0:
        return "Nilai tidak valid"
    elif rata_rata_omset >= 50:
        return "Sangat Tinggi (Target Terlampaui)"
    elif rata_rata_omset >= 30:
        return "Tinggi (Memenuhi Target)"
    elif rata_rata_omset >= 15:
        return "Cukup (Stabil)"
    else:
        return "Rendah (Perlu Evaluasi & Promosi)"