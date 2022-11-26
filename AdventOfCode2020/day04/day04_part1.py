def passport_is_valid(passport, fields_mandatory):
    for field in fields_mandatory:
        if not passport.get(field):
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

fields_mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
fields_optional = ["cid"]

valid = 0
for passport in data:
    valid += passport_is_valid(passport, fields_mandatory)

print(valid)
