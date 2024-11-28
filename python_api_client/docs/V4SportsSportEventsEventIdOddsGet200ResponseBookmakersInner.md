# V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique slug (key) of the bookmaker | [optional] 
**title** | **str** | A formatted title of the bookmaker | [optional] 
**markets** | [**List[V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner]**](V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner.md) | The included market depends on the specified &#39;markets&#39; GET param. | [optional] 
**link** | **str** | Link to the event on the bookmaker&#39;s website if available. This field is included when providing the query parameter includeLinks&#x3D;true | [optional] 
**sid** | **str** | The bookmaker&#39;s id of the event if available. This field is included when providing the query parameter includeSids&#x3D;true | [optional] 

## Example

```python
from openapi_client.models.v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner import V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner from a JSON string
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_instance = V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner.from_json(json)
# print the JSON string representation of the object
print(V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner.to_json())

# convert the object into a dict
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_dict = v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_instance.to_dict()
# create an instance of V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner from a dict
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_from_dict = V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner.from_dict(v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


