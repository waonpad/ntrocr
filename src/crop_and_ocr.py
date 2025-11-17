import json
import sys

from src.crop_image import crop_image
from src.ocr import ocr_image
from src.validators import (
    validate_arrival_date,
    validate_defeated_bosses,
    validate_defeated_enemies,
    validate_player_defeated_enemies,
    validate_player_frasco,
    validate_player_level,
    validate_player_name,
    validate_player_runes,
    validate_rescues,
    validate_session_id,
    validate_treasures,
)


def crop_and_ocr(*, image_path: str) -> None:
    crop_result = crop_image(image_path=image_path)

    texts: dict[str, str] = {}

    for cropped_image_path in crop_result:
        name = cropped_image_path.stem

        # OCR処理を行う
        texts[name] = "".join(ocr_image(image_path=str(cropped_image_path)))

    # バリデーションと整形
    arrival_date = validate_arrival_date(arrival_date=texts["arrival_date"])
    defeated_bosses = validate_defeated_bosses(defeated_bosses=texts["defeated_bosses"])
    defeated_enemies = validate_defeated_enemies(defeated_enemies=texts["defeated_enemies"])
    game_result = texts["game_result"]
    players: list[dict[str, int | str]] = []
    # 1~3までのindexで回す
    for i in range(1, 4):
        # プレイヤーが3人未満の可能性もある
        exist_name_key = f"player_{i}_name"
        if exist_name_key not in texts:
            break

        player = {
            "name": validate_player_name(name=texts[f"player_{i}_name"]),
            "level": validate_player_level(level=texts[f"player_{i}_level"]),
            "defeated_enemies": validate_player_defeated_enemies(
                defeated_enemies=texts[f"player_{i}_defeated_enemies"]
            ),
            "frasco": validate_player_frasco(frasco=texts[f"player_{i}_frasco"]),
            "runes": validate_player_runes(runes=texts[f"player_{i}_runes"]),
        }
        # 武器は本来ここに入るべき
        players.append(player)
    rescues = validate_rescues(rescues=texts["rescues"])
    session_id = validate_session_id(session_id=texts["session_id"])
    treasures = validate_treasures(treasures=texts["treasures"])

    # 綺麗に表示
    print(
        json.dumps(
            {
                "arrival_date": arrival_date,
                "defeated_bosses": defeated_bosses,
                "defeated_enemies": defeated_enemies,
                "game_result": game_result,
                "players": players,
                "rescues": rescues,
                "session_id": session_id,
                "treasures": treasures,
            },
            indent=4,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    image_path = sys.argv[1]
    crop_and_ocr(image_path=image_path)
