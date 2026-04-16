## 2024-05-18 - Pre-filtering contours before sorting
**Learning:** In OpenCV image processing pipelines (e.g., `CardScannerGUI.py`), `cv2.findContours` often returns thousands of tiny noise artifacts. Directly sorting these by area is an expensive `O(N log N)` operation on mostly useless data.
**Action:** Always pre-filter `contours` by area (e.g., `[c for c in contours if cv2.contourArea(c) >= MIN_AREA]`) before sorting to drastically reduce the array size and improve performance.
