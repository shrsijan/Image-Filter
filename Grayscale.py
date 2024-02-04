import common

def grayscale(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            average_value = sum(image_matrix[row][col]) // 3
            image_matrix[row][col] = [average_value, average_value, average_value]
    new_file_name ="Grayscale_image.jpeg"
    common.write_file(new_file_name, image_matrix) 

matrix_img = common.read_file("rainbow.png") 
grayscale(matrix_img)
