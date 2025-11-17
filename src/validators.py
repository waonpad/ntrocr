from typing import Literal

from src.data import (
    incantations,
    sorceries,
    talismans,
    weapon_accessories,
    weapon_skills,
    weapon_type_map,
    weapon_types,
    weapons_data,
)


def validate_weapon_type(*, weapon_type: str) -> str:
    if weapon_type in weapon_types:
        return weapon_type

    msg = f"不正な武器種: {weapon_type}"
    raise ValueError(msg)


def validate_weapon_name(*, weapon_name: str, weapon_type: str) -> str:
    # weapon_type_mapの、バリューがweapon_typeのキーを取得
    weapon_type_key = next(key for key, value in weapon_type_map.items() if value == weapon_type)

    weapon_names_of_type = weapons_data[weapon_type_key]

    if weapon_name in weapon_names_of_type:
        return weapon_name

    # TODO: 派生していた場合の対応ベクトルで比較?
    msg = f"不正な武器名: {weapon_name} (武器種: {weapon_type})"
    raise ValueError(msg)


def validate_weapon_attack(*, weapon_attack: str) -> int:
    # 2~4桁の数値かどうか
    if weapon_attack.isdigit() and 2 <= len(weapon_attack) <= 4:  # noqa: PLR2004
        return int(weapon_attack)

    msg = f"不正な武器攻撃力: {weapon_attack}"
    raise ValueError(msg)


def validate_weapon_skill_name(*, weapon_skill_name: str) -> str:
    if weapon_skill_name in weapon_skills:
        return weapon_skill_name

    msg = f"不正な武器スキル名: {weapon_skill_name}"
    raise ValueError(msg)


def validate_weapon_accessory_name(*, weapon_accessory_name: str, index: int) -> str:
    # 2つ目以降の付帯効果名は空文字(無い)可能性もある
    if index >= 2 and weapon_accessory_name == "":  # noqa: PLR2004
        return weapon_accessory_name

    if weapon_accessory_name in weapon_accessories:
        return weapon_accessory_name

    msg = f"不正な付帯効果名: {weapon_accessory_name}"
    raise ValueError(msg)


def validate_talisman_name(*, talisman_name: str) -> str:
    if talisman_name in talismans:
        return talisman_name

    msg = f"不正なタリスマン名: {talisman_name}"
    raise ValueError(msg)


def validate_sorcery_name(*, sorcery_name: str) -> str:
    if sorcery_name in sorceries:
        return sorcery_name

    msg = f"不正な魔術名: {sorcery_name}"
    raise ValueError(msg)


def validate_incantation_name(*, incantation_name: str) -> str:
    if incantation_name in incantations:
        return incantation_name

    msg = f"不正な祈祷名: {incantation_name}"
    raise ValueError(msg)


def validate_accessory_value_sign(*, sign: str) -> Literal["+", "-", ""]:
    # 空文字の可能性もある
    if sign in ["+", "-", ""]:
        return sign  # type: ignore

    msg = f"不正な付帯効果の符号: {sign}"
    raise ValueError(msg)


def validate_accessory_value(*, value: str) -> tuple[str, str | None]:
    suffix = None

    # 空文字の可能性もある
    if value == "":
        return value, suffix

    # 末尾に%があれば取り除く
    if value.endswith("%"):
        value = value[:-1]
        suffix = "%"

    # 1~3桁の数値かどうか
    if value.isdigit() and 1 <= len(value) <= 3:  # noqa: PLR2004
        return value, suffix

    msg = f"不正な付帯効果の数値: {value}"
    raise ValueError(msg)


def validate_arrival_date(*, arrival_date: str) -> Literal["最初の日", "次の日", "最期の日"]:
    if arrival_date in ["最初の日", "次の日", "最期の日"]:
        return arrival_date  # type: ignore

    msg = f"不正な到達日: {arrival_date}"
    raise ValueError(msg)


def validate_player_name(*, name: str) -> str:
    # 空文字ではないかどうか
    if len(name) >= 1:
        return name

    msg = f"不正なプレイヤー名: {name}"
    raise ValueError(msg)


def validate_player_level(*, level: str) -> int:
    # 1~2桁の数値かどうか
    if level.isdigit() and 1 <= len(level) <= 2:  # noqa: PLR2004
        return int(level)

    msg = f"不正なプレイヤーレベル: {level}"
    raise ValueError(msg)


def validate_player_defeated_enemies(*, defeated_enemies: str) -> int:
    # 1~3桁の数値かどうか
    if defeated_enemies.isdigit() and 1 <= len(defeated_enemies) <= 3:  # noqa: PLR2004
        return int(defeated_enemies)

    msg = f"不正な撃破した敵数: {defeated_enemies}"
    raise ValueError(msg)


def validate_player_frasco(*, frasco: str) -> int:
    # 1~2桁の数値かどうか
    if frasco.isdigit() and 1 <= len(frasco) <= 2:  # noqa: PLR2004
        return int(frasco)

    msg = f"不正な聖杯瓶所持数: {frasco}"
    raise ValueError(msg)


def validate_player_runes(*, runes: str) -> int:
    # 1~8桁の数値かどうか
    if runes.isdigit() and 1 <= len(runes) <= 8:  # noqa: PLR2004
        return int(runes)

    msg = f"不正な獲得ルーン数: {runes}"
    raise ValueError(msg)


def validate_defeated_enemies(*, defeated_enemies: str) -> int:
    # 1~3桁の数値かどうか
    if defeated_enemies.isdigit() and 1 <= len(defeated_enemies) <= 3:  # noqa: PLR2004
        return int(defeated_enemies)

    msg = f"不正な撃破した敵数: {defeated_enemies}"
    raise ValueError(msg)


def validate_defeated_bosses(*, defeated_bosses: str) -> int:
    # 1~2桁の数値かどうか
    if defeated_bosses.isdigit() and 1 <= len(defeated_bosses) <= 2:  # noqa: PLR2004
        return int(defeated_bosses)

    msg = f"不正な撃破したボス数: {defeated_bosses}"
    raise ValueError(msg)


def validate_treasures(*, treasures: str) -> int:
    # 1~n桁の数値かどうか
    if treasures.isdigit() and len(treasures) >= 1:
        return int(treasures)

    msg = f"不正な発見した宝箱数: {treasures}"
    raise ValueError(msg)


def validate_rescues(*, rescues: str) -> int:
    # 1~n桁の数値かどうか
    if rescues.isdigit() and len(rescues) >= 1:
        return int(rescues)

    msg = f"不正な救助数: {rescues}"
    raise ValueError(msg)


def validate_session_id(*, session_id: str) -> str:
    # 5桁区切りで-が3つある数値かどうか
    parts = session_id.split("-")
    if len(parts) == 4 and all(part.isdigit() and len(part) == 5 for part in parts):  # noqa: PLR2004
        return session_id

    msg = f"不正なセッションID: {session_id}"
    raise ValueError(msg)
