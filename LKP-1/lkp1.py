# ======================================================
# Praktikum 1
# Nama  : Azdi Fahmi
# NIM   : M0503251018
# MK    : Visi Komputer dalam Pertanian Cerdas
# ======================================================

# Import library
import numpy as np
import cv2

# Menentukan ukuran citra
N = 256     # Ukuran citra 256x256 piksel

# =====================================================
# SOAL 1: Membuat Matriks Citra Grayscale
# =====================================================

# Membuat matriks kosong berukuran 256x256
# dtype uint8 digunakan agar nilai pixel berada pada rentang 0–255
citra = np.zeros((N, N), dtype=np.uint8)

# Mengisi nilai pixel dengan gradien vertikal
# Nilai pixel tergantung indeks baris (i)
for i in range(N):
    for j in range(N):
        citra[i, j] = i # Semakin ke bawah semakin terang

# Menampilkan informasi matriks
print("SOAL 1")
print("Matriks citra:\n", citra)

# Menampilkan citra hasil Soal 1
cv2.imshow("Soal 1 - Citra Grayscale", citra)
cv2.waitKey(0)
cv2.destroyAllWindows()


# =====================================================
# SOAL 2: Mengganti Nilai Pixel < 150 menjadi 255
# =====================================================

# Menyalin citra agar citra asli tidak berubah
citra_edit = citra.copy()

# Mengecek setiap pixel pada citra
for i in range(N):
    for j in range(N):
        # Jika nilai pixel kurang dari 150
        if citra_edit[i, j] < 150:
            citra_edit[i, j] = 255   # Ubah nilai pixel menjadi 255 (putih)

print("\nSOAL 2")
print("Matriks citra:\n", citra_edit)

# Menampilkan citra hasil Soal 2
cv2.imshow("Soal 2 - Pixel < 150 menjadi 255", citra_edit)
cv2.waitKey(0)
cv2.destroyAllWindows()


# =====================================================
# SOAL 3: Membalik Matriks (Transpose)
# =====================================================

# Membuat matriks kosong untuk menampung hasil transpose
transpose = np.zeros((N, N), dtype=np.uint8)

# Proses transpose: menukar baris dan kolom
for i in range(N):
    for j in range(N):
        transpose[j, i] = citra[i, j]

print("\nSOAL 3")
print("Matriks citra awal:\n", citra)
print("Matriks citra transpose:\n", transpose)

# Menampilkan citra awal dan citra hasil transpose
cv2.imshow("Soal 3 - Citra Awal", citra)
cv2.imshow("Soal 3 - Citra Transpose", transpose)
cv2.waitKey(0)
cv2.destroyAllWindows()