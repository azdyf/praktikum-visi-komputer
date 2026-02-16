# =========================
# Praktikum 3 - Histogram
# =========================

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Output folder
# =========================
OUTDIR = "output"
os.makedirs(OUTDIR, exist_ok=True)

# =========================
# 1) Baca citra grayscale
# =========================
img = cv2.imread("melon.jpg", 0)
if img is None:
    raise FileNotFoundError("File 'melon.jpg' tidak ditemukan.")

# ============================================
# 2) Contrast Stretching (sesuai modul)
# g(x,y) = (f(x,y)-fmin)/(fmax-fmin) * 255
# ============================================
def contrastStretching(image: np.ndarray) -> np.ndarray:
    fmin = int(np.min(image))
    fmax = int(np.max(image))
    if fmax == fmin:
        return image.copy()

    stretched = (image.astype(np.float32) - fmin) / (fmax - fmin) * 255.0
    stretched = np.clip(stretched, 0, 255).astype(np.uint8)
    return stretched

# ===============================================
# 3) Histogram Equalization Manual (Sesuai modul)
# - hist
# - normalized hist
# - CDF
# - mapping: s_k = CDF(r_k) * 255
# ===============================================
def histogramEqualization(image: np.ndarray):
    # Histogram kemunculan
    hist = np.zeros(256, dtype=np.int64)
    for p in image.ravel():
        hist[int(p)] += 1

    # Normalized histogram
    total = image.size
    hist_norm = hist / total

    # CDF
    cdf = np.cumsum(hist_norm)

    # Mapping sesuai modul (tanpa cdf_min)
    mapping = np.round(cdf * 255.0)
    mapping = np.clip(mapping, 0, 255).astype(np.uint8)

    # Apply mapping
    equalized = mapping[image]
    return hist, hist_norm, cdf, mapping, equalized

# =========================
# Proses
# =========================
stretched = contrastStretching(img)
hist, hist_norm, cdf, mapping, equalized = histogramEqualization(img)

# Histogram citra equalized (normalized)
hist_eq = np.zeros(256, dtype=np.int64)
for p in equalized.ravel():
    hist_eq[int(p)] += 1
hist_eq_norm = hist_eq / equalized.size

# =========================
# Simpan citra output
# =========================
plt.imsave(os.path.join(OUTDIR, "01_original.png"), img, cmap="gray")
plt.imsave(os.path.join(OUTDIR, "02_contrast_stretching.png"), stretched, cmap="gray")
plt.imsave(os.path.join(OUTDIR, "03_histogram_equalization.png"), equalized, cmap="gray")

# =========================
# Helper simpan figure
# =========================
def save_fig(filename):
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, filename), dpi=200)
    plt.close()

# ================================
# Simpan histogram satu-satu (PNG)
# ================================

# Histogram original (count)
plt.figure(figsize=(6,4))
plt.hist(img.ravel(), bins=256, range=(0,256))
plt.title("Histogram Original")
save_fig("04_hist_original.png")

# Histogram contrast stretching (count)
plt.figure(figsize=(6,4))
plt.hist(stretched.ravel(), bins=256, range=(0,256))
plt.title("Histogram Contrast Stretching")
save_fig("05_hist_contrast_stretching.png")

# Normalized histogram (bar)
plt.figure(figsize=(6,4))
plt.bar(np.arange(256), hist_norm, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Normalized Histogram")
plt.xlim(0,255)
save_fig("06_normalized_hist.png")

# CDF (bar)
plt.figure(figsize=(6,4))
plt.bar(np.arange(256), cdf, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Cumulative Histogram (CDF)")
plt.xlim(0,255)
plt.ylim(0,1.0)
save_fig("07_cumulative_hist.png")

# Equalized histogram (normalized, bar)
plt.figure(figsize=(6,4))
plt.bar(np.arange(256), hist_eq_norm, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Equalized Histogram (Normalized)")
plt.xlim(0,255)
save_fig("08_equalized_hist.png")

# =========================
# Panel 2x2
# =========================
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.hist(img.ravel(), bins=256, range=(0,256))
plt.title("Histogram")

plt.subplot(2,2,2)
plt.bar(np.arange(256), hist_norm, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Normalized Histogram")
plt.xlim(0,255)

plt.subplot(2,2,3)
plt.bar(np.arange(256), cdf, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Cumulative Histogram")
plt.xlim(0,255)
plt.ylim(0,1.0)

plt.subplot(2,2,4)
plt.bar(np.arange(256), hist_eq_norm, width=0.9, align="edge", edgecolor="white", linewidth=0.2)
plt.title("Equalized Histogram")
plt.xlim(0,255)

plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "09_panel_histograms_2x2.png"), dpi=200)
plt.show()

# =========================
# Tampilkan hasil citra
# =========================
cv2.imshow("Original", img)
cv2.imshow("Contrast Stretching", stretched)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Selesai. Semua output tersimpan di: {OUTDIR}")