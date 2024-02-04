import common
def random_color_overlay(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            image_matrix[row][col] = [ 100, image_matrix[row][col][1], 100 ]

    new_file_name = "Random_Color_Overlay.png"
    common.write_file(new_file_name, image_matrix)

matrix_img = common.read_file("ss.png")
random_color_overlay(matrix_img)
