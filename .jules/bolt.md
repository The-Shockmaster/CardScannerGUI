## 2024-05-15 - Pre-filter Contours Before Sorting
**Learning:** Sorting raw results from `cv2.findContours` before filtering out noise by area causes an expensive O(N log N) sorting operation on thousands of noise artifacts.
**Action:** Always pre-filter OpenCV contours by area or other criteria *before* applying sorting operations to turn O(N log N) into O(K log K) where K << N.
