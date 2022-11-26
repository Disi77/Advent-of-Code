with open("day13_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()

timestamp = int(input_data[0])
bus_numbers = [int(x) for x in input_data[1].replace("x,", "").split(",")]

for stamp in range(timestamp, timestamp + 10**2):
    for bus in bus_numbers:
        if stamp % bus == 0:
            print("What is the ID of the earliest bus * the number of minutes you'll need to wait for that bus?")
            print(" =", bus * (stamp - timestamp))
            exit()
