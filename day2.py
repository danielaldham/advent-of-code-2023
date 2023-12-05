file = 'inputs/input_day2.txt'

"""
day 1 plan
split line to get plan
split line to get each set
split line to each cube group
"""

with open(file, 'r') as f:
    sum = 0
    for line in f:
        line = line.split(':')
        game = line[0]
        game_num = game.split()[1]
        game_num = int(game_num)     
        sets = line[1].split(';')
        possible = True
        for set in sets:
            set = set.split(',')
            for group in set:
                if 'blue' in group:
                    num = group.split()[0]
                    if int(num) > 14:
                        possible = False
                if 'red' in group:
                    num = group.split()[0]
                    if int(num) > 12:
                        possible = False
                if 'green' in group:
                    num = group.split()[0]
                    if int(num) > 13:
                        possible = False
        if possible == True:
            #print(game_num)
            sum += game_num
        # print(sum)
    print(sum)