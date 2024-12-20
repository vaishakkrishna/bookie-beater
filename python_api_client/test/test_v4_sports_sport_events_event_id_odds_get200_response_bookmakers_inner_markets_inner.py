# coding: utf-8

"""
    The Odds API

    To access the API, get a free API key from https://the-odds-api.com

    The version of the OpenAPI document: 4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v4_sports_sport_events_event_id_odds_get200_response_bookmakers_inner_markets_inner import V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner

class TestV4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner(unittest.TestCase):
    """V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner:
        """Test V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner`
        """
        model = V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner()
        if include_optional:
            return V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner(
                key = 'alternate_spreads',
                last_update = '2023-10-10T12:10:29Z',
                outcomes = [{"name":"Houston Texans","price":5.08,"point":-23.0},{"name":"Houston Texans","price":4.82,"point":-22.5},{"name":"Houston Texans","price":4.66,"point":-22},{"name":"Kansas City Chiefs","price":1.15,"point":23.0},{"name":"Kansas City Chiefs","price":1.17,"point":22.5},{"name":"Kansas City Chiefs","price":1.17,"point":22.0}],
                link = '',
                sid = ''
            )
        else:
            return V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner(
        )
        """

    def testV4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner(self):
        """Test V4SportsSportEventsEventIdOddsGet200ResponseBookmakersInnerMarketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
