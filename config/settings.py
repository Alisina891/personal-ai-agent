import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]

load_dotenv(PROJECT_ROOT / ".env")


APP_MODE = os.getenv("APP_MODE", "development")
DATABASE_PATH = os.getenv("DATABASE_PATH", "database/agent.db")
AI_PROVIDER = os.getenv("AI_PROVIDER", "")
PRIVACY_MODE = os.getenv("PRIVACY_MODE", "local")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"