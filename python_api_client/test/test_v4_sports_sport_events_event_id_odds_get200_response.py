# coding: utf-8

"""
    The Odds API

    To access the API, get a free API key from https://the-odds-api.com

    The version of the OpenAPI document: 4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v4_sports_sport_events_event_id_odds_get200_response import V4SportsSportEventsEventIdOddsGet200Response

class TestV4SportsSportEventsEventIdOddsGet200Response(unittest.TestCase):
    """V4SportsSportEventsEventIdOddsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V4SportsSportEventsEventIdOddsGet200Response:
        """Test V4SportsSportEventsEventIdOddsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V4SportsSportEventsEventIdOddsGet200Response`
        """
        model = V4SportsSportEventsEventIdOddsGet200Response()
        if include_optional:
            return V4SportsSportEventsEventIdOddsGet200Response(
                id = 'e912304de2b2ce35b473ce2ecd3d1502',
                sport_key = 'americanfootball_nfl',
                sport_title = 'NFL',
                commence_time = '2023-10-11T23:10Z',
                home_team = 'Houston Texans',
                away_team = 'Kansas City Chiefs',
                bookmakers = [
                    openapi_client.models._v4_sports__sport__events__event_id__odds_get_200_response_bookmakers_inner._v4_sports__sport__events__eventId__odds_get_200_response_bookmakers_inner(
                        key = 'draftkings', 
                        title = 'DraftKings', 
                        markets = [
                            openapi_client.models._v4_sports__sport__events__event_id__odds_get_200_response_bookmakers_inner_markets_inner._v4_sports__sport__events__eventId__odds_get_200_response_bookmakers_inner_markets_inner(
                                key = 'alternate_spreads', 
                                last_update = '2023-10-10T12:10:29Z', 
                                outcomes = [{"name":"Houston Texans","price":5.08,"point":-23.0},{"name":"Houston Texans","price":4.82,"point":-22.5},{"name":"Houston Texans","price":4.66,"point":-22},{"name":"Kansas City Chiefs","price":1.15,"point":23.0},{"name":"Kansas City Chiefs","price":1.17,"point":22.5},{"name":"Kansas City Chiefs","price":1.17,"point":22.0}], 
                                link = '', 
                                sid = '', )
                            ], 
                        link = 'https://sportsbook.draftkings.com/event/chi-bears-%40-ind-colts/30568753', 
                        sid = '30568753', )
                    ]
            )
        else:
            return V4SportsSportEventsEventIdOddsGet200Response(
        )
        """

    def testV4SportsSportEventsEventIdOddsGet200Response(self):
        """Test V4SportsSportEventsEventIdOddsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()