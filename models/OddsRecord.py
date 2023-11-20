from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from datetime import datetime
from .utils import PyObjectId


class OddsRecordMetadata(BaseModel):
    # unique identifier of the market
    market_id: str
    # name of the market (e.g. team1 Moneyline)
    line_name: str
    # name of the sportsbook providing the line
    sportsbook_name: str


class OddsRecord(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # metadata
    metadata: OddsRecordMetadata
    timestamp: datetime
    price: int
