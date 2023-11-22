import uuid
import bson
import json
from models import OddsRecord, Sportsbook, Game
from datetime import datetime, timedelta
import time
from seleniumwire import webdriver
from typing import Dict, List
from collections import defaultdict
from seleniumwire.utils import decode


class OddsPortal(Sportsbook):
    def __init__(self, name: str = None, headless=True):
        super().__init__(name)

        # Create the webdriver object and pass the arguments
        options = webdriver.ChromeOptions()
        if headless:
            # Chrome will start in Headless mode
            options.add_argument('headless')

        # Ignores any certificate errors if there is any
        options.add_argument("--ignore-certificate-errors")

        self.driver = webdriver.Chrome(options=options)
        # game links by year
        self.game_links = defaultdict(list)

    def get_game_odds_from_game(self, game: Game) -> List[OddsRecord]:
        '''Gets moneyline odds for a game. Indexed by team name, then bookmaker name

        :param game_link: _description_
        :type game_link: str
        :return: _description_
        :rtype: Dict[str, int]
        '''
        game_link = "https://www.oddsportal.com" + game.metadata["url"]
        self.driver.get(game_link)

        t1_odds_xpath = '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[2]/div/div/p'
        t2_odds_xpath = '//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[3]/div/div/p'
        t1_name_xpath = '//*[@id="app"]/div/div[1]/div/main/div[2]/div[2]/div[1]/div[1]/div/div[1]/span'
        t2_name_xpath = '//*[@id="app"]/div/div[1]/div/main/div[2]/div[2]/div[1]/div[3]/div[1]/span'
        t1_name = self.driver.find_element(
            by="xpath", value=t1_name_xpath).text
        t2_name = self.driver.find_element(
            by="xpath", value=t2_name_xpath).text
        bookie_name_xpath = f'//*[@id="app"]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/a[2]/p'

        bookie_names = [t.text for t in self.driver.find_elements(
            by="xpath", value=bookie_name_xpath)]
        t1_odds = [t.text for t in self.driver.find_elements(
            by="xpath", value=t1_odds_xpath)]
        t2_odds = [t.text for t in self.driver.find_elements(
            by="xpath", value=t2_odds_xpath)]
        zipped_odds = zip(bookie_names, t1_odds, t2_odds)
        all_odds = []
        for bookie, t1_odd, t2_odd in zipped_odds:
            try:
                or1 = OddsRecord(
                    _id=bson.ObjectId(),
                    market_id="", line_name=f"{t1_name} to win",
                    sportsbook_name=bookie, timestamp=game.start_timestamp,
                    price=int(t1_odd))
                or2 = OddsRecord(
                    _id=bson.ObjectId(),
                    market_id="", line_name=f"{t2_name} to win",
                    sportsbook_name=bookie, timestamp=game.start_timestamp,
                    price=int(t2_odd))

            except:
                pass
        return {t1_name: t1_odds_dict, t2_name: t2_odds_dict}

    def get_games_by_year(self, start_year: int = 2022, start_page: int = 1):

        self.driver.execute_script('alert("Focus window")')
        self.driver.switch_to.alert.accept()
        base_url = "https://www.oddsportal.com"
        sport = "basketball"
        country = "usa"
        league = "nba"
        results_url = f"{base_url}/{sport}/{country}/{league}-{start_year}-{start_year + 1}/results/"
        next_page = True
        MAX_TRIES = 1000
        games = []
        self.driver.get(results_url + f"#/page/{start_page}")
        while next_page:
            # force site to load all games
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(1)
            # get response with games info
            try:
                req = [r for r in self.driver.requests if "tournament" in r.url][-1]
                body = decode(req.response.body, req.response.headers.get(
                    'Content-Encoding', 'identity'))
                response = json.loads(body.decode('utf-8'))
                new_games = self.parse_game_info_response(response)
                print(f"fetched {len(new_games)} new games")
                games.extend(new_games)
            except:
                print("games for page not found")

            # Load the next page
            next_page = self.load_next_results_page()

        return games

    def parse_game_info_response(self, response: dict) -> List[Game]:
        games_info = response['d']['rows']
        games = []
        for game_info in games_info:
            name = game_info["name"]
            t = game_info['date-start-timestamp']
            sport = game_info["sport-url-name"]
            league = "NBA"
            teams = [game_info["home-name"], game_info["away-name"]]
            scores = {game_info["home-name"]: int(game_info["homeResult"]),
                      game_info["away-name"]: int(game_info["awayResult"])}
            meta = {"url": game_info["url"]}
            game = Game(_id=bson.ObjectId(), name=name, start_timestamp=t, sport=sport,
                        league=league, teams=teams, scores=scores, metadata=meta)
            games.append(game)
        return games

    def load_next_results_page(self) -> bool:
        try:
            next_page = self.driver.find_element(
                by="link text", value="Next")
        except:
            return False
        next_page.click()
        return True

    def get_current_odds(self, game_id: str,
                         market_name: str, team_name: str) -> int: ...

    def get_prematch_odds(self, market_id: str, team_name: str) -> int: ...
    def get_games(self, sport: str, from_date: datetime = datetime.now(
    ), to_date: datetime = (datetime.now() + timedelta(days=3)), limit: int = 100): ...
    def get_markets(self, game_id: str) -> Dict[str, Dict]: ...
    def get_moneyline_odds(self, game_id: str, team_name: str) -> int: ...
