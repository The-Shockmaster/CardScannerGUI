## 2024-05-24 - OpenCV findContours sorting bottleneck
**Learning:** `cv2.findContours` often returns thousands of tiny noise contours. Sorting the entire list with `sorted(contours, key=cv2.contourArea, reverse=True)` before filtering applies an O(N log N) operation on potentially massive amounts of noise, causing significant slowdowns.
**Action:** Always filter contours by minimum area (e.g., using a list comprehension) BEFORE sorting the remaining valid contours in-place.
