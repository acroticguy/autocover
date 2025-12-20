import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
PROFILES_DIR = DATA_DIR / "profiles"

# Ensure directories exist
PROFILES_DIR.mkdir(parents=True, exist_ok=True)

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model settings
GEMINI_MODEL = "gemini-flash-latest"

def validate_api_key() -> bool:
    """Check if the Gemini API key is configured."""
    return GEMINI_API_KEY is not None and len(GEMINI_API_KEY) > 0
