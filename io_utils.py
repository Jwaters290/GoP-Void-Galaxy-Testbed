# gop_void_testbed/io_utils.py

import json
from pathlib import Path
from typing import List
from .data_models import VoidGalaxy

def load_void_galaxies_from_json(path: str | Path) -> List[VoidGalaxy]:
    path = Path(path)
    with path.open("r") as f:
        raw = json.load(f)
    galaxies = []
    for entry in raw:
        galaxies.append(VoidGalaxy(**entry))
    return galaxies
