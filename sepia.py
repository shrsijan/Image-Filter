

import common

def sepia(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            # the variable names are in Nepali (red=rato, green=hariyo, blue=nilo)
            output_rato = min(255, int((image_matrix[row][col][0] * 0.393) + (image_matrix[row][col][1] * 0.769) + (image_matrix[row][col][2] * 0.189)))
            output_hariyo = min(255, int((image_matrix[row][col][0] * 0.349) + (image_matrix[row][col][1] * 0.686) + (image_matrix[row][col][2] * 0.168)))
            output_nilo = min(255, int((image_matrix[row][col][0] * 0.272) + (image_matrix[row][col][1] * 0.534) + (image_matrix[row][col][2] * 0.131)))
            image_matrix[row][col] = [output_rato, output_hariyo, output_nilo]
    
    new_file_name = "Sepia.png"
    common.write_file(new_file_name, image_matrix)

matrix_img = common.read_file("robot.png")
sepia(matrix_img)

