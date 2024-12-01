path = "AdventOfCode2024/day01/input.txt"

with open(path, encoding="utf-8", mode="r") as raw_data:
    nums1 = []
    nums2 = []
    for line in raw_data:
        n1, n2 = line.strip().split("   ")
        nums1.append(int(n1))
        nums2.append(int(n2))

nums1.sort()
nums2.sort()

# Puzzle 1
result = sum([abs(nums1[i] - nums2[i]) for i in range(len(nums1))])
print("Puzzle 1 =", result)


#Puzzle 2
result = sum([num * nums2.count(num) for num in nums1])
print("Puzzle 2 =", result)
