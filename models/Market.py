from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from .utils import PyObjectId


class Market(BaseModel):
    id: PyObjectId = Field(alias="_id")
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # internal ID of the market
    market_id: str
    # name of the market (Moneyline, Over/Under x, etc.)
    market_name: str
    # name of the line (team, player, etc.)
    lines: List[str]
    # maps lines to American odds
    prematch_odds: Dict[str, int]
    # mapping of sportsbook names to their market_ids
    sb_market_ids: Dict[str, str]
