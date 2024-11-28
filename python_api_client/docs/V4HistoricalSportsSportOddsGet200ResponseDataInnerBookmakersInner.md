# V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique slug (key) of the bookmaker | [optional] 
**title** | **str** | A formatted title of the bookmaker | [optional] 
**last_update** | **datetime** | A timestamp of when the bookmaker&#39;s odds were last read. Will be an integer if dateFormat&#x3D;unix, otherwise it will be a string | [optional] 
**markets** | [**List[V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner]**](V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.md) | The included market depends on the specified &#39;markets&#39; GET param. NOTE Allow for the addition of new market types in future. | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner import V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner from a JSON string
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_instance = V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner.to_json())

# convert the object into a dict
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_dict = v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_instance.to_dict()
# create an instance of V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner from a dict
v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_from_dict = V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner.from_dict(v4_historical_sports_sport_odds_get200_response_data_inner_bookmakers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


