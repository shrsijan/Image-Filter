import common

def pixelate_image(image_matrix, pixel_size):
    height = len(image_matrix)
    width = len(image_matrix[0])

    for row in range(0, height, pixel_size):
        for col in range(0, width, pixel_size):
            # Calculate the average color within the pixel block
            total_r, total_g, total_b = 0, 0, 0
            count = 0

            for r in range(pixel_size):
                for c in range(pixel_size):
                    if row + r < height and col + c < width:
                        r, g, b = image_matrix[row + r][col + c][0], image_matrix[row + r][col + c][1], image_matrix[row + r][col + c][2]
                    image_matrix[row][col] = [r[0], g[1], b[2]]
                    

    new_file_name = f"Pixelated_{pixel_size}.png"
    common.write_file(new_file_name, image_matrix)

matrix_img = common.read_file("robot.png")
pixelate_image(matrix_img, pixel_size=2)
