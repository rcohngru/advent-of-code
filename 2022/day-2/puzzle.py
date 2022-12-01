
def main():

    hand_decoder = {
        "A":"rock",
        "X":"rock",
        "B":"paper",
        "Y":"paper",
        "C":"scissor",
        "Z":"scissor"
    }

    outcome_decoder = {
        "X":"loss",
        "Y":"draw",
        "Z":"win"
    }

    games = ingest_file()

    game_scores = []
    for g in games:
        outcome = compare_hands(hand_decoder[g[0]], hand_decoder[g[1]])
        score = score_game(hand_decoder[g[1]], outcome)
        game_scores.append(score)

    total_score = sum(game_scores)
    print("-------- Part 1 --------")
    print(total_score)

    game_scores = []
    for g in games:
        player = player_hand(hand_decoder[g[0]], outcome_decoder[g[1]])
        score = score_game(player, outcome_decoder[g[1]])
        game_scores.append(score)

    total_score = sum(game_scores)
    print("-------- Part 2 --------")
    print(total_score)

# -------- Part 1 --------
def ingest_file():
    with open("puzzle_data.txt", "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]
    lines = [l.split(" ") for l in lines]
    return lines

def compare_hands(opponent, player):
    outcome = None

    if opponent == player:
        outcome = "draw"
    elif (
        (opponent == "rock" and player == "paper") or
        (opponent == "paper" and player == "scissor") or
        (opponent == "scissor" and player == "rock")
    ):
        outcome = "win"
    else:
        outcome = "loss"

    return outcome

def score_game(player, outcome):
    # Scoring rules:
    # Shape:
    # Rock -> 1
    # Paper -> 2
    # Scissors -> 3
    #
    # Outcome:
    # Loss -> 0
    # Draw -> 3
    # Win -> 6

    shape_scores = {
        "rock": 1,
        "paper": 2,
        "scissor": 3
    }

    outcome_scores = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

    game_score = 0

    game_score += outcome_scores[outcome] + shape_scores[player]

    return game_score

# --------- Part 2 ---------

def player_hand(opponent, expected_outcome):

    hand_defeater = {
        "rock":"paper",
        "paper":"scissor",
        "scissor":"rock"
    }

    if expected_outcome == "draw":
        return opponent
    elif expected_outcome == "win":
        return hand_defeater[opponent]
    else:
        h = hand_defeater.items()
        for k, v in h:
            if v == opponent:
                return k

if __name__ == "__main__":
    main()