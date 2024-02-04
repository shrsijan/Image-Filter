import common

def invert_colors(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            image_matrix[row][col] = [255 - image_matrix[row][col][0], 255 - image_matrix[row][col][1], 255 - image_matrix[row][col][2]]
    new_file_name ="Invert_image.png"
    common.write_file(new_file_name, image_matrix) 

matrix_img = common.read_file("rainbow.png") 
invert_colors(matrix_img)
