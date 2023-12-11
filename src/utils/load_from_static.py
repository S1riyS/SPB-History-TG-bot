from pathlib import Path

from aiogram.types import FSInputFile

from src.config import STATIC_DIR


def load_photo(file_path: Path) -> FSInputFile:
    """Loads photo from static folder and makes it compatible with aiogram"""
    absolute_path = STATIC_DIR / file_path
    return FSInputFile(absolute_path)
