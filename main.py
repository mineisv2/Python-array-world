width = 27
height = 15

world = []

def buildWorld():
    for i in range(height):
        world.append([])
        for j in range(width):
            world[i].append(0)

def printWorld():
    for i in range(len(world)):
        print(world[i])

buildWorld()

player = [1, 1]

world[player[0]][player[1]] = 1

while True:
    printWorld()
    world = []
    buildWorld()
    move = input(" ")
    if move == "d":
        player[1] += 1
        world[player[0]][player[1]] = 1
    elif move == "a":
        player[1] -= 1
        world[player[0]][player[1]] = 1
    elif move == "s":
        player[0] += 1
        world[player[0]][player[1]] = 1
    elif move == "w":
        player[0] -= 1
        world[player[0]][player[1]] = 1
    else:
        break
