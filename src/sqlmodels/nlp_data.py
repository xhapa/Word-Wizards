# Python
from typing import Optional, List, Tuple

# SQLModel
from sqlmodel import SQLModel, Field

class NLPData(SQLModel, table=True):
    nlp_data_id : Optional[int] | None = Field(default=None, primary_key=True)
    text : str = Field(index=True)
    tokens : List[str] = Field(index=True)
    word_count : int = Field(index=True)
    pos : List[str] = Field(index=True)
    entities : List[str] = Field(index=True)
    lemma : List[str] = Field(index=True)
    keywords : List[str] = Field(index=True)
    summarize : str = Field(index=True)

