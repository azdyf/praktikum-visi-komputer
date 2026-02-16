# Praktikum 3 – Histogram, Contrast Stretching, dan Histogram Equalization

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?logo=numpy)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Deskripsi

Project ini merupakan implementasi Praktikum 3 pada mata kuliah Visi Komputer.  
Program mengolah citra grayscale menggunakan:

- Histogram Citra
- Contrast Stretching
- Histogram Equalization (manual tanpa fungsi bawaan OpenCV)

Seluruh proses dilakukan sesuai dengan rumus dan algoritme pada modul praktikum.

---

## 🎯 Tujuan

1. Menampilkan histogram citra grayscale.
2. Mengimplementasikan contrast stretching.
3. Mengimplementasikan histogram equalization secara manual.
4. Menganalisis perubahan histogram dan kualitas citra.

---

## 🧠 Dasar Teori

### 1️⃣ Contrast Stretching

Meningkatkan kontras citra dengan memperlebar rentang intensitas piksel menggunakan rumus:

$$
g(x,y) = \frac{f(x,y) - f_{min}}{f_{max} - f_{min}} \times 255
$$

Metode ini bersifat **linier** dan meningkatkan kontras global citra.

---

### 2️⃣ Histogram Equalization

Meningkatkan kontras citra dengan meratakan distribusi intensitas menggunakan Cumulative Distribution Function (CDF).

Langkah-langkah:

1. Hitung histogram
2. Hitung normalized histogram
3. Hitung cumulative histogram (CDF)
4. Transformasi intensitas:

$$
s_k = CDF(r_k) \times 255
$$

Metode ini bersifat **non-linier** dan biasanya menghasilkan detail yang lebih jelas dibanding contrast stretching.


