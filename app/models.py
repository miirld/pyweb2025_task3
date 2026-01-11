from typing import Optional
from pydantic import BaseModel, Field


class Term(BaseModel):
    title: str = Field(..., min_length=1)
    definition: str = Field(..., min_length=1)
    source_link: Optional[str] = Field(None, min_length=1)


class TermUpdate(BaseModel):
    definition: Optional[str] = Field(None, min_length=1)
    source_link: Optional[str] = Field(None, min_length=1)
