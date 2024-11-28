# openapi_client.HistoricalEventsApi

All URIs are relative to *https://api.the-odds-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_historical_sports_sport_events_event_id_odds_get**](HistoricalEventsApi.md#v4_historical_sports_sport_events_event_id_odds_get) | **GET** /v4/historical/sports/{sport}/events/{eventId}/odds | 
[**v4_historical_sports_sport_events_get**](HistoricalEventsApi.md#v4_historical_sports_sport_events_get) | **GET** /v4/historical/sports/{sport}/events | 
[**v4_historical_sports_sport_odds_get**](HistoricalEventsApi.md#v4_historical_sports_sport_odds_get) | **GET** /v4/historical/sports/{sport}/odds | 


# **v4_historical_sports_sport_events_event_id_odds_get**
> V4HistoricalSportsSportEventsEventIdOddsGet200Response v4_historical_sports_sport_events_event_id_odds_get(sport, event_id, api_key, regions, var_date, markets=markets, date_format=date_format, odds_format=odds_format, bookmakers=bookmakers)



Returns bookmaker odds for a single event as they appeared at the specified timestamp (date parameter). Accepts any available market keys using the `markets` parameter. Use this endpoint to access historical odds from any available markets for an event. For historical odds of the most popular featured markets, use the `/v4/historical/sports/{sport}/odds` endpoint. See the [full list of market keys here](https://the-odds-api.com/sports-odds-data/betting-markets.html)

### Example


```python
import openapi_client
from openapi_client.models.v4_historical_sports_sport_events_event_id_odds_get200_response import V4HistoricalSportsSportEventsEventIdOddsGet200Response
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
    api_instance = openapi_client.HistoricalEventsApi(api_client)
    sport = 'americanfootball_nfl' # str | sport key for which to return events and odds. This is obtained from the /sports endpoint
    event_id = '50f069186530f68051f2a978745931b5' # str | Event ids can be found in the `id` field in the response of the historical events endpoint (see `/v4/historical/sports/{sports}/events`). If the event had expired at the specified timestamp (not receiving updates due to completion or cancellation), a HTTP 404 status code will be returned.
    api_key = 'abc123ABC456abc123ABC456abc123ABC456abc1' # str | Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access
    regions = 'us' # str | Determines which bookmakers appear in the response. Multiple regions can be specified if comma delimited. Most use cases will only need to specify one region. See [the full list of bookmakers by region](https://the-odds-api.com/sports-odds-data/bookmaker-apis.html)
    var_date = '2023-10-10T12:15:00Z' # str | The timestamp of the data snapshot to be returned, specified in ISO8601 format. The API will return the closest snapshot equal to or earlier than the provided date parameter
    markets = 'h2h' # str | The odds markets to return. Multiple markets can be specified if comma delimited. Defaults to h2h (head to head / moneyline). Outrights only avaialable for select sports. See [the full list of supported market keys](https://the-odds-api.com/sports-odds-data/betting-markets.html) (optional) (default to 'h2h')
    date_format = iso # str | Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) (optional) (default to iso)
    odds_format = decimal # str | Format of returned odds (optional) (default to decimal)
    bookmakers = 'bookmakers_example' # str | Comma-separated list of bookmakers to be returned. If both `bookmakers` and `regions` are specified, `bookmakers` takes precendence. Bookmakers can be from any region. Every group of 10 bookmakers counts as 1 request. For example for a single market, specifying up to 10 bookmakers counts as 1 request. Specifying between 11 and 20 bookmakers counts as 2 requests (optional)

    try:
        api_response = api_instance.v4_historical_sports_sport_events_event_id_odds_get(sport, event_id, api_key, regions, var_date, markets=markets, date_format=date_format, odds_format=odds_format, bookmakers=bookmakers)
        print("The response of HistoricalEventsApi->v4_historical_sports_sport_events_event_id_odds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoricalEventsApi->v4_historical_sports_sport_events_event_id_odds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport** | **str**| sport key for which to return events and odds. This is obtained from the /sports endpoint | 
 **event_id** | **str**| Event ids can be found in the &#x60;id&#x60; field in the response of the historical events endpoint (see &#x60;/v4/historical/sports/{sports}/events&#x60;). If the event had expired at the specified timestamp (not receiving updates due to completion or cancellation), a HTTP 404 status code will be returned. | 
 **api_key** | **str**| Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access | 
 **regions** | **str**| Determines which bookmakers appear in the response. Multiple regions can be specified if comma delimited. Most use cases will only need to specify one region. See [the full list of bookmakers by region](https://the-odds-api.com/sports-odds-data/bookmaker-apis.html) | 
 **var_date** | **str**| The timestamp of the data snapshot to be returned, specified in ISO8601 format. The API will return the closest snapshot equal to or earlier than the provided date parameter | 
 **markets** | **str**| The odds markets to return. Multiple markets can be specified if comma delimited. Defaults to h2h (head to head / moneyline). Outrights only avaialable for select sports. See [the full list of supported market keys](https://the-odds-api.com/sports-odds-data/betting-markets.html) | [optional] [default to &#39;h2h&#39;]
 **date_format** | **str**| Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) | [optional] [default to iso]
 **odds_format** | **str**| Format of returned odds | [optional] [default to decimal]
 **bookmakers** | **str**| Comma-separated list of bookmakers to be returned. If both &#x60;bookmakers&#x60; and &#x60;regions&#x60; are specified, &#x60;bookmakers&#x60; takes precendence. Bookmakers can be from any region. Every group of 10 bookmakers counts as 1 request. For example for a single market, specifying up to 10 bookmakers counts as 1 request. Specifying between 11 and 20 bookmakers counts as 2 requests | [optional] 

### Return type

[**V4HistoricalSportsSportEventsEventIdOddsGet200Response**](V4HistoricalSportsSportEventsEventIdOddsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The event with the eventId specified in the path parameter. Includes odds from bookmakers in the specified region for the specified markets |  * x-requests-remaining - The number of requests remaining until the quota resets <br>  * x-requests-used - The number of requests used since the last quota reset <br>  * x-requests-last - The usage cost of the last API call <br>  |
**401** | Unauthenticated or unauthorized. The API key might be missing or invalid (unauthenticated), or it might at its usage limit (unauthorized). The repsonse body will contain more info |  -  |
**404** | The event id is invalid or the event has expired |  -  |
**422** | One or more of the query params are invalid. The repsonse body will contain more info |  -  |
**429** | Requests are being sent too frequently - the request was throttled |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_historical_sports_sport_events_get**
> V4HistoricalSportsSportEventsGet200Response v4_historical_sports_sport_events_get(sport, api_key, var_date, date_format=date_format, event_ids=event_ids, commence_time_from=commence_time_from, commence_time_to=commence_time_to)



Returns a list of events for the specified sport as they appeared at the specified timestamp (date parameter). Odds are not included in the response

### Example


```python
import openapi_client
from openapi_client.models.v4_historical_sports_sport_events_get200_response import V4HistoricalSportsSportEventsGet200Response
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
    api_instance = openapi_client.HistoricalEventsApi(api_client)
    sport = 'americanfootball_nfl' # str | sport key for which to return events and odds. This is obtained from the /sports endpoint
    api_key = 'abc123ABC456abc123ABC456abc123ABC456abc1' # str | Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access
    var_date = '2023-10-10T12:15:00Z' # str | The timestamp of the data snapshot to be returned, specified in ISO8601 format. The API will return the closest snapshot equal to or earlier than the provided date parameter
    date_format = iso # str | Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) (optional) (default to iso)
    event_ids = 'event_ids_example' # str | Comma-separated event ids. Filters the response to only return events for the specified ids, provided those events have not expired (optional)
    commence_time_from = '2023-09-09T00:00:00Z' # str | Filters the response to show events that commence on and after this parameter. Values are in ISO8601 format (optional)
    commence_time_to = '2023-09-09T00:00:00Z' # str | Filters the response to show events that commence on and before this parameter. Values are in ISO8601 format (optional)

    try:
        api_response = api_instance.v4_historical_sports_sport_events_get(sport, api_key, var_date, date_format=date_format, event_ids=event_ids, commence_time_from=commence_time_from, commence_time_to=commence_time_to)
        print("The response of HistoricalEventsApi->v4_historical_sports_sport_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoricalEventsApi->v4_historical_sports_sport_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport** | **str**| sport key for which to return events and odds. This is obtained from the /sports endpoint | 
 **api_key** | **str**| Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access | 
 **var_date** | **str**| The timestamp of the data snapshot to be returned, specified in ISO8601 format. The API will return the closest snapshot equal to or earlier than the provided date parameter | 
 **date_format** | **str**| Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) | [optional] [default to iso]
 **event_ids** | **str**| Comma-separated event ids. Filters the response to only return events for the specified ids, provided those events have not expired | [optional] 
 **commence_time_from** | **str**| Filters the response to show events that commence on and after this parameter. Values are in ISO8601 format | [optional] 
 **commence_time_to** | **str**| Filters the response to show events that commence on and before this parameter. Values are in ISO8601 format | [optional] 

### Return type

[**V4HistoricalSportsSportEventsGet200Response**](V4HistoricalSportsSportEventsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of live and upcoming events for the specified sport, as they appeared at the specified timestamp (date parameter), excluding odds |  * x-requests-remaining - The number of requests remaining until the quota resets <br>  * x-requests-used - The number of requests used since the last quota reset <br>  * x-requests-last - The usage cost of the last API call <br>  |
**401** | Unauthenticated or unauthorized. The API key might be missing or invalid (unauthenticated), or it might at its usage limit (unauthorized). The repsonse body will contain more info |  -  |
**422** | One or more of the query params are invalid. The repsonse body will contain more info |  -  |
**429** | Requests are being sent too frequently - the request was throttled |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_historical_sports_sport_odds_get**
> V4HistoricalSportsSportOddsGet200Response v4_historical_sports_sport_odds_get(sport, api_key, regions, var_date, markets=markets, date_format=date_format, odds_format=odds_format, event_ids=event_ids, bookmakers=bookmakers)



Returns list of live and upcoming events at a point in time for a given sport, including bookmaker odds for the specified region and markets. This endpoint will only return featured markets (moneyline, match winner, 1x2, head-to-head, spreads, totals, over/under, outrights etc.), using the market keys `h2h`, `spreads`, `totals`. This endpoint was previously `/v4/sports/{sport}/odds-history`, which has been deprecated.

### Example


```python
import openapi_client
from openapi_client.models.v4_historical_sports_sport_odds_get200_response import V4HistoricalSportsSportOddsGet200Response
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
    api_instance = openapi_client.HistoricalEventsApi(api_client)
    sport = 'americanfootball_nfl' # str | sport key for which to return events and odds. This is obtained from the /sports endpoint
    api_key = 'abc123ABC456abc123ABC456abc123ABC456abc1' # str | Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access
    regions = 'us' # str | Determines which bookmakers appear in the response. Multiple regions can be specified if comma delimited. Most use cases will only need to specify one region. For a list of bookmakers by region, see https://the-odds-api.com/sports-odds-data/bookmaker-apis.html
    var_date = '2023-10-10T12:15:00Z' # str | The timestamp of the data snapshot to be returned, specified in ISO8601 format. The historical odds API will return the closest snapshot equal to or earlier than the provided date parameter
    markets = h2h # str | The odds market to return. Multiple markets can be specified if comma delimited. Defaults to h2h (head to head / moneyline). Outrights are only avaialable for select sports, such as golf. (optional) (default to h2h)
    date_format = iso # str | Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) (optional) (default to iso)
    odds_format = decimal # str | Format of returned odds (optional) (default to decimal)
    event_ids = 'event_ids_example' # str | Comma-separated event ids. Filters the response to only return events for the specified ids, provided those events have not expired (optional)
    bookmakers = 'bookmakers_example' # str | Comma-separated list of bookmakers to be returned. If both `bookmakers` and `regions` are specified, `bookmakers` takes precendence. Bookmakers can be from any region. Every group of 10 bookmakers counts as 1 request. For example for a single market, specifying up to 10 bookmakers counts as 1 request. Specifying between 11 and 20 bookmakers counts as 2 requests (optional)

    try:
        api_response = api_instance.v4_historical_sports_sport_odds_get(sport, api_key, regions, var_date, markets=markets, date_format=date_format, odds_format=odds_format, event_ids=event_ids, bookmakers=bookmakers)
        print("The response of HistoricalEventsApi->v4_historical_sports_sport_odds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoricalEventsApi->v4_historical_sports_sport_odds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport** | **str**| sport key for which to return events and odds. This is obtained from the /sports endpoint | 
 **api_key** | **str**| Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access | 
 **regions** | **str**| Determines which bookmakers appear in the response. Multiple regions can be specified if comma delimited. Most use cases will only need to specify one region. For a list of bookmakers by region, see https://the-odds-api.com/sports-odds-data/bookmaker-apis.html | 
 **var_date** | **str**| The timestamp of the data snapshot to be returned, specified in ISO8601 format. The historical odds API will return the closest snapshot equal to or earlier than the provided date parameter | 
 **markets** | **str**| The odds market to return. Multiple markets can be specified if comma delimited. Defaults to h2h (head to head / moneyline). Outrights are only avaialable for select sports, such as golf. | [optional] [default to h2h]
 **date_format** | **str**| Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) | [optional] [default to iso]
 **odds_format** | **str**| Format of returned odds | [optional] [default to decimal]
 **event_ids** | **str**| Comma-separated event ids. Filters the response to only return events for the specified ids, provided those events have not expired | [optional] 
 **bookmakers** | **str**| Comma-separated list of bookmakers to be returned. If both &#x60;bookmakers&#x60; and &#x60;regions&#x60; are specified, &#x60;bookmakers&#x60; takes precendence. Bookmakers can be from any region. Every group of 10 bookmakers counts as 1 request. For example for a single market, specifying up to 10 bookmakers counts as 1 request. Specifying between 11 and 20 bookmakers counts as 2 requests | [optional] 

### Return type

[**V4HistoricalSportsSportOddsGet200Response**](V4HistoricalSportsSportOddsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of live and upcoming events and bookmaker odds for the specified sport, from the historical snapshot closest to the specified date |  * x-requests-remaining - The number of requests remaining until the quota resets <br>  * x-requests-used - The number of requests used since the last quota reset <br>  * x-requests-last - The usage cost of the last API call <br>  |
**401** | Unauthenticated or unauthorized. The API key might be missing or invalid (unauthenticated), or it might at its usage limit (unauthorized). The repsonse body will contain more info |  -  |
**422** | One or more of the query params are invalid. The repsonse body will contain more info |  -  |
**429** | Requests are being sent too frequently - the request was throttled |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

