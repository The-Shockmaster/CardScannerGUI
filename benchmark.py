import cv2
import numpy as np
import time

# Create dummy contours, many small ones and few large ones
contours = []
for _ in range(10000):
    # small noise
    c = np.array([[[0,0]], [[0,1]], [[1,1]], [[1,0]]], dtype=np.int32)
    contours.append(c)

for _ in range(10):
    # large contours
    c = np.array([[[0,0]], [[0,100]], [[100,100]], [[100,0]]], dtype=np.int32)
    contours.append(c)

min_area = 5000

start = time.time()
# Original
found = 0
for i, contour in enumerate(sorted(contours, key=cv2.contourArea, reverse=True)):
    if cv2.contourArea(contour) < min_area: continue
    found += 1
t1 = time.time() - start

start = time.time()
# Optimized
valid_contours = []
for c in contours:
    area = cv2.contourArea(c)
    if area >= min_area:
        valid_contours.append((area, c))
valid_contours.sort(key=lambda x: x[0], reverse=True)
found2 = 0
for i, (area, contour) in enumerate(valid_contours):
    found2 += 1
t2 = time.time() - start

print(f"Original: {t1:.4f}s")
print(f"Optimized: {t2:.4f}s")
print(f"Speedup: {t1/t2:.2f}x")
