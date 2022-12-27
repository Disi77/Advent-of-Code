from pathlib import Path


here = Path(__file__).parent
snafu_numbers = Path(here / "input.txt").read_text().split("\n")

def snafu_to_decimal(snafu):
    key = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    decimal = 0
    for i in range(1, len(snafu) + 1):
        decimal += key[snafu[-i]] * 5 ** (i - 1)
    return decimal


def decimal_to_snafu(decimal):
    key = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    reminders = []
    while True:
        reminders.append(decimal % 5)
        decimal = decimal // 5
        if decimal == 0:
            break

    snafu = ""
    koef = 0
    for num in reminders:
        num = num + koef
        if num in key:
            snafu = key[num] + snafu
            if koef:
                koef = 0
        elif num - 5 in key:
            snafu = key[num - 5] + snafu
            koef = 1

    return snafu


decimal_sum = 0
for snafu in snafu_numbers:
    decimal_sum += snafu_to_decimal(snafu)

snafu = decimal_to_snafu(decimal_sum)
print("Puzzle 1 =", snafu)
