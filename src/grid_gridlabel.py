import sys

import cv2


def draw_grid_with_labels(*, image_path: str) -> None:
    # 画像パスを指定
    img_path = image_path
    img = cv2.imread(img_path)

    height, width = img.shape[:2]

    # グリッド間隔
    step = 50
    color = (0, 255, 0)  # 緑
    thickness = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.3
    font_color = (0, 0, 255)  # 赤
    font_thickness = 1

    # 縦線
    for x in range(0, width, step):
        cv2.line(img, (x, 0), (x, height), color, thickness)
    # 横線
    for y in range(0, height, step):
        cv2.line(img, (0, y), (width, y), color, thickness)

    # 座標ラベル
    for y in range(0, height, step):
        for x in range(0, width, step):
            label = f"{x},{y}"
            cv2.putText(img, label, (x + 1, y + 8), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

    # 保存
    cv2.imwrite(f"/workspace/grid_output_{img_path.split('/')[-1].split('.')[0]}.jpg", img)
    print(f"グリッド画像を /workspace/grid_output_{img_path.split('/')[-1].split('.')[0]}.jpg に保存しました")


if __name__ == "__main__":
    image_path = sys.argv[1]
    draw_grid_with_labels(image_path=image_path)
