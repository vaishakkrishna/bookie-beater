# Outcome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The outcome label. The value will depend on the market. For totals markets, this will be &#39;Over&#39; or &#39;Under&#39;. For team markets, it will be the name of the team or participant, or &#39;Draw&#39; | [optional] 
**price** | **float** | The odds of the outcome. The format is determined by the oddsFormat query param. The format is decimal by default. | [optional] 
**point** | **float** | The handicap or points of the outcome, only applicable to spreads and totals markets (this property will be missing for h2h and outrights markets) | [optional] 
**description** | **str** | This field is only relevant for certain markets. It contains more information about the outcome (for example, for player prop markets, it includes the player&#39;s name) | [optional] 
**link** | **str** | If available, link to the bookmaker&#39;s website and populate the betslip. This field is included when providing the query parameter includeLinks&#x3D;true | [optional] 
**sid** | **str** | The bookmaker&#39;s id for the bet selection, if available. This field is included when providing the query parameter includeSids&#x3D;true | [optional] 
**bet_limit** | **float** | The bookmaker&#39;s or exchange&#39;s monetary limit on the betting selection. The currency will depend on the bookmaker/exchange. This field is included when providing the query parameter includeBetLimits&#x3D;true, and is mainly populated for betting exchanges. | [optional] 

## Example

```python
from openapi_client.models.outcome import Outcome

# TODO update the JSON string below
json = "{}"
# create an instance of Outcome from a JSON string
outcome_instance = Outcome.from_json(json)
# print the JSON string representation of the object
print(Outcome.to_json())

# convert the object into a dict
outcome_dict = outcome_instance.to_dict()
# create an instance of Outcome from a dict
outcome_from_dict = Outcome.from_dict(outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


