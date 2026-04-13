## 2024-04-13 - O(N log N) Contour Sorting Bottleneck
**Learning:** Sorting raw `cv2.findContours` output by area before filtering forces an expensive O(N log N) operation on thousands of noise artifacts. Pre-filtering by area first reduces N significantly.
**Action:** Always pre-filter contours (or any large datasets with noise) before applying sorting or other expensive operations in OpenCV pipelines.
