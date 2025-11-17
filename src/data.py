import json
from pathlib import Path

weapons_data = json.loads(Path("/workspace/data/weapons.json").read_text(encoding="utf-8"))

# type_mapのキーバリューの値だけ取り出してリストにする
weapon_type_map: dict[str, str] = weapons_data["_type_map"]
weapon_types: list[str] = list(weapons_data["_type_map"].values())

weapon_skills: list[str] = json.loads(Path("/workspace/data/weapon_skills.json").read_text(encoding="utf-8"))[
    "weapon_skills"
]
weapon_accessories: list[str] = json.loads(Path("/workspace/data/weapon_accessories.json").read_text(encoding="utf-8"))[
    "weapon_accessories"
]
talismans: list[str] = json.loads(Path("/workspace/data/talismans.json").read_text(encoding="utf-8"))["talismans"]
sorceries: list[str] = json.loads(Path("/workspace/data/sorceries.json").read_text(encoding="utf-8"))["sorceries"]
incantations: list[str] = json.loads(Path("/workspace/data/incantations.json").read_text(encoding="utf-8"))[
    "incantations"
]
