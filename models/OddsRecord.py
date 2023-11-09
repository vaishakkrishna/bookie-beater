from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from datetime import datetime
from .utils import PyObjectId


class OddsRecordMetadata(BaseModel):
    market_id: str
    line_name: str
    sportsbook_name: str


class OddsRecord(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # metadata
    metadata: OddsRecordMetadata
    timestamp: datetime
    price: int
