from typing import List


def american_odds_to_probability(odds):
    """
    Convert American sports betting odds to implied probabilities.

    :param odds: The American odds. Positive for underdog, negative for favorite.
    :return: The implied probability as a percentage.
    """
    if odds > 0:
        # For underdog (positive odds)
        probability = 100 / (odds + 100)
    else:
        # For favorite (negative odds)
        probability = -odds / (-odds + 100)

    return probability



