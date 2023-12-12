import re
games = []

MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('cube_game.txt', 'r') as file:
    for line in file:
        games.append(line.strip())

def possibles(games):
    possible_matches = 0
    for game in games:
        correcto = True
        match_number = re.search(r'Game (\d+)', game).group(1)
        matches = re.findall(r'(\d+) (green|red|blue)', game)
        for result in matches:
            if int(result[0]) > MAX[result[1]]:
                correcto = False
        if correcto:
            possible_matches += int(match_number)
    return possible_matches


def other(games):
    pow = 0
    for game in games:
        min_r = 0
        min_g = 0
        min_b = 0
        matches = re.findall(r'(\d+) (green|red|blue)', game)
        for result in matches:
            if result[1] == 'red':
                if min_r < int(result[0]):
                    min_r = int(result[0])
            elif result[1] == 'green':
                if min_g < int(result[0]):
                    min_g = int(result[0])
            else:
                if min_b < int(result[0]):
                    min_b = int(result[0])
        pow += min_r*min_g*min_b
    return pow

        
print(possibles(games))
print(other(games))