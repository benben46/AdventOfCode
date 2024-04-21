# Day 2: Cube Conundrum

allowed = {"red": 12,
           "green": 13,
           "blue": 14}

# [12 green, 9 blue, 13 red]
def isValid(set_score):
    for element in set_score:
        color = element.split(" ")[1].strip()
        num = int(element.split(" ")[0]).strip()
        if (allowed[color.lower()] < num):
            return False
    return True
        
possible_games = []
with open("input.txt", "r") as f:
    for line in f:
        game_index = 0
        # Remove the "Game #: " part
        games = line.split(":", 1)[1]
        sets = games.split(";")
        stripped_sets = [x.strip() for x in sets]
        for set in stripped_sets:
            set_stats = set.split(",")
            if isValid(set_stats):
                possible_games.append(game_index)
        game_index += 1

print("Sum of Game #'s that qualify as possible games:", sum(possible_games))
