from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from datetime import datetime
from .utils import PyObjectId
import json


class OddsRecord(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # metadata
    # unique identifier of the market
    market_id: str
    # name of the market (e.g. team1 Moneyline)
    line_name: str
    timestamp: datetime
    # maps sportsbooks to prices
    prices: Dict[str, int]

    @staticmethod
    def odds_from_json(path: str):
        with open(path, "r") as f:
            odds_json = json.load(f)
        if type(odds_json) == list:
            return [OddsRecord(**o) for o in odds_json]
        else:
            return OddsRecord(**odds_json)
