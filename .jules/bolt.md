## 2024-05-24 - OpenCV Contour Processing
**Learning:** In heavily noisy images, `cv2.findContours` can return hundreds of thousands of tiny noise contours. Sorting this entire list using a lambda or `cv2.contourArea` key before filtering by `min_area` is an $O(N \log N)$ operation that creates a massive CPU bottleneck.
**Action:** When filtering contours by minimum area, ALWAYS filter using a generator expression or list comprehension BEFORE sorting. This reduces the set of elements to be sorted from $N$ to $K$ valid elements ($O(K \log K)$), and minimizes calls to `cv2.contourArea`.
