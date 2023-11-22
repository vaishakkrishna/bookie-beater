from pydantic import BaseModel
from pydantic import ConfigDict, Field
from typing import List, Dict
from .utils import PyObjectId
from datetime import datetime
from .Market import Market
import json


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

    @staticmethod
    def games_from_json(path: str):
        '''load a game or list of games
        from json

        :param path: path to json file of games
        :type path: str
        '''
        with open(path, "r") as f:
            games_json = json.load(f)
        if type(games_json) == list:
            return [Game(**g) for g in games_json]
        else:
            return Game(**games_json)
