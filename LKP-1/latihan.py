# Program 1
# Program OpenCV sederhana untuk membaca dan menampilkan citra daun.

# Import package cv2 untuk opencv-python dan numpy
import numpy as np  #untuk meringkas numpy menjadi np agar tidak terlalu panjang
import cv2

#Membaca file bernama daun.jpg
image = cv2.imread('daun.jpg')

#Menampilkan citra
cv2.imshow("Gambar", image)

#Mengambil nilai dimensi (panjang dan lebar) dan channel citra
row,col,ch = image.shape

#Membuat kanvas kosong
kanvas = np.zeros((row,col,3), np.uint8)

#Menyimpan nilai citra pada kanvas
for i in range (0,row):
    for j in range (0,col):
        kanvas[i,j]=image[i,j]

#Menampilkan citra pada canvas
cv2.imshow("Gambar pada kanvas", kanvas)

#Menghentikan gambar hingga pengguna menekan tombol
cv2.waitKey(0)