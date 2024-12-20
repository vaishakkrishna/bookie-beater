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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner import V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner
from typing import Optional, Set
from typing_extensions import Self

class V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner(BaseModel):
    """
    V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner
    """ # noqa: E501
    key: Optional[StrictStr] = Field(default=None, description="A unique slug (key) of the bookmaker")
    title: Optional[StrictStr] = Field(default=None, description="A formatted title of the bookmaker")
    last_update: Optional[datetime] = Field(default=None, description="A timestamp of when the bookmaker's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string")
    markets: Optional[List[V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner]] = Field(default=None, description="The included market depends on the specified 'markets' GET param. NOTE Allow for the addition of new market types in future.")
    __properties: ClassVar[List[str]] = ["key", "title", "last_update", "markets"]

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
        """Create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in markets (list)
        _items = []
        if self.markets:
            for _item_markets in self.markets:
                if _item_markets:
                    _items.append(_item_markets.to_dict())
            _dict['markets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "title": obj.get("title"),
            "last_update": obj.get("last_update"),
            "markets": [V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.from_dict(_item) for _item in obj["markets"]] if obj.get("markets") is not None else None
        })
        return _obj


