import common

def red_stripe(image_matrix):
    stripe_height = 50 
    for row in range(len(image_matrix)):
        if (row // stripe_height) % 2 == 0:
            for col in range(len(image_matrix[row])):
                image_matrix[row][col] = [255, image_matrix[row][col][2] , image_matrix[row][col][2]]
    new_file_name = "Redstripes_image.png"
    common.write_file(new_file_name, image_matrix) 

matrix_img = common.read_file("robot.png") 
red_stripe(matrix_img)

