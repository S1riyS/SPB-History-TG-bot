import os
from pathlib import Path

from dotenv import load_dotenv

# Directories of project
SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
STATIC_DIR = ROOT_DIR / "static"

# Environment variables
load_dotenv(ROOT_DIR / ".env")
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN", "")
