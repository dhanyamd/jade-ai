from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    api_key: str
    model: str = "gpt-4o-mini"
    base_url: Optional[str] = None
