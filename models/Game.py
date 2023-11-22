from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from .utils import PyObjectId
from datetime import datetime
from .Market import Market


class Game(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # name of the game
    name: str
    # when the game started
    start_timestamp: datetime
    # name of sport
    sport: str
    # name of league
    league: str
    # list of  `Team` names
    teams: List[str] = []
    # map of `Team` names
    scores: Dict[str, int] = {}
    # list of available markets for the game
    markets: List[Market] = []
    # metadata
    metadata: dict = {}
