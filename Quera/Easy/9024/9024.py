# https://quera.org/problemset/9024

from enum import Enum

from typing import List


class Winner(Enum):
    PLAYER_1 = 'karakter e komaki_1'
    PLAYER_2 = 'karakter e komaki_2'
    DRAW = 'mosavi'


n = int(input())
list_of_nums = list(map(int, input().split()))


class Situation:
    def __init__(self, winner: Winner, distance: int, selector: Winner):
        self.winner = winner
        self.distance = distance
        self.selector = selector


list_of_p1_score: List[int] = [0] * n
list_of_p2_score: List[int] = [0] * n
list_of_situations: List[Situation] = [None] * n

table = [list_of_nums, list_of_p1_score, list_of_p2_score, list_of_situations]


def give_better_situation_for_p1(situation1: Situation, situation2: Situation):
    # player_1 is winner in both
    if (situation1.winner is Winner.PLAYER_1) and (situation2.winner is Winner.PLAYER_1):
        return situation1 if (situation1.distance > situation2.distance) else situation2

    # when player 2 is winner in both
    elif (situation1.winner is Winner.PLAYER_2) and (situation2.winner is Winner.PLAYER_2):
        return situation1 if (situation1.distance < situation2.distance) else situation2

    # else if there is one player_1 winner, returns it
    elif (situation1.winner is Winner.PLAYER_1) or (situation2.winner is Winner.PLAYER_1):
        return situation1 if (situation1.winner is Winner.PLAYER_1) else situation2

    # else there might be a Draw and a player_2, so draw should be returned
    else:
        return situation1 if (situation1.winner is Winner.DRAW) else situation2
    pass


def give_situation_by_scores(score_player1: int, score_player2: int, selector: Winner):
    distance = abs(score_player1 - score_player2)
    if score_player1 > score_player2:
        return Situation(winner=Winner.PLAYER_1, distance=distance, selector=selector)
    if score_player1 < score_player2:
        return Situation(winner=Winner.PLAYER_2, distance=distance, selector=selector)
    else:
        return Situation(winner=Winner.DRAW, distance=distance, selector=selector)


def does_player1_selected_in_previous_turn(pre_turn_index: int):
    return True if list_of_situations[pre_turn_index].selector is Winner.PLAYER_1 else False


def is_current_situation_better(current_sit, pre_situation=None):
    if pre_situation is None:
        return True
    elif current_sit == give_better_situation_for_p1(current_situation, pre_situation):
        return True
    else:
        return False


def set_scores_and_situation(turn_index: int, p1_score: int, p2_score: int, situation: Situation):
    list_of_p1_score[turn_index] = p1_score
    list_of_p2_score[turn_index] = p2_score
    list_of_situations[turn_index] = situation


turn = 0

# initial turn, player one have to select first number
list_of_p1_score[turn] = list_of_nums[turn]

list_of_situations[turn] = (give_situation_by_scores
                            (list_of_p1_score[turn],
                             list_of_p2_score[turn],
                             Winner.PLAYER_1)
                            )

for turn in range(1, n):

    best_situation = None
    this_turn_selector = None
    current_score_for_p1 = 0
    current_score_for_p2 = 0

    for pre_turn in range(turn):
        if does_player1_selected_in_previous_turn(pre_turn):

            #  --- scenario for player_1, that player_1 selects the number
            this_turn_selector = Winner.PLAYER_1

            # ignore the previous turn score for player_1 and select this number
            current_score_for_p1 = (list_of_p1_score[pre_turn] - list_of_nums[pre_turn]) + list_of_nums[turn]
            # the score for player_2 won't change
            current_score_for_p2 = list_of_p2_score[pre_turn]

            current_situation = give_situation_by_scores(current_score_for_p1, current_score_for_p2, this_turn_selector)
            if is_current_situation_better(current_situation, best_situation):
                set_scores_and_situation(turn, current_score_for_p1, current_score_for_p2, current_situation)
                best_situation = current_situation

            # --- scenario for player_2, that player_2 selects the number
            this_turn_selector = Winner.PLAYER_2
            # the score for p1 won't change
            current_score_for_p1 = list_of_p1_score[pre_turn]
            # as the previous turn selector is player_1 so the score for player 2 is:
            current_score_for_p2 = list_of_p2_score[pre_turn] + list_of_nums[turn]

            current_situation = give_situation_by_scores(current_score_for_p1, current_score_for_p2, this_turn_selector)
            if is_current_situation_better(current_situation, best_situation):
                set_scores_and_situation(turn, current_score_for_p1, current_score_for_p2, current_situation)
                best_situation = current_situation

        else:
            #  --- scenario for player_1, that player_1 selects the number
            this_turn_selector = Winner.PLAYER_1

            current_score_for_p1 = list_of_p1_score[pre_turn] + list_of_nums[turn]
            current_score_for_p2 = list_of_p2_score[pre_turn]

            current_situation = give_situation_by_scores(current_score_for_p1, current_score_for_p2, this_turn_selector)
            if is_current_situation_better(current_situation, best_situation):
                set_scores_and_situation(turn, current_score_for_p1, current_score_for_p2, current_situation)
                best_situation = current_situation

            # --- scenario for player_2, that player_2 selects the number
            this_turn_selector = Winner.PLAYER_2

            current_score_for_p1 = list_of_p1_score[pre_turn]
            current_score_for_p2 = (list_of_p2_score[pre_turn] - list_of_nums[pre_turn]) + list_of_nums[turn]

            current_situation = give_situation_by_scores(current_score_for_p1, current_score_for_p2, this_turn_selector)
            if is_current_situation_better(current_situation, best_situation):
                set_scores_and_situation(turn, current_score_for_p1, current_score_for_p2, current_situation)
                best_situation = current_situation
    pass

# print the result
last_situation = list_of_situations[n - 1]

if last_situation.winner is Winner.DRAW:
    print(last_situation.winner.value)
else:
    print(f'{last_situation.winner.value}: {last_situation.distance}')

