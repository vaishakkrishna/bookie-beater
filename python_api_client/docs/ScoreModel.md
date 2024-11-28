# ScoreModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The participant name | [optional] 
**score** | **str** | The most recent score for the participant | [optional] 

## Example

```python
from openapi_client.models.score_model import ScoreModel

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreModel from a JSON string
score_model_instance = ScoreModel.from_json(json)
# print the JSON string representation of the object
print(ScoreModel.to_json())

# convert the object into a dict
score_model_dict = score_model_instance.to_dict()
# create an instance of ScoreModel from a dict
score_model_from_dict = ScoreModel.from_dict(score_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


