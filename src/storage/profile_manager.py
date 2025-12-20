import json
from pathlib import Path
from datetime import datetime
from typing import Optional

from src.config import PROFILES_DIR
from src.storage.models import UserProfile


DEFAULT_PROFILE_PATH = PROFILES_DIR / "default.json"


def save_profile(profile: UserProfile) -> None:
    """Save user profile to disk."""
    profile.updated_at = datetime.now()
    with open(DEFAULT_PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile.model_dump(mode="json"), f, indent=2, default=str)


def load_profile() -> UserProfile:
    """Load user profile from disk, or return empty profile if none exists."""
    if DEFAULT_PROFILE_PATH.exists():
        try:
            with open(DEFAULT_PROFILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return UserProfile(**data)
        except (json.JSONDecodeError, ValueError):
            pass
    return UserProfile()


def profile_exists() -> bool:
    """Check if a saved profile exists."""
    return DEFAULT_PROFILE_PATH.exists()
