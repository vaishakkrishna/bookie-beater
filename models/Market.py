from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from .utils import PyObjectId


class Market(BaseModel):
    id: PyObjectId = Field(alias="_id")
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # name of the market (Moneyline, Over/Under x, etc.)
    market_name: str
    # id of the game associated with the market
    game_id: str
    # name of the lines (team1/team2 moneyline, player under/over, etc.)
    lines: List[str]
    # maps lines to American odds
    prematch_odds: Dict[str, int]