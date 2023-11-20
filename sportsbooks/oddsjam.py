from models.SportsBook import Sportsbook
from sports import BASKETBALL
from OddsJamClient import OddsJamClient
from datetime import datetime, timedelta
from typing import Dict, List
import requests
import json
from models.SportsBook import DRAFTKINGS, BOVADA
from models import Game, OddsRecord, OddsRecordMetadata


class OddsJam(Sportsbook):
    def __init__(self, api_key=None) -> None:
        super().__init__(name="oddsjam")
        self.api_key = api_key
        self.client = OddsJamClient(APIKEY=api_key)
        self.client.UseV2()
        self.api_base = "https://api-external.oddsjam.com/api/v2"

    def get_current_odds(self, game_id: str, market_name: str, team_id: str = None, sportsbooks: List[str] = [DRAFTKINGS]) -> Dict[str, int]:
        '''get the current in-play American odds value for a particular team
        in a market, given a list of sportsbooks

        :param game_id: universal game_id
        :type game_id: str
        :param market_name: universal market name
        :type market_name: str
        :param team_id: id of the team we want odds for
        :type team_id: str
        :return: map of sportsbook names to american odds
        :rtype: Dict[str, int]
        '''
        endpt = f"{self.api_base}/game-odds"
        params = {
            "key": self.api_key,
            "game_id": game_id,
            "market_name": market_name,
            "sportsbook": sportsbooks,
        }
        params.update({"team_id": team_id} if team_id else {})
        try:
            resp = requests.get(endpt, params=params).json()["data"][0]
        except:
            return []
        odds_data = resp["odds"]
        result = []
        for o in odds_data:
            result.append(OddsRecord(market_id=resp["id"], line_name=o["name"], sportsbook_name=o["sports_book_name"],
                                     imestamp=datetime.now(), price=o["price"]))
        return result

    def get_prematch_odds(self, market_id: str, team_name: str) -> int:
        '''gets the American odds value for a market 5 minutes before a game started.
        For use with historical odds.

        :param market_id: market_id in the sportsbook
        :type market_id: str
        :param team_name: name of the team/player/line we want odds for
        :type team_name: str
        '''
        pass

    def get_games(self, sport: str, from_date: datetime = datetime.now() + timedelta(hours=12),
                  to_date: datetime = (
            datetime.now() + timedelta(days=3)),
            league: str = None, limit: int = 100):
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
        endpt = f"{self.api_base}/schedules/list"
        params = {
            "key": self.api_key,
            "sport": sport,
            "start_date_before": to_date,
            "start_date_after": from_date,
            "page": 1
        }

        params.update({"league": league} if league else {})
        # returns json with keys "data", "page", "total_pages"
        result = []
        while (len(result) < limit) and (game_data := requests.get(endpt, params=params).json()["data"]):
            games = []
            for g in game_data:
                if sport == BASKETBALL:
                    teams = [g["home_team"], g["away_team"]]
                else:
                    raise NotImplemented(
                        "Games other than Basketball are not supported!")
                games.append(Game(id=g["game_id"],
                                  name=g["description"],
                                  start_timestamp=g["start_date"],
                                  sport=g["sport"],
                                  league=g["league"],
                                  teams=teams))
            result.extend(games)
            params["page"] += 1
        return result[-limit:]

    def get_markets(self, game_id: str, limit=3) -> Dict[str, Dict]:
        '''get all the market ids

        :param game_id: universal game id 
        :type game_id: str
        :return: get a list of all the markets of a game
        :rtype: Dict[str, Dict]
        '''
        # TODO: implement large numbers of markets, convert to market class
        return self.client.GetMarkets(game_id=game_id)

    def get_moneyline_odds(self, game_id: str, sportsbooks: List[str] = [DRAFTKINGS, BOVADA],
                           sport: str = None, league: str = None) -> Dict[str, int]:
        '''get moneyline odds of outcomes of a game
        TODO: add league/sport filtering
        :param game_id: _description_
        :type game_id: str
        :param team_name: _description_
        :type team_name: str
        :return: map of outcome (team name) to price
        :rtype: int
        '''
        return self.get_current_odds(game_id, market_name="Moneyline", sportsbooks=sportsbooks)

    def get_team_id(self, team_name: str, sport: str = None, league: str = None):
        '''gets a team's id given its name

        :param team_name: name of the team (Ex: "Harlem Globetrotters")
        :type team_name: str
        '''
        endpt = f"{self.api_base}/teams/"
        params = {
            "key": self.api_key,
            "team_name": team_name
        }
        params.update({"league": league} if league else {})
        params.update({"sport": sport} if sport else {})
        return requests.get(endpt, params=params).json()[
            "data"][0]["id"]

    def get_historical_odds(self, game_id: str, market_name: str, team_id: str = None, sportsbooks: List[str] = [DRAFTKINGS]) -> Dict[str, int]:
        '''get the historical American odds value for a particular team
        in a market, given a list of sportsbooks

        :param game_id: universal game_id
        :type game_id: str
        :param market_name: universal market name
        :type market_name: str
        :param team_id: id of the team we want odds for
        :type team_id: str
        :return: map of sportsbook names to american odds
        :rtype: Dict[str, int]
        '''
        endpt = f"{self.api_base}/historical-odds"
        params = {
            "key": self.api_key,
            "game_id": game_id,
            "market_name": market_name,
            "sportsbook": sportsbooks,
        }
        params.update({"team_id": team_id} if team_id else {})
        try:
            resp = requests.get(endpt, params=params).json()["data"][0]
        except:
            return []
        odds_data = resp["odds"]
        result = []
        for o in odds_data:
            meta = OddsRecordMetadata(
            )
            result.append(OddsRecord(market_id=resp["id"], line_name=o["name"], sportsbook_name=o["sports_book_name"],
                                     timestamp=datetime.now(), price=o["price"]))
        return result
