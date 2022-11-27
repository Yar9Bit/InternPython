from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()


# pprint(game_stamps)


def get_score(game_stamps, offset: int) -> tuple:
    offset_low = 0
    offset_middle = 0
    offset_high = len(game_stamps) - 1
    score = game_stamps[offset_middle]
    home = score["score"]["home"]
    away = score["score"]["away"]
    while offset_low <= offset_high:
        offset_middle = (offset_low + offset_high) // 2
        score = game_stamps[offset_middle]
        if score["offset"] == offset:
            return home, away
        else:
            if offset < score["offset"]:
                offset_high = offset_middle - 1
            elif offset > score["offset"]:
                offset_low = offset_middle + 1
    return home, away


s = get_score(generate_game(), 115)
pprint(s)
