# V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique key for the odds market | [optional] 
**last_update** | **datetime** | A timestamp of when the markets&#39;s odds were last read. Will be an integer if dateFormat&#x3D;unix, otherwise it will be a string. | [optional] 
**outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner import V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner from a JSON string
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner_instance = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner.to_json())

# convert the object into a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner_dict = v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner_instance.to_dict()
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner from a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner_from_dict = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner.from_dict(v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_markets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


