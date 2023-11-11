from abc import ABC, abstractmethod
from models import OddsRecord
from typing import List

class BaseStrategy(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        # `Market`s that the strategy is tracking
        self.markets = []
        # list of sportsbook names to track
        self.sportsbooks = []

    @abstractmethod
    def process_odds_record(self, odds_record: OddsRecord):
        pass

    def process_odds_records(self, odds_records: List[OddsRecord]):
        for o in odds_records:    
            self.process_odds_record(o)
    