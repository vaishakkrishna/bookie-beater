# V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique slug (key) of the bookmaker | [optional] 
**title** | **str** | A formatted title of the bookmaker | [optional] 
**markets** | [**List[V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner]**](V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner.md) | The included market depends on the specified &#39;markets&#39; GET param. | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner import V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner from a JSON string
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_instance = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner.to_json())

# convert the object into a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_dict = v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_instance.to_dict()
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner from a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_from_dict = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner.from_dict(v4_historical_sports_sport_events_event_id_odds_get200_response_data_bookmakers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


