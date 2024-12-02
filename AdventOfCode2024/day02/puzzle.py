path = "AdventOfCode2024/day02/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    reports = []
    for line in raw_data:
        numbers = [int(item) for item in line.strip().split()]
        reports.append(numbers)

# Puzzle 1
def report_is_save(report):
    if report[0] > report[1]:
        for i in range(1, len(report)):
            if report[i - 1] <= report[i]:
                break
            if report[i - 1] - report[i] > 3:
                break
        else:
            return True

    else:
        for i in range(1, len(report)):
            if report[i - 1] >= report[i]:
                break
            if report[i - 1] - report[i] < - 3:
                break
        else:
            return True
    
    return False


save_reports = 0
for report in reports:
    if report_is_save(report):
        save_reports += 1
    
print("Puzzle 1 =", save_reports)


#Puzzle 2
save_reports = 0
for report in reports:
    if report_is_save(report):
        save_reports += 1
    else:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if report_is_save(new_report):
                save_reports += 1
                break

print("Puzzle 2 =", save_reports)
