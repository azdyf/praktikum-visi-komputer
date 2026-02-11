# 📷 Praktikum 2 – Pengenalan Citra Digital Menggunakan Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?logo=numpy)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📖 Deskripsi

Praktikum ini membahas konsep dasar pengolahan citra digital menggunakan Python dan OpenCV, meliputi:

- Tipe dan ukuran citra
- Format file citra
- Operasi baca dan simpan citra
- Konversi warna (RGB, Grayscale, HSV)
- Thresholding

Praktikum ini menjadi fondasi dalam memahami representasi citra digital sebelum masuk ke tahap Computer Vision yang lebih lanjut.

---

## 🎯 Tujuan Praktikum

Setelah menyelesaikan praktikum ini mampu:

- Memahami tipe-tipe citra digital (Binary, Grayscale, RGB, Indexed)
- Menggunakan fungsi dasar OpenCV
- Melakukan konversi warna
- Melakukan thresholding
- Memproses channel HSV secara manual

---

## 🖼️ Image Types

| Type | Description | Bit Depth |
|------|------------|-----------|
| Binary | Hitam & putih (0 / 1) | 1 bit |
| Grayscale | Intensitas 0 – 255 | 8 bit |
| RGB | Red, Green, Blue | 24 bit |
| Indexed | Menggunakan color palette | Variatif |

RGB memiliki 256³ = **16.777.216 kemungkinan warna**.

---

## 📂 Supported Image Formats

- BMP
- GIF
- JPEG
- PNG
- TIFF

## ⚙️ Fungsi Dasar OpenCV

| Fungsi | Keterangan |
|--------|------------|
| `cv2.imread(filename)` | Membaca citra |
| `cv2.imwrite(filename, image)` | Menyimpan citra |
| `cv2.cvtColor(image, flag)` | Konversi warna |
| `cv2.threshold(source, thresh, maxVal, type)` | Thresholding |