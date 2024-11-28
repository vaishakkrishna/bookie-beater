# openapi_client.SportsApi

All URIs are relative to *https://api.the-odds-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_sports_get**](SportsApi.md#v4_sports_get) | **GET** /v4/sports | 


# **v4_sports_get**
> List[V4SportsGet200ResponseInner] v4_sports_get(api_key, all=all)



A successful response includes a list of available sports and tournaments

### Example


```python
import openapi_client
from openapi_client.models.v4_sports_get200_response_inner import V4SportsGet200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.the-odds-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.the-odds-api.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SportsApi(api_client)
    api_key = 'abcdefg1234567890' # str | Get an API key at https://the-odds-api.com/#get-access
    all = true # bool | When excluded, only recently updated (in-season) sports appear. Include this paramter to see all available sports (optional)

    try:
        api_response = api_instance.v4_sports_get(api_key, all=all)
        print("The response of SportsApi->v4_sports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SportsApi->v4_sports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Get an API key at https://the-odds-api.com/#get-access | 
 **all** | **bool**| When excluded, only recently updated (in-season) sports appear. Include this paramter to see all available sports | [optional] 

### Return type

[**List[V4SportsGet200ResponseInner]**](V4SportsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of available sports. Use the sport \&quot;key\&quot; in the /odds request |  * x-requests-remaining - The number of requests remaining until the quota resets <br>  * x-requests-used - The number of requests used since the last quota reset <br>  * x-requests-last - The usage cost of the last API call <br>  |
**401** | Unauthenticated or unauthorized. The API key might be missing or invalid (unauthenticated), or it might at its usage limit (unauthorized). The repsonse body will contain more info |  -  |
**422** | One or more of the query params are invalid. The repsonse body will contain more info |  -  |
**429** | The request was throttled because requests are being sent too frequently |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

