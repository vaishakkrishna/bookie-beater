from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List
from .utils import PyObjectId
from datetime import datetime


class Game(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    game_id: str
    game_name: str
    start_timestamp: datetime
    sport: str
    league: str
    teams: List[str]
