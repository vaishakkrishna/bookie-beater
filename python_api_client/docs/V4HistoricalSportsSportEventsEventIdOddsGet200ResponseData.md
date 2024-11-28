# V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique 32 character identifier for the event. | [optional] 
**sport_key** | **str** | A unique slug for the sport. Use this as the \&quot;sport\&quot; param in /odds requests | [optional] 
**sport_title** | **str** | A presentable title of the sport. Occassionally this value can change, for example if a league undergoes a name change or change in sponsorship. | [optional] 
**commence_time** | **datetime** | The match start time (ISO 8601 formatted). This will be unix timestamp integer if the dateFormat query param is set to dateFormat&#x3D;unix. | [optional] 
**home_team** | **str** | The home team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events. | [optional] 
**away_team** | **str** | The away team. If home/away is not applicable for the sport (such as MMA and Tennis), it will be one of the participants. Null for outrights (futures) events. | [optional] 
**bookmakers** | [**List[V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner]**](V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_events_event_id_odds_get200_response_data import V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData from a JSON string
v4_historical_sports_sport_events_event_id_odds_get200_response_data_instance = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData.to_json())

# convert the object into a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_dict = v4_historical_sports_sport_events_event_id_odds_get200_response_data_instance.to_dict()
# create an instance of V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData from a dict
v4_historical_sports_sport_events_event_id_odds_get200_response_data_from_dict = V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData.from_dict(v4_historical_sports_sport_events_event_id_odds_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


