import argparse

import cv2


def draw_grid_with_labels(*, image_path: str, grid_step: int = 50, label_step: int = 50) -> None:
    img_path = image_path
    img = cv2.imread(img_path)
    height, width = img.shape[:2]
    color = (0, 255, 0)  # 緑
    thickness = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.3
    font_color = (0, 0, 255)  # 赤
    font_thickness = 1

    # グリッド線
    for x in range(0, width, grid_step):
        cv2.line(img, (x, 0), (x, height), color, thickness)
    for y in range(0, height, grid_step):
        cv2.line(img, (0, y), (width, y), color, thickness)

    # ラベル
    for y in range(0, height, label_step):
        for x in range(0, width, label_step):
            label = f"{x},{y}"
            cv2.putText(img, label, (x + 1, y + 8), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

    cv2.imwrite(f"grid_output_{img_path.split('/')[-1].split('.')[0]}.jpg", img)
    print(f"グリッド画像を grid_output_{img_path.split('/')[-1].split('.')[0]}.jpg に保存しました")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    parser.add_argument("--grid_step", type=int, default=10)
    parser.add_argument("--label_step", type=int, default=50)
    args = parser.parse_args()
    draw_grid_with_labels(image_path=args.image_path, grid_step=args.grid_step, label_step=args.label_step)
