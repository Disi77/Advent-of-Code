import math


with open("day20_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read().split("\n\n")


def create_final_image(FINAL_IMAGE):
    """
    From list of IMAGES in final state create final image:
        * from every original image deletes the border and
        * gaps between images
    Returns final image as string.
    """
    final = []
    for i_row, row in enumerate(FINAL_IMAGE):
        for index in range(len(FINAL_IMAGE[0][0].body.split("\n"))-1):
            if index == 0:
                continue
            final_row = ""
            for i_col, item in enumerate(row):
                final_row += item.body.split("\n")[index][1:-1]
            final.append(final_row)
    return "\n".join(final)


def make_cutout(image, start_i, start_j, h_monster, w_monster):
    """
    Create cutout from final image from coordinates (start_i, start_j)
    and as size as monster image.
    """
    new_image = ""
    image = image.split("\n")
    for i_row in range(start_i, start_i + h_monster):
        new_image += image[i_row][start_j: start_j + w_monster] + "\n"
    return new_image


def monster_in_cutout(monster, cutout):
    """
    Return True if monster is in cutout.
    """
    for i_monster, char_monster in enumerate(monster):
        if char_monster == "#" and cutout[i_monster] == ".":
            return False
    else:
        return True


def set_rotation_and_flip_for_first_2_images():
    """
    For first 2 images find correct rotation and flip = go through all possible
    states (= rotation and flip) for both images and if borders are same, then
    we have what we are looking for.
    """
    while True:
        for state1 in range(0, 8):
            for state2 in range(0, 8):
                FINAL_IMAGE[0][0].set_state(state1)
                FINAL_IMAGE[0][1].set_state(state2)
                if FINAL_IMAGE[0][0].right == FINAL_IMAGE[0][1].left:
                    return


class Image:
    """
    Class for Image - from input image it is created attributes like name,
    body and borders (up, down, left, right). Attribute list_borders contains
    list of possible image borders after flipping and rotating.

    Class contains methods for rotating and flipping and method for change
    state of image (they can be 8 different states - after rotating 4 different
    states and for every state after rotating 1 additional state after flipping
    => 4 * 2 = 8 states).
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

    def change_state(self):
        if self.state % 2 == 0:
            self.flip()
            self.rotate_right()
        else:
            self.flip()
        self.state += 1
        self.state = self.state % 8

    def set_state(self, num):
        while num != self.state:
            self.change_state()

    def rotate_right(self):
        up = self.left[::-1]
        down = self.right[::-1]
        left = self.down
        right = self.up
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.body = "\n".join("".join(x) for x in list(zip(*self.body.strip().split("\n")[::-1])))

    def flip(self):
        up = self.down
        down = self.up
        left = self.left[::-1]
        right = self.right[::-1]
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.body = "\n".join(self.body.split("\n")[::-1])


# From input data create list of objects from class Image
IMAGES = []
for item in input_data:
    IMAGES.append(Image(item))

# Go through all images in list IMAGES and compare list of possible image
# borders and counts the number of borders that are the same for 2 images.
# If the border doesnt match nothing, then delete this border from list_borders
# And creates new attribute self.match_with as list of names of images with
# them the image has match
for image in IMAGES:
    match = 0
    image.match_with = set()
    for i, border in enumerate(image.list_borders):
        border_match = 0
        for image2 in IMAGES:
            if image.name == image2.name:
                continue
            for i2, border2 in enumerate(image2.list_borders):
                if border == border2:
                    match += 1
                    image.match_with.add(image2.name)
                    border_match += 1
        if border_match == 0:
            image.list_borders[i] = ""
    image.match = match
    image.match_with = list(image.match_with)


# Delete empty border from list_borders
for image in IMAGES:
    while "" in image.list_borders:
        image.list_borders.remove("")

# Split images from IMAGES to categories CORNER x BORDER x MIDDLE
IMAGES_CORNER = []
IMAGES_BORDER = []
IMAGES_MIDDLE = []

for image in IMAGES:
    if len(image.list_borders) == 4:
        IMAGES_CORNER.append(image)
    elif len(image.list_borders) == 6:
        IMAGES_BORDER.append(image)
    elif len(image.list_borders) == 8:
        IMAGES_MIDDLE.append(image)


size = int(math.sqrt(len(IMAGES)))

# CREATE LIST OF IMAGES IN CORRECT ORDER

# Create empty list of final images = the images will be save in this
# variable FINAL_IMAGE in correct order. FINAL_IMAGE is list of lists
FINAL_IMAGE = []
for i in range(size):
    FINAL_IMAGE.append((list([None] * size)))

# Go through the empty places in FINAL_IMAGE and find the correct
# image which match this place.
for i_row, row in enumerate(FINAL_IMAGE):
    for i_col, item in enumerate(row):
        if isinstance(item, Image):
            continue
        # ITEM IS CORNER
        if (i_row, i_col) in [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]:
            # TOP LEFT CORNER
            if i_row == i_col == 0:
                # For first corner = first item in FINAL_IMAGE simply choose
                # one random image from IMAGES_CORNER.
                FINAL_IMAGE[0][0] = (IMAGES_CORNER.pop())
            # TOP RIGHT CORNER
            if i_row == 0 and i_col == size-1:
                for i, image in enumerate(IMAGES_CORNER):
                    if image.name in FINAL_IMAGE[0][-2].match_with:
                        FINAL_IMAGE[i_row][i_col] = image
                        del IMAGES_CORNER[i]
                        break
            # DOWN LEFT CORNER
            if i_row == size-1 and i_col == 0:
                for i, image in enumerate(IMAGES_CORNER):
                    if image.name in FINAL_IMAGE[-2][0].match_with:
                        FINAL_IMAGE[i_row][i_col] = image
                        del IMAGES_CORNER[i]
                        break
            # DOWN RIGHT CORNER
            if i_row == size-1 and i_col == size-1:
                FINAL_IMAGE[i_row][i_col] = IMAGES_CORNER[0]
        # ITEM IS BORDER
        elif i_row in [0, size-1] or i_col in [0, size-1]:
            if i_row in [0, size-1]:
                for i, image in enumerate(IMAGES_BORDER):
                    if image.name in FINAL_IMAGE[i_row][i_col - 1].match_with:
                        FINAL_IMAGE[i_row][i_col] = image
                        del IMAGES_BORDER[i]
                        break
            if i_col in [0, size-1]:
                for i, image in enumerate(IMAGES_BORDER):
                    if image.name in FINAL_IMAGE[i_row - 1][i_col].match_with:
                        FINAL_IMAGE[i_row][i_col] = image
                        del IMAGES_BORDER[i]
                        break
        # ITEM IS IN THE MIDDLE
        else:
            # Find common match from image above and on the left
            for item1 in FINAL_IMAGE[i_row - 1][i_col].match_with:
                for item2 in FINAL_IMAGE[i_row][i_col - 1].match_with:
                    if item1 == item2:
                        next_item = item1
                        break
                else:
                    continue
                break
            # From IMAGES_MIDDLE find image with this number
            for i, image in enumerate(IMAGES_MIDDLE):
                if image.name == next_item:
                    FINAL_IMAGE[i_row][i_col] = image
                    # Delete the number of an already assigned image from the
                    # list self.match_with = it will be usefull for searching
                    # for another images.
                    FINAL_IMAGE[i_row][i_col].match_with.remove(FINAL_IMAGE[i_row - 1][i_col].name)
                    FINAL_IMAGE[i_row][i_col].match_with.remove(FINAL_IMAGE[i_row][i_col - 1].name)
                    del IMAGES_MIDDLE[i]
                    break

# List of images is now in correct order

# FIND CORRECT ROTATION AND FLIP OF EVERY IMAGE

# For first 2 images find correct rotation and flip = go through all possible
# states (= rotation and flip) for both images and if borders are same, then
# we have what we are looking for.
set_rotation_and_flip_for_first_2_images()

# Then continue with all images and try to find rotation and flip which match
# the already set images.
for i_row, row in enumerate(FINAL_IMAGE):
    for i_col, item in enumerate(row):
        # First 2 images were already set before
        if (i_row, i_col) in [(0, 0), (0, 1)]:
            continue
        # If you are setting first image in second row (with index 1), then
        # check, if is or is not needed to flip first row (with index 0).
        # If there is no image with match, then is needed to flip first row.
        if i_row == 1 and i_col == 0:
            for state in range(0, 8):
                FINAL_IMAGE[i_row][i_col].set_state(state)
                if FINAL_IMAGE[i_row - 1][i_col].down == FINAL_IMAGE[i_row][i_col].up:
                    break
            else:
                for image in FINAL_IMAGE[0]:
                    image.flip()
        # Try to find correct rotation and flip of image which match the
        # already set images.
        if i_col != 0:
            for state in range(0, 8):
                FINAL_IMAGE[i_row][i_col].set_state(state)
                if FINAL_IMAGE[i_row][i_col - 1].right == FINAL_IMAGE[i_row][i_col].left:
                    break
        elif i_col == 0:
            for state in range(0, 8):
                FINAL_IMAGE[i_row][i_col].set_state(state)
                if FINAL_IMAGE[i_row - 1][i_col].down == FINAL_IMAGE[i_row][i_col].up:
                    break

# IMAGEs ARE IN CORRECT ORDER, ROTATION AND FLIP = we can create final image
# I am using my class Image and because of that I need to add to the image
# dummy first line with name = Tile 9999:

final_image = Image("Tile 9999:\n" + create_final_image(FINAL_IMAGE))

monster = """
..................#.
#....##....##....###
.#..#..#..#..#..#...
""".strip()

h_image = len(final_image.body.split("\n"))
w_image = len(final_image.body.split("\n")[0])

h_monster = len(monster.split("\n"))
w_monster = len(monster.split("\n")[0])

# Change of state of final image = rotation and flip of final image =>
# and try to find monsters
for state in range(0, 8):
    final_image.set_state(state)

    count_of_monsters = 0
    for start_i in range(0, h_image - h_monster):
        for start_j in range(0, w_image - w_monster):
            cutout = make_cutout(final_image.body, start_i, start_j, h_monster, w_monster)
            result = monster_in_cutout(monster, cutout)
            if result:
                count_of_monsters += 1

    if count_of_monsters == 0:
        continue

    # Final result = count of "#" in final image minus count of "#" in all
    # monsters I found out
    print("How many # are not part of a sea monster?")
    result = final_image.body.count("#") - count_of_monsters * monster.count("#")
    print(result)
    break
