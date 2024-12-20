# coding: utf-8

"""
    The Odds API

    To access the API, get a free API key from https://the-odds-api.com

    The version of the OpenAPI document: 4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.score_model import ScoreModel
from typing import Optional, Set
from typing_extensions import Self

class V4SportsSportScoresGet200ResponseInner(BaseModel):
    """
    V4SportsSportScoresGet200ResponseInner
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="A unique 32 character identifier for the event.")
    sport_key: Optional[StrictStr] = Field(default=None, description="A unique slug for the sport. Use this as the \"sport\" param in /odds requests")
    sport_title: Optional[StrictStr] = Field(default=None, description="A presentable title of the sport. Occassionally this value can change, for example if a league undergoes a name change or change in sponsorship.")
    commence_time: Optional[datetime] = Field(default=None, description="The match start time (ISO 8601 formatted). This will be unix timestamp integer if the dateFormat query param is set to dateFormat=unix.")
    completed: Optional[StrictBool] = Field(default=None, description="true if the event has finished, otherwise false")
    home_team: Optional[StrictStr] = Field(default=None, description="The home team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.")
    away_team: Optional[StrictStr] = Field(default=None, description="The away team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events.")
    scores: Optional[List[ScoreModel]] = Field(default=None, description="A list of teams and their scores. List will be empty if event has not started.")
    last_update: Optional[StrictStr] = Field(default=None, description="ISO8601 datetime of when the scores were last updated. Will be null if event has not started")
    __properties: ClassVar[List[str]] = ["id", "sport_key", "sport_title", "commence_time", "completed", "home_team", "away_team", "scores", "last_update"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V4SportsSportScoresGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in scores (list)
        _items = []
        if self.scores:
            for _item_scores in self.scores:
                if _item_scores:
                    _items.append(_item_scores.to_dict())
            _dict['scores'] = _items
        # set to None if home_team (nullable) is None
        # and model_fields_set contains the field
        if self.home_team is None and "home_team" in self.model_fields_set:
            _dict['home_team'] = None

        # set to None if away_team (nullable) is None
        # and model_fields_set contains the field
        if self.away_team is None and "away_team" in self.model_fields_set:
            _dict['away_team'] = None

        # set to None if last_update (nullable) is None
        # and model_fields_set contains the field
        if self.last_update is None and "last_update" in self.model_fields_set:
            _dict['last_update'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V4SportsSportScoresGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sport_key": obj.get("sport_key"),
            "sport_title": obj.get("sport_title"),
            "commence_time": obj.get("commence_time"),
            "completed": obj.get("completed"),
            "home_team": obj.get("home_team"),
            "away_team": obj.get("away_team"),
            "scores": [ScoreModel.from_dict(_item) for _item in obj["scores"]] if obj.get("scores") is not None else None,
            "last_update": obj.get("last_update")
        })
        return _obj


