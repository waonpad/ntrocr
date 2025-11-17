import cv2

# TODO: weapon_typeのOCR結果が杖か聖印だったらspell_y_bufferを60にする
# spell_y_buffer = 60
spell_y_buffer = 0

player_y_buffer = 155

paths = {
    # "weapon_full": {"x1": 600, "y1": 150, "x2": 1200, "y2": 600},
    # 武器種の中のどれか
    "weapon_type": {"x1": 600, "y1": 150, "x2": 730, "y2": 180},
    # 武器名の中のどれかか、派生した事で変わった名前
    "weapon_name": {"x1": 730, "y1": 230, "x2": 1200, "y2": 260},
    # 2~4桁の数字
    "weapon_attack": {"x1": 930, "y1": 260, "x2": 1050, "y2": 290},
    # 魔術, 祈祷1つ目 or 戦技
    "weapon_skill_or_spell_1": {"x1": 680, "y1": 360, "x2": 1200, "y2": 390},
    # 杖か祈祷なら魔術, 祈祷2つ目、でなければ取得しない
    "weapon_spell_2": {"x1": 680, "y1": 430, "x2": 1200, "y2": 460},
    # 付帯効果1つ目の名前
    "weapon_accessory_1_name": {"x1": 680, "y1": 430 + spell_y_buffer, "x2": 1070, "y2": 460 + spell_y_buffer},
    # 付帯効果1つ目の符号(+, _, 空文字)
    "weapon_accessory_1_value_sign": {"x1": 1070, "y1": 430 + spell_y_buffer, "x2": 1090, "y2": 460 + spell_y_buffer},
    # 付帯効果1つ目の数値(1~3桁の数値 + %があるかもしれない, 空文字の可能性もあり)
    "weapon_accessory_1_value": {"x1": 1100, "y1": 430 + spell_y_buffer, "x2": 1180, "y2": 460 + spell_y_buffer},
    # 2つ目以降は全て空文字の可能性がある
    "weapon_accessory_2_name": {"x1": 680, "y1": 470 + spell_y_buffer, "x2": 1070, "y2": 500 + spell_y_buffer},
    "weapon_accessory_2_value_sign": {"x1": 1070, "y1": 470 + spell_y_buffer, "x2": 1090, "y2": 500 + spell_y_buffer},
    "weapon_accessory_2_value": {"x1": 1100, "y1": 470 + spell_y_buffer, "x2": 1180, "y2": 500 + spell_y_buffer},
    "weapon_accessory_3_name": {"x1": 680, "y1": 510 + spell_y_buffer, "x2": 1070, "y2": 530 + spell_y_buffer},
    "weapon_accessory_3_value_sign": {"x1": 1070, "y1": 510 + spell_y_buffer, "x2": 1090, "y2": 530 + spell_y_buffer},
    "weapon_accessory_3_value": {"x1": 1100, "y1": 510 + spell_y_buffer, "x2": 1180, "y2": 530 + spell_y_buffer},
    # タリスマン
    #
    # 夜の王アイコン(画像認識?)
    #
    # 到達日(最初の日, 次の日, 最期の日)
    "arrival_date": {"x1": 1430, "y1": 180, "x2": 1530, "y2": 210},
    # 勝ち負け(光があるか無いか, 画像認識?)
    "game_result": {"x1": 1670, "y1": 180, "x2": 1690, "y2": 210},
    "player": {
        # キャラアイコン(画像認識?)
        #
        # 文字列
        "name": {"x1": 1410, "y1": 290, "x2": 1700, "y2": 320},
        # 1~2桁の数値
        "level": {"x1": 1830, "y1": 290, "x2": 1860, "y2": 320},
        # 1~3桁の数値
        "defeated_enemies": {"x1": 1430, "y1": 330, "x2": 1480, "y2": 350},
        # 1~2桁の数値
        "frasco": {"x1": 1600, "y1": 330, "x2": 1640, "y2": 350},
        # 1~8桁の数値
        "runes": {"x1": 1750, "y1": 330, "x2": 1860, "y2": 350},
    },
    # 1~3桁の数値
    "defeated_enemies": {"x1": 1790, "y1": 770, "x2": 1860, "y2": 800},
    # 1~2桁の数値
    "defeated_bosses": {"x1": 1790, "y1": 800, "x2": 1860, "y2": 830},
    # 1~n桁の数値
    "treasures": {"x1": 1790, "y1": 830, "x2": 1860, "y2": 860},
    # 救助
    "rescues": {"x1": 1790, "y1": 860, "x2": 1860, "y2": 890},
    # 5桁区切りで-が3つある数値
    "session_id": {"x1": 1570, "y1": 920, "x2": 1860, "y2": 950},
}

# 画像パスと切り取り範囲を指定
img_path = "/workspace/images/20251028014715_1.jpg"

img = cv2.imread(img_path)


# 全部切り取り
for key, path in paths.items():
    # playerだけは、player_y_bufferをyに加算して3回切り取り
    if key == "player":
        for i in range(3):
            for pkey, ppath in path.items():
                crop = img[
                    ppath["y1"] + i * player_y_buffer : ppath["y2"] + i * player_y_buffer,  # type: ignore
                    ppath["x1"] : ppath["x2"],  # type: ignore
                ]
                cv2.imwrite(f"/workspace/crop_{key}_{i + 1}_{pkey}.jpg", crop)
                print(f"切り取った画像を /workspace/crop_{key}_{i + 1}_{pkey}.jpg に保存しました")
        continue

    crop = img[path["y1"] : path["y2"], path["x1"] : path["x2"]]
    cv2.imwrite(f"/workspace/crop_{key}.jpg", crop)
    print(f"切り取った画像を /workspace/crop_{key}.jpg に保存しました")
