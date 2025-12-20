from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserProfile(BaseModel):
    """User profile containing about me text and CV content."""
    about_me: str = ""
    cv_text: str = ""
    cv_filename: Optional[str] = None
    updated_at: datetime = datetime.now()
