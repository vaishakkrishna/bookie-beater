from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List
from .utils import PyObjectId
from datetime import datetime


class Game(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    start_timestamp: datetime
    sport: str
    league: str
    # list of  `Team` ids
    teams: List[str]
    # team id of winning team
    winner: str