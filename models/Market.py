from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List
from .utils import PyObjectId


class Market(BaseModel):
    id: PyObjectId = Field(alias="_id")
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # name of the market (Moneyline, Over/Under x, etc.)
    market_name: str
    # name of the lines (team1/team2 moneyline, player under/over, etc.)
    lines: List[str]
    # name of the winning line
    winning_line: str = None
