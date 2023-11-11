
from .SportsBook import Sportsbook
from datetime import datetime, timedelta


class OddsPortal(Sportsbook):
    def __init__(self, name: str = None):
        super().__init__(name)

    def get_basketball_game_ids(self, date: datetime):
        
    
    