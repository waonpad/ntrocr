from pathlib import Path
import time

import pyautogui

# 横に50、縦に150ずつ移動
# 横にloop_x回移動した後、縦にstep_y移動してまた横にloop_x回移動を繰り返す
step_x = 50
step_y = 150
# 武器6つ+タリスマン2つ
loop_x = 8
# 最大3人
loop_y = 3

# 座標一覧
player_1_weapon_coords_start = {"x": 1360, "y": 390}


def main() -> None:
    Path("screenshots").mkdir(exist_ok=True)

    for y in range(loop_y):
        for x in range(loop_x):
            coord_x = player_1_weapon_coords_start["x"] + step_x * x
            coord_y = player_1_weapon_coords_start["y"] + step_y * y

            print(f"移動先: ({coord_x}, {coord_y})")

            pyautogui.moveTo(coord_x, coord_y)
            # スクショ
            scr = pyautogui.screenshot().convert("RGB")
            if x < 6:
                scr.save(f"screenshots/player_{y + 1}_weapon_{x + 1}.jpg")
            else:
                scr.save(f"screenshots/player_{y + 1}_talisman_{x - 5}.jpg")

            time.sleep(0.5)  # クリック後に少し待つ


if __name__ == "__main__":
    main()
