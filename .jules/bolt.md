## 2024-04-15 - Contour Pre-Filtering
**Learning:** Pre-filtering `cv2.findContours` results by area before sorting them prevents redundant calculations and expensive `O(N log N)` sorting operations on noise artifacts. Sorting first then filtering is an anti-pattern.
**Action:** Always filter OpenCV contours by minimum area (or other gating criteria) before applying expensive ranking or sorting operations.
