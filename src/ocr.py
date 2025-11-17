import time

import cv2
from onnxocr.onnx_paddleocr import ONNXPaddleOcr  # type: ignore

model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False, lang="japan")


img = cv2.imread("/workspace/xxxxxxxx")
s = time.time()
result = model.ocr(img)  # type: ignore
e = time.time()
print(f"total time: {e - s:.3f}")
print("result:", result)  # type: ignore
for box in result[0]:  # type: ignore
    print(box)  # type: ignore
