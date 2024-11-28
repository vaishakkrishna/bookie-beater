# V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique key for the odds market | [optional] 
**last_update** | **datetime** | A timestamp of when the markets&#39;s odds were last read. Will be an integer if dateFormat&#x3D;unix, otherwise it will be a string. | [optional] 
**outcomes** | [**List[Outcome]**](Outcome.md) |  | [optional] 
**link** | **str** | Link to the market on the bookmaker&#39;s website if applicable. This field is included when providing the query parameter includeLinks&#x3D;true | [optional] 
**sid** | **str** | The bookmaker&#39;s id of the market if available. This field is included when providing the query parameter includeSids&#x3D;true | [optional] 

## Example

```python
from openapi_client.models.v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner import V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner from a JSON string
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner_instance = V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner.from_json(json)
# print the JSON string representation of the object
print(V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner.to_json())

# convert the object into a dict
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner_dict = v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner_instance.to_dict()
# create an instance of V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner from a dict
v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner_from_dict = V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner.from_dict(v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


