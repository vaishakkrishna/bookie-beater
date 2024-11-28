# V4HistoricalSportsSportOddsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | The timestamp of the snapshot. This will be the closest available timestamp equal to or earlier than the provided date parameter. | [optional] 
**previous_timestamp** | **str** | The preceding available timestamp. This can be used as the date parameter in a new request to move back in time. | [optional] 
**next_timestamp** | **str** | The next available timestamp. This can be used as the date parameter in a new request to move forward in time. | [optional] 
**data** | [**List[V4HistoricalSportsSportOddsGet200ResponseDataInner]**](V4HistoricalSportsSportOddsGet200ResponseDataInner.md) | A list of live and upcoming events at the time of the snapshot | [optional] 

## Example

```python
from openapi_client.models.v4_historical_sports_sport_odds_get200_response import V4HistoricalSportsSportOddsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V4HistoricalSportsSportOddsGet200Response from a JSON string
v4_historical_sports_sport_odds_get200_response_instance = V4HistoricalSportsSportOddsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V4HistoricalSportsSportOddsGet200Response.to_json())

# convert the object into a dict
v4_historical_sports_sport_odds_get200_response_dict = v4_historical_sports_sport_odds_get200_response_instance.to_dict()
# create an instance of V4HistoricalSportsSportOddsGet200Response from a dict
v4_historical_sports_sport_odds_get200_response_from_dict = V4HistoricalSportsSportOddsGet200Response.from_dict(v4_historical_sports_sport_odds_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


