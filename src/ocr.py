import sys

import cv2
from onnxocr.onnx_paddleocr import ONNXPaddleOcr  # type: ignore

model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False, lang="japan")


def ocr_image(*, image_path: str) -> list[str]:
    img = cv2.imread(image_path)
    # 今回扱う画像は全て一部分だけ切り抜かれているのでとても小さい
    # そのため、OCRの精度を上げるために5倍に拡大する
    img = cv2.resize(img, None, fx=5.0, fy=5.0, interpolation=cv2.INTER_CUBIC)

    result = model.ocr(img)  # type: ignore

    texts: list[str] = []
    for box in result[0]:  # type: ignore
        print(box)  # type: ignore
        texts.append(box[1][0])  # type: ignore

    print(f"OCR結果: {image_path} -> {texts}")

    return texts


if __name__ == "__main__":
    image_path = sys.argv[1]
    texts = ocr_image(image_path=image_path)

    for text in texts:
        print(text)
