from pydantic import BaseModel, ConfigDict, Field
from .utils import PyObjectId


class Team(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    # league that the team participates in
    league: str
    # name of sport that team plays
    sport: str
