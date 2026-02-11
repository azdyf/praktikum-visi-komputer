import cv2

# 1) Baca citra
img = cv2.imread("images/Lenna.png")
if img is None:
    print("Citra tidak ditemukan!")
    raise SystemExit

# 2) Konversi ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 3) Split channel HSV
H, S, V = cv2.split(hsv)

# Ambil ukuran citra
rows, cols = H.shape
total_pixel = rows * cols

# 4) Hitung rata-rata intensitas tiap channel (MANUAL)
sum_H = sum_S = sum_V = 0

for i in range(rows):
    for j in range(cols):
        h = int(H[i, j])
        s = int(S[i, j])
        v = int(V[i, j])

        sum_H += h
        sum_S += s
        sum_V += v

mean_H = sum_H / total_pixel
mean_S = sum_S / total_pixel
mean_V = sum_V / total_pixel

print("Rata-rata Hue:", mean_H)
print("Rata-rata Saturation:", mean_S)
print("Rata-rata Value:", mean_V)

# 5) Thresholding manual
H_out = H.copy()
S_out = S.copy()
V_out = V.copy()

for i in range(rows):
    for j in range(cols):
        H_out[i, j] = 255 if int(H[i, j]) >= mean_H else 0
        S_out[i, j] = 255 if int(S[i, j]) >= mean_S else 0
        V_out[i, j] = 255 if int(V[i, j]) >= mean_V else 0

# Simpan hasil (opsional)
cv2.imwrite("images/Hue_Threshold.png", H_out)
cv2.imwrite("images/Saturati on_Threshold.png", S_out)
cv2.imwrite("images/Value_Threshold.png", V_out)

# 6) Tampilkan hasil
cv2.imshow("Hue Threshold", H_out)
cv2.imshow("Saturation Threshold", S_out)
cv2.imshow("Value Threshold", V_out)

cv2.waitKey(0)
cv2.destroyAllWindows()