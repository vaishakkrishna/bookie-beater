from typing import Dict
from datetime import datetime, timedelta
from models import Market


class Sportsbook:
    def __init__(self, name: str = None):
        self.name = name

    def get_current_odds(self, game_id: str, market_name: str, team_name: str) -> int:
        '''get the current in-play American odds value for a particular team
        in a market.

        :param game_id: universal game_id
        :type game_id: str
        :param market_name: market_name in the sportsbook
        :type market_name: str
        :param team_name: name of the team/player/line we want odds for
        :type team_name: str
        :return: _description_
        :rtype: int
        '''
        pass

    def get_prematch_odds(self, market_id: str, team_name: str) -> int:
        '''gets the American odds value for a market 5 minutes before a game started.
        For use with historical odds.

        :param market_id: market_id in the sportsbook
        :type market_id: str
        :param team_name: name of the team/player/line we want odds for
        :type team_name: str
        '''
        pass

    def get_games(self, sport: str, from_date: datetime = datetime.now(), to_date: datetime = (datetime.now() + timedelta(days=3)), limit: int = 100):
        '''Get a list of previous/upcoming game information (if supported) for a particular sport

        :param sport: sport name
        :type sport: str
        :param from_date: _description_, defaults to datetime.now()
        :type from_date: datetime, optional
        :param to_date: _description_, defaults to (datetime.now()+datetime.timedelta(days=3))
        :type to_date: datetime, optional
        :param limit: max number of markets to return, defaults to 100
        :type limit: int, optional
        '''
        pass

    def get_markets(self, game_id: str) -> Dict[str, Dict]:
        '''get all the market ids

        :param game_id: _description_
        :type game_id: str
        :return: _description_
        :rtype: Dict[str, Dict]
        '''
        pass

    def get_moneyline_odds(self, game_id: str, team_name: str) -> int:
        '''get moneyline odds of a team right now.

        :param game_id: _description_
        :type game_id: str
        :param team_name: _description_
        :type team_name: str
        :return: _description_
        :rtype: int
        '''
        pass


TEN_BET = "10bet"
TRIPLE_EIGHT_SPORT = "888sport"
BARSTOOL = "Barstool"
BET365 = "bet365"
BET99 = "BET99"
BET_AMERICA = "Bet America"
BETFAIR = "Betfair"
BETMGM = "BetMGM"
BETUS = "BetUS"
BETVICTOR = "BetVictor"
BORGATA = "Borgata"
BOVADA = "Bovada"
CAESARS = "Caesars"
CIRCA_SPORTS = "Circa Sports"
CLUTCHBET = "ClutchBet"
DRAFTKINGS = "DraftKings"
FANDUEL = "FanDuel"
FLIFF = "Fliff"
FOUR_WINDS = "Four Winds"
FOX_BET = "FOX Bet"
GOLDEN_NUGGET = "Golden Nugget"
HARD_ROCK = "Hard Rock"
NITROGEN = "Nitrogen"
PARTYPOKER = "partypoker"
POWERPLAY = "PowerPlay"
PRIZEPICKS = "PrizePicks"
PROLINE = "Proline"
PROPHET_EXCHANGE = "Prophet Exchange"
SKY_BET = "Sky Bet"
SPORTSBET = "Sportsbet"
SPORTSBETTING_DOT_COM = "SportsBetting.com"
SUGARHOUSE = "SugarHouse"
TWINSPIRES = "TwinSpires"
UNIBET = "Unibet"
WILLIAM_HILL = "William Hill"
WYNNBET = "WynnBET"

ALL_SPORTSBOOKS = [TEN_BET, TRIPLE_EIGHT_SPORT, BARSTOOL, BET365, BET99, BET_AMERICA, BETFAIR, BETMGM, BETUS, BETVICTOR, BORGATA, BOVADA, CAESARS, CIRCA_SPORTS, CLUTCHBET, DRAFTKINGS, FANDUEL, FLIFF, FOUR_WINDS,
                   FOX_BET, GOLDEN_NUGGET, HARD_ROCK, NITROGEN, PARTYPOKER, POWERPLAY, PRIZEPICKS, PROLINE, PROPHET_EXCHANGE, SKY_BET, SPORTSBET, SPORTSBETTING_DOT_COM, SUGARHOUSE, TWINSPIRES, UNIBET, WILLIAM_HILL, WYNNBET]
