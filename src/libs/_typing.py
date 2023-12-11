from dataclasses import dataclass
from pathlib import Path


@dataclass
class RouteDetails:
    name: str
    map_photo_path: Path
    brief_description: str
    full_description: str


@dataclass
class CheckpointDetails:
    # Name of checkpoint (e.g. "Girl from the village" etc)
    name: str
    # Path to photo of checkpoint
    photo_path: Path
    # Comprehensive description of checkpoint
    description: str
    # Can be particular address or any other description of location
    location: str
