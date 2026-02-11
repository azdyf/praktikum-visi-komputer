import cv2
# buka citra
img = cv2.imread('images/Lenna.png')
# assign row col
row, col, ch = img.shape
# buat salinan dari citra yang akan dijadikan grayscale
img_gray = img.copy()
# ubah color space dari img_gray menjadi grayscale
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
# fungsi threshold. Semua pixel yang bernilai di atas 100
# akan diubah menjadi 255, selainnya menjadi 0.
ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
# tampilkan citra hasil
cv2.imshow('threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()