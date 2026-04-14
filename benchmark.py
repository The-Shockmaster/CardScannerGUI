import cv2
import numpy as np
import time

def generate_contours(num_contours, num_valid):
    contours = []
    # Add valid contours
    for _ in range(num_valid):
        # Create a contour with area > 5000
        c = np.array([[[0, 0]], [[100, 0]], [[100, 100]], [[0, 100]]])
        contours.append(c)
    # Add noise contours
    for _ in range(num_contours - num_valid):
        # Create a contour with area < 5000
        c = np.array([[[0, 0]], [[10, 0]], [[10, 10]], [[0, 10]]])
        contours.append(c)
    return contours

contours = generate_contours(5000, 5)

start = time.time()
for _ in range(100):
    for i, contour in enumerate(sorted(contours, key=cv2.contourArea, reverse=True)):
        if cv2.contourArea(contour) < 5000: continue
        pass
end = time.time()
print(f"Original: {end - start:.4f}s")

start = time.time()
for _ in range(100):
    filtered_contours = [c for c in contours if cv2.contourArea(c) >= 5000]
    for i, contour in enumerate(sorted(filtered_contours, key=cv2.contourArea, reverse=True)):
        pass
end = time.time()
print(f"Optimized: {end - start:.4f}s")
