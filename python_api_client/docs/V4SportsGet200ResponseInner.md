# V4SportsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique slug for the sport. Use this as the \&quot;sport\&quot; param in /odds requests | [optional] 
**active** | **bool** | Indicates if the sport is in season | [optional] 
**group** | **str** | A broader grouping | [optional] 
**description** | **str** | A brief description of the sport. Subject to change (for example, if sponsors change) | [optional] 
**title** | **str** | A presentable title of the sport. Occassionally this value can change, for example if a league undergoes a name change or change in sponsorship. | [optional] 
**has_outrights** | **bool** | Indicates if the sport has outrights markets. | [optional] 

## Example

```python
from openapi_client.models.v4_sports_get200_response_inner import V4SportsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of V4SportsGet200ResponseInner from a JSON string
v4_sports_get200_response_inner_instance = V4SportsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(V4SportsGet200ResponseInner.to_json())

# convert the object into a dict
v4_sports_get200_response_inner_dict = v4_sports_get200_response_inner_instance.to_dict()
# create an instance of V4SportsGet200ResponseInner from a dict
v4_sports_get200_response_inner_from_dict = V4SportsGet200ResponseInner.from_dict(v4_sports_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


