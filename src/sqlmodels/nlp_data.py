# Python
from typing import Optional, List, Tuple

# SQLAlchemy
from sqlalchemy import Column, JSON

# SQLModel
from sqlmodel import SQLModel, Field, select

class NLPData(SQLModel, table=True):
    nlp_data_id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field(index=True)
    lang: str = Field(index=True)
    tokens: List[str] = Field(sa_column=Column(JSON))
    word_count: int = Field(index=True)
    pos: List[Tuple[str, str]] = Field(sa_column=Column(JSON))
    entities: List[Tuple[str, str]] = Field(sa_column=Column(JSON))
    lemma: List[str] = Field(sa_column=Column(JSON))
    keywords: List[str] = Field(sa_column=Column(JSON))
    summary: str = Field(index=True)

    class Config:
        schema_extra = {
            "example": {
            }
        }