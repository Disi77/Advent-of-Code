import re


def passport_is_valid(passport, fields_mandatory):
    for field, value in fields_mandatory.items():
        if not passport.get(field):
            return False
        if not re.match(value, passport[field]):
            return False
    return True


with open("day04_input.txt", encoding="utf-8", mode="r") as f:
    batch = f.read().split("\n\n")

data = []
for record in batch:
    record_dict = {}
    for item in record.split():
        record_dict[item[:3]] = item[4:]
    data.append(record_dict)

fields_mandatory = {"byr": r"^19[2-9][0-9]|200[0-2]$",
                    "iyr": r"^201[0-9]|2020$",
                    "eyr": r"^202[0-9]|2030$",
                    "hgt": r"^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$",
                    "hcl": r"^#[0-9a-f]{6}$",
                    "ecl": r"^amb|blu|brn|gry|grn|hzl|oth$",
                    "pid": r"^[0-9]{9}$"}
fields_optional = ["cid"]

valid = 0
for passport in data:
    valid += passport_is_valid(passport, fields_mandatory)

print(valid)
