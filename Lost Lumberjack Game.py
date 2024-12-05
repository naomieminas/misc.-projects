#Lost Lumberjack Game

import random

# GAME DATA
SIZE = 10
TREE = "♣"
FLOOR = "."
PLAYER = "@"
GOAL = "X"


# blank maze
maze =[]
for r in range(SIZE):
    row = []
    for c in range(SIZE):
        row.append(TREE)
    maze.append(row)

# randomly place open spots
for i in range(SIZE*3):
    x = random.randint(1, SIZE-2)
    y = random.randint(1, SIZE-2)
    maze[y][x] = FLOOR

# place goal and player in corners
corners = [[1,1], [1,SIZE-2], [SIZE-2,1], [SIZE-2, SIZE-2]]
for c in corners:
    maze[c[1]][c[0]] = FLOOR
random.shuffle(corners)
play_pos = corners.pop()
goal_pos = corners.pop()

# GAME LOOP + USER INPUT
TURNS = 5
MAX_INPUT = 5
cur_turn = 1
while cur_turn <= TURNS and play_pos != goal_pos:
    # show the maze
    for r in range(SIZE):
        for c in range(SIZE):
            tile = maze[r][c]
            if play_pos == [c,r]:
                tile = PLAYER
            elif goal_pos == [c,r]:
                tile = GOAL
            print(tile,end="")
        print("")
    print("")

    # show # of turns left 
    print(f"Turns: {cur_turn} / {TURNS}")

    # start turn and take in player_input
    print("What would you like to do [u]p, [d]own, [l]eft, [r]ight, or [c]ut?")
    moves = input(f"Take an action (max {MAX_INPUT}): ")

    # process the user input:
    for action in moves[:MAX_INPUT]:
        np = play_pos.copy()

        # PROCESS CODE HERE #
        # cut action -- removes trees around a player
        if action == "c":
            maze[np[1]-1][np[0]] = FLOOR
            maze[np[1]+1][np[0]] = FLOOR
            maze[np[1]][np[0]-1] = FLOOR
            maze[np[1]][np[0]+1] = FLOOR

        # move in direction
        elif action == "u":
            np[1] -= 1
        elif action == "d":
            np[1] += 1
        elif action == "l":
            np[0] -= 1
        elif action == "r":
            np[0] += 1

        # keep within the maze
        np[0] = min(max(np[0],1), SIZE-2)
        np[1] = min(max(np[1],1), SIZE-2)

        # check if valid, then move
        if maze[np[1]][np[0]] == FLOOR:
            play_pos = np.copy()

    cur_turn += 1

# return end game status
if play_pos == goal_pos:
    print("**** You win! ****")
else:
    print("---- You lose ----")


