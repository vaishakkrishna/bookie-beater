
from .SportsBook import Sportsbook
from datetime import datetime, timedelta
import time
from selenium import webdriver
from typing import Dict, List


class OddsPortal(Sportsbook):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.driver = webdriver.Chrome()

    def get_game_links_by_year(self, start_year: int = 2023) -> List[str]:
        self.driver.execute_script('alert("Focus window")')
        self.driver.switch_to.alert.accept()

        base_url = "https://www.oddsportal.com"
        sport = "basketball"
        country = "usa"
        league = "nba"
        start_year = 2022
        results_url = f"{base_url}/{sport}/{country}/{league}-{start_year}-{start_year + 1}/results/"
        a = "/html/body/div/div/div/div/main/div/div/div/div/a"
        links = set()
        for page in range(self.get_num_pages()):
            page = 1
            page_suffix = f"#/page/{page}"
            self.driver.get(results_url + page_suffix)
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(1)
            for elem in self.driver.find_elements(by="xpath", value=a):
                elem = elem.get_property("href")
                if elem and "results" not in elem and elem != results_url:
                    links.add(elem)
        return list(links)

    def get_num_pages(self) -> int:
        num_pages = 1
        for elem in self.driver.find_elements(by="xpath", value="//a[@class='pagination-link']"):
            try:
                page_num = max(int(elem.text), page_num)
            except:
                pass
        return num_pages

    def get_current_odds(self, game_id: str,
                         market_name: str, team_name: str) -> int: ...

    def get_prematch_odds(self, market_id: str, team_name: str) -> int: ...
    def get_games(self, sport: str, from_date: datetime = datetime.now(
    ), to_date: datetime = (datetime.now() + timedelta(days=3)), limit: int = 100): ...
    def get_markets(self, game_id: str) -> Dict[str, Dict]: ...
    def get_moneyline_odds(self, game_id: str, team_name: str) -> int: ...
