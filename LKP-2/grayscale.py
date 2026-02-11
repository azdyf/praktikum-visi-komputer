import cv2
# buka citra
img = cv2.imread('images/Lenna.png')
# assign row col
row, col, ch = img.shape
# buat salinan dari citra yang akan dijadikan grayscale
img_gray = img.copy()
# ubah color space dari img_gray menjadi grayscale
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
# simpan citra ke sebuah file
cv2.imwrite('images/lenna_grayscale.jpg', img_gray)