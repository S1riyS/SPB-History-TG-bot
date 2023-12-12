from dataclasses import dataclass
from pathlib import Path


@dataclass
class RouteDetails:
    # Name of route
    name: str
    # Path to photo of full route
    map_photo_path: Path
    # Brief description that will be shown when user uses /start command
    brief_description: str
    # Full description that will be shown when user chooses specific route
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
