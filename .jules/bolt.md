## 2026-05-28 - OpenCV releases GIL for true multithreading
**Learning:** In Python, OpenCV (cv2) operations are implemented in C and release the Global Interpreter Lock (GIL). This means we can achieve true multi-threading for heavy image processing tasks using `concurrent.futures.ThreadPoolExecutor`, rather than needing `ProcessPoolExecutor`.
**Action:** Always consider `ThreadPoolExecutor` for batch OpenCV/image processing operations instead of sequential loops.
