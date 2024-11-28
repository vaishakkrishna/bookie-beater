# V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the odds market | [optional] 
**last_update** | **datetime** | A timestamp of when the markets&#39;s odds were last read. Will be an integer if dateFormat&#x3D;unix, otherwise it will be a string. To check recency of odds, we recommend using this field instead of the \&quot;last_update\&quot; field at the bookmaker level. | [optional] 
**outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner import V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner from a JSON string
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner_instance = V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.to_json())

# convert the object into a dict
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner_dict = v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner_instance.to_dict()
# create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner from a dict
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner_from_dict = V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.from_dict(v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_markets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


