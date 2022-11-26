with open("day20_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read().split("\n\n")


class Image:
    """
    Class for Image - from input image it is created
    attributes like name, body and borders (up, down, left, right).
    Attribute list_borders contains list of possible image borders after
    flipping and rotating.
    """
    def __init__(self, image):
        self.name = int(image[5:9])
        self.body = image[10:].strip()
        self.up = self.body[:11].strip()
        self.down = self.body[-10:].strip()
        left = ""
        right = ""
        for i in range(0, 110, 11):
            left += self.body[i]
            right += self.body[i+9]
        self.left = left.strip()
        self.right = right.strip()
        self.state = 0
        self.list_borders = [self.left,
                             self.left[::-1],
                             self.right,
                             self.right[::-1],
                             self.up,
                             self.up[::-1],
                             self.down,
                             self.down[::-1]
                             ]


# From input data create list of objects from class Image
IMAGES = []
for item in input_data:
    IMAGES.append(Image(item))


# Go through all images in list IMAGES and compare list of possible image
# borders and counts the number of borders that are the same for 2 images
for image in IMAGES:
    match = 0
    for i, border in enumerate(image.list_borders):
        for image2 in IMAGES:
            if image.name == image2.name:
                continue
            for i2, border2 in enumerate(image2.list_borders):
                if border == border2:
                    match += 1
    image.match = match

# Creates list of results, where for every image is added tuple with image
# count of matches with another images and image name
results = []
for image in IMAGES:
    results.append((image.match, image.name))

# Sort this list of results
results.sort()

# Find in results first 4 items = items with lowest count of
# matches = 4 corners AND multiply names of this tiles
final = 1
for count, item in results[:4]:
    final *= item

print("What do you get if you multiply together the IDs of the four corner tiles?")
print(f"= {final}")
