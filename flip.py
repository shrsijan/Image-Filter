import common

def flip(image_matrix):
    image_matrix = image_matrix[::-1]
    new_file_name = "Flipped.png"
    common.write_file(new_file_name, image_matrix)

matrix_img = common.read_file("robot.png")
flip(matrix_img)