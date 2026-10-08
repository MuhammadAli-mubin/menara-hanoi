# menara-hanoi
Tugas Game Developer

# Penyelesaian Menara Hanoi (Tower of Hanoi)

## Deskripsi Masalah
Tugas ini adalah permainan **Menara Hanoi** dengan 3 buah piringan yang berpindah dari **Tiang A (Start)** ke **Tiang C (Finish)** menggunakan **Tiang B** sebagai bantuan.

## Aturan Permainan
1. Hanya satu piringan yang boleh dipindahkan dalam satu waktu.
2. Piringan yang lebih besar tidak boleh diletakkan di atas piringan yang lebih kecil.

## Logika & Pendekatan (Algoritma Rekursif)
Program ini menggunakan fungsi rekursif dengan kompleksitas waktu $O(2^n - 1)$. Untuk 3 piringan, dibutuhkan total $2^3 - 1 = 7$ langkah pemindahan yang dieksekusi otomatis oleh kode Python dalam file `hanoi.py`.
