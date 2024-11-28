# openapi-client
To access the API, get a free API key from https://the-odds-api.com

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    api_instance = openapi_client.CurrentEventsApi(api_client)
    sport = 'americanfootball_nfl' # str | sport key for which to return events and odds. This is obtained from the /sports endpoint
    event_id = '50f069186530f68051f2a978745931b5' # str | Event ids can be found in the `id` field in the response of the `/events` endpoint (see `/v4/sports/{sports}/events`). If the event has expired (not receiving updates due to completion or cancellation), a HTTP 404 status code will be returned.
    api_key = 'abc123ABC456abc123ABC456abc123ABC456abc1' # str | Access key (40 characters). Get an API key at https://the-odds-api.com/#get-access
    regions = 'us' # str | Determines which bookmakers appear in the response. Multiple regions can be specified if comma delimited. Each region will count as 1 request against the usage quota for each market. Most use cases will only need to specify one region. See [the full list of bookmakers by region](https://the-odds-api.com/sports-odds-data/bookmaker-apis.html)
    markets = 'h2h' # str | The odds markets to return. Multiple markets can be specified if comma delimited. Defaults to h2h (head to head / moneyline). Outrights only avaialable for select sports. See [the full list of supported market keys](https://the-odds-api.com/sports-odds-data/betting-markets.html) (optional) (default to 'h2h')
    date_format = iso # str | Format of returned timestamps. Can be iso (ISO8601) or unix timestamp (seconds since epoch) (optional) (default to iso)
    odds_format = decimal # str | Format of returned odds (optional) (default to decimal)
    bookmakers = 'bookmakers_example' # str | Comma-separated list of bookmakers to be returned. If both `bookmakers` and `regions` are specified, `bookmakers` takes precendence. Bookmakers can be from any region. Every group of 10 bookmakers counts as 1 request. For example for a single market, specifying up to 10 bookmakers counts as 1 request. Specifying between 11 and 20 bookmakers counts as 2 requests (optional)
    include_links = False # bool | The response will include bookmaker links to events, markets, and betslips if available. (optional) (default to False)
    include_sids = False # bool | The response will include source ids (bookmaker ids) for events, markets, and outcomes if available. (optional) (default to False)
    include_bet_limits = False # bool | The response will include the bet limit of each betting option, mainly available for betting exchanges. (optional) (default to False)

    try:
        api_response = api_instance.v4_sports_sport_events_event_id_odds_get(sport, event_id, api_key, regions, markets=markets, date_format=date_format, odds_format=odds_format, bookmakers=bookmakers, include_links=include_links, include_sids=include_sids, include_bet_limits=include_bet_limits)
        print("The response of CurrentEventsApi->v4_sports_sport_events_event_id_odds_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentEventsApi->v4_sports_sport_events_event_id_odds_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.the-odds-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CurrentEventsApi* | [**v4_sports_sport_events_event_id_odds_get**](docs/CurrentEventsApi.md#v4_sports_sport_events_event_id_odds_get) | **GET** /v4/sports/{sport}/events/{eventId}/odds | 
*CurrentEventsApi* | [**v4_sports_sport_events_get**](docs/CurrentEventsApi.md#v4_sports_sport_events_get) | **GET** /v4/sports/{sport}/events | 
*CurrentEventsApi* | [**v4_sports_sport_odds_get**](docs/CurrentEventsApi.md#v4_sports_sport_odds_get) | **GET** /v4/sports/{sport}/odds | 
*CurrentEventsApi* | [**v4_sports_sport_scores_get**](docs/CurrentEventsApi.md#v4_sports_sport_scores_get) | **GET** /v4/sports/{sport}/scores | 
*HistoricalEventsApi* | [**v4_historical_sports_sport_events_event_id_odds_get**](docs/HistoricalEventsApi.md#v4_historical_sports_sport_events_event_id_odds_get) | **GET** /v4/historical/sports/{sport}/events/{eventId}/odds | 
*HistoricalEventsApi* | [**v4_historical_sports_sport_events_get**](docs/HistoricalEventsApi.md#v4_historical_sports_sport_events_get) | **GET** /v4/historical/sports/{sport}/events | 
*HistoricalEventsApi* | [**v4_historical_sports_sport_odds_get**](docs/HistoricalEventsApi.md#v4_historical_sports_sport_odds_get) | **GET** /v4/historical/sports/{sport}/odds | 
*SportsApi* | [**v4_sports_get**](docs/SportsApi.md#v4_sports_get) | **GET** /v4/sports | 


## Documentation For Models

 - [Outcome](docs/Outcome.md)
 - [ScoreModel](docs/ScoreModel.md)
 - [V4HistoricalSportsSportEventsEventIdOddsGet200Response](docs/V4HistoricalSportsSportEventsEventIdOddsGet200Response.md)
 - [V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData](docs/V4HistoricalSportsSportEventsEventIdOddsGet200ResponseData.md)
 - [V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner](docs/V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInner.md)
 - [V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner](docs/V4HistoricalSportsSportEventsEventIdOddsGet200ResponseDataBookmakersInnerMarketsInner.md)
 - [V4HistoricalSportsSportEventsGet200Response](docs/V4HistoricalSportsSportEventsGet200Response.md)
 - [V4HistoricalSportsSportOddsGet200Response](docs/V4HistoricalSportsSportOddsGet200Response.md)
 - [V4HistoricalSportsSportOddsGet200ResponseDataInner](docs/V4HistoricalSportsSportOddsGet200ResponseDataInner.md)
 - [V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner](docs/V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInner.md)
 - [V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner](docs/V4HistoricalSportsSportOddsGet200ResponseDataInnerBookmakersInnerMarketsInner.md)
 - [V4SportsGet200ResponseInner](docs/V4SportsGet200ResponseInner.md)
 - [V4SportsSportEventsEventIdOddsGet200Response](docs/V4SportsSportEventsEventIdOddsGet200Response.md)
 - [V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner](docs/V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInner.md)
 - [V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner](docs/V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner.md)
 - [V4SportsSportEventsGet200ResponseInner](docs/V4SportsSportEventsGet200ResponseInner.md)
 - [V4SportsSportOddsGet200ResponseInner](docs/V4SportsSportOddsGet200ResponseInner.md)
 - [V4SportsSportOddsGet200ResponseInnerBookmakersInner](docs/V4SportsSportOddsGet200ResponseInnerBookmakersInner.md)
 - [V4SportsSportOddsGet200ResponseInnerBookmakersInnerMarketsInner](docs/V4SportsSportOddsGet200ResponseInnerBookmakersInnerMarketsInner.md)
 - [V4SportsSportScoresGet200ResponseInner](docs/V4SportsSportScoresGet200ResponseInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author



