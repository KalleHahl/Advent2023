import re
from collections import deque

games = deque([])
game_wins = {}

with open('card_game.txt', 'r') as file:
    for line in file:
        game = line.strip()
        game = game.split(":")
        game_num = re.findall(r"\d+",game[0])
        game = game[1].split('|')
        game = deque([re.findall(r"\d+", game[0]),re.findall(r"\d+", game[1]) ])
        games.append(game)

def winning_games(games):
    points = 0

    for i,game in enumerate(games):
        game_points = 0
        wins = 0
        for num in game[1]:
            if num in game[0]:
                wins += 1
                if game_points == 0:
                    game_points = 1
                    continue
                game_points *= 2

        add_game_wins(i+1,wins)
        points += game_points

    return points



def add_game_wins(game_num, wins):
    if wins > 0:
        indices = deque([i for i in range(game_num+1,game_num+wins+1)])
        game_wins[game_num] = indices
        


def winning_games_copy_rules(game_wins, games):
    copies = {num: 1 for num in range(1,games+1)}

    scratchcards = deque([value for values_list in game_wins.values() for value in values_list])

    while scratchcards:
        game = scratchcards.popleft()
        try:
            scratchcards += game_wins[game]
        except KeyError:
            pass
        copies[game] += 1
    return sum(copies.values())


if __name__ == "__main__":
    print(
        f"Part 1: {winning_games(games)}"
    )
    print(
        f"Part 2: {winning_games_copy_rules(game_wins, len(games))}"
    )
