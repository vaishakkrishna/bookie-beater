# V4SportsSportOddsGet200ResponseInnerBookmakersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique slug (key) of the bookmaker | [optional] 
**title** | **str** | A formatted title of the bookmaker | [optional] 
**last_update** | **datetime** | A timestamp of when the bookmaker&#39;s odds were last read. Will be an integer if dateFormat&#x3D;unix, otherwise it will be a string | [optional] 
**markets** | [**List[V4SportsSportOddsGet200ResponseInnerBookmakersInnerMarketsInner]**](V4SportsSportOddsGet200ResponseInnerBookmakersInnerMarketsInner.md) | The included market depends on the specified &#39;markets&#39; GET param. NOTE Allow for the addition of new market types in future. | [optional] 
**link** | **str** | Link to the event on the bookmaker&#39;s website if available. This field is included when providing the query parameter includeLinks&#x3D;true | [optional] 
**sid** | **str** | The bookmaker&#39;s id of the event if available. This field is included when providing the query parameter includeSids&#x3D;true | [optional] 

## Example

```python
from openapi_client.models.v4_sports_sport_odds_get200_response_inner_bookmakers_inner import V4SportsSportOddsGet200ResponseInnerBookmakersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4SportsSportOddsGet200ResponseInnerBookmakersInner from a JSON string
v4_sports_sport_odds_get200_response_inner_bookmakers_inner_instance = V4SportsSportOddsGet200ResponseInnerBookmakersInner.from_json(json)
# print the JSON string representation of the object
print(V4SportsSportOddsGet200ResponseInnerBookmakersInner.to_json())

# convert the object into a dict
v4_sports_sport_odds_get200_response_inner_bookmakers_inner_dict = v4_sports_sport_odds_get200_response_inner_bookmakers_inner_instance.to_dict()
# create an instance of V4SportsSportOddsGet200ResponseInnerBookmakersInner from a dict
v4_sports_sport_odds_get200_response_inner_bookmakers_inner_from_dict = V4SportsSportOddsGet200ResponseInnerBookmakersInner.from_dict(v4_sports_sport_odds_get200_response_inner_bookmakers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


