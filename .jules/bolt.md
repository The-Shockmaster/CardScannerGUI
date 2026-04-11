## 2024-04-11 - Pre-filtering Contours
**Learning:** In image processing pipelines (like CardScannerGUI.py), `cv2.findContours` can return tens of thousands of tiny noise contours. Sorting all of them before filtering is an O(N log N) operation on a large N, and re-calculating `cv2.contourArea` during iteration is wasteful.
**Action:** Always filter out noise (e.g., area < min_area) with a single pass O(N) before sorting the surviving contours.
