from typing import List, Optional
from enum import Enum
from pydantic import BaseModel


class StatusEnum(str, Enum):
    """Перечисление для статуса питомца"""
    available = "available"
    pending = "pending"
    sold = "sold"


class Category(BaseModel):
    """Модель категории питомца"""
    id: int
    name: str


class Tag(BaseModel):
    """Модель тега питомца"""
    id: int
    name: str


class Pet(BaseModel):
    """Основная модель питомца"""
    id: int
    category: Optional[Category] = None
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]] = None
    status: Optional[StatusEnum] = None
