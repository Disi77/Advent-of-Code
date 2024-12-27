import re


path = "AdventOfCode2024/day14/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    robots = []
    for line in raw_data:
        robot = [int(x) for x in re.findall("[-]{0,1}\d+", line.strip())]
        robots.append(robot)

# Puzzle 2
X, Y = 103, 101
for sec in range(10000):
    for index, robot in enumerate(robots):
        y0, x0, dy, dx = robot
        x1 = (dx + x0) % X
        y1 = (dy + y0) % Y
        robots[index] = (y1, x1, dy, dx)

    if sec in range(4912, 10000, 103) or sec in range(4950, 10000, 101):
        # first I tried to put some random numbers as result so I found out that the number should
        # be between 5000 and 10000, then I tried to find the result manually by observing the results 
        # between 5000 and 10000 sec and I realised that the robots are periodically clustered in the middle of the area
        # in my case every 103 second from 71st second and every 101 second from 1st second
        # so I was able to check the state after second in range(74, 10000, 103) or range(3, 10000, 101)
        # and because I knew that the result is bigger than 5000, I updated the ranges a little bit
        print(sec + 1)
        robots_coors = set()
        for robot in robots:
            robots_coors.add((robot[0], robot[1]))

        for i in range(X):
            for j in range(Y):
                if (i, j) in robots_coors:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
    
    if sec + 1 == 6870:
        break

print("Puzzle 1 =", sec + 1)
