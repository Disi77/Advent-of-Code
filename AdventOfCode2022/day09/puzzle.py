from pathlib import Path


def puzzle_solution(instructions, snake, history):
    for i in instructions:
        direction, steps = i.split()
        steps = int(steps)
        for _ in range(steps):
            x0, y0 = snake[0]
            if direction == "R":
                x0 += 1
            elif direction == "L":
                x0 -= 1
            elif direction == "D":
                y0 -= 1
            elif direction == "U":
                y0 += 1
            snake[0] = x0, y0

            for index, (x1, y1) in enumerate(snake):
                if (x0, y0) == (x1, y1) or abs(y0 - y1) <= 1 and abs(x0 - x1) <= 1:
                    pass
                elif x0 == x1 and abs(y0 - y1) == 2:
                    y1 = (y1 + y0) // 2
                elif y0 == y1 and abs(x0 - x1) == 2:
                    x1 = (x1 + x0) // 2
                else:
                    koef_x = 1 if (x1 - x0) > 0 else -1
                    koef_y = 1 if (y1 - y0) > 0 else -1
                    x1, y1 = x1 - koef_x, y1 - koef_y
                snake[index] = (x1, y1)
                x0, y0 = x1, y1
                history.add(snake[-1])


here = Path(__file__).parent
instructions = Path(here / "input.txt").read_text().split("\n")


snake = [(0, 0), (0, 0)]
history = set()
puzzle_solution(instructions, snake, history)
print("Puzzle 1 =", len(history))


snake = [(0, 0) for _ in range(10)]
history = set()
puzzle_solution(instructions, snake, history)
print("Puzzle 2 =", len(history))
