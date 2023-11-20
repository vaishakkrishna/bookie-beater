
from models.SportsBook import Sportsbook
from datetime import datetime, timedelta
import time
from selenium import webdriver
from typing import Dict, List
from collections import defaultdict


class OddsPortal(Sportsbook):
    def __init__(self, name: str = None):
        super().__init__(name)
        self.driver = webdriver.Chrome()
        # game links by year
        self.game_links = defaultdict(list)

    def get_game_links_by_year(self, start_year: int = 2023, start_page=1) -> List[str]:
        self.driver.execute_script('alert("Focus window")')
        self.driver.switch_to.alert.accept()

        base_url = "https://www.oddsportal.com"
        sport = "basketball"
        country = "usa"
        league = "nba"
        results_url = f"{base_url}/{sport}/{country}/{league}-{start_year}-{start_year + 1}/results/"
        a = "/html/body/div/div/div/div/main/div/div/div/div/a"
        links = set()
        self.driver.get(results_url + f"#/page/{start_page}")
        next_page = True
        MAX_TRIES = 1000
        for _ in range(MAX_TRIES):
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(1)
            before = len(links)
            for elem in self.driver.find_elements(by="xpath", value=a):
                elem = elem.get_property("href")
                if elem and "results" not in elem and elem != results_url:
                    links.add(elem)
            after = len(links)
            print(f"Fetched {after-before} game links from page")
            try:
                next_page = self.driver.find_element(
                    by="link text", value="Next")
            except Exception as e:
                break
            next_page.click()
        self.game_links[start_year].extend(links)
        return list(links)

    def get_num_pages(self) -> int:
        '''gets number of pages to load. MAKE SURE INITIAL RESULTS PAGE IS LOADED 

        :param link: _description_
        :type link: str
        :return: _description_
        :rtype: int
        '''
        num_pages = 1
        page_xpath = '//*[@id="app"]/div/div[1]/div/main/div[2]/div[4]/div[5]/div/a'
        for elem in self.driver.find_elements(by="xpath", value=page_xpath):
            try:
                num_pages = max(int(elem.text), num_pages)
            except:
                pass
        return num_pages

    def get_game_odds_from_link(self, game_link: str) -> Dict[str, Dict[str, int]]:
        '''Gets moneyline odds for a game. Indexed by team name, then bookmaker name

        :param game_link: _description_
        :type game_link: str
        :return: _description_
        :rtype: Dict[str, int]
        '''
        self.driver.get(game_link)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 5000);")
        time.sleep(2)

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
        t1_odds_dict, t2_odds_dict = {}, {}
        for bookie, t1_odd, t2_odd in zipped_odds:
            try:
                t1_odds_dict[bookie] = int(t1_odd)
                t2_odds_dict[bookie] = int(t2_odd)
            except:
                pass
        return {t1_name: t1_odds_dict, t2_name: t2_odds_dict}

    def get_game_results_by_year(self, start_year: str) -> str:
        ...

    def get_current_odds(self, game_id: str,
                         market_name: str, team_name: str) -> int: ...

    def get_prematch_odds(self, market_id: str, team_name: str) -> int: ...
    def get_games(self, sport: str, from_date: datetime = datetime.now(
    ), to_date: datetime = (datetime.now() + timedelta(days=3)), limit: int = 100): ...
    def get_markets(self, game_id: str) -> Dict[str, Dict]: ...
    def get_moneyline_odds(self, game_id: str, team_name: str) -> int: ...
