import common
import copy

def blur(image_matrix):
    channels = len(image_matrix[0][0])
    new_image = copy.deepcopy(image_matrix)

    for row in range(len(image_matrix)):
         for col in range(len(image_matrix[row])):
            for channel in range(channels):
                total = 0
                count = 0

                for r_val in range(-1, 4):
                    for c_val in range(-1, 4):
                        neighboring_row = row + r_val
                        neighboring_col = col + c_val

                        if 0 <= neighboring_row < len(image_matrix) and 0 <= neighboring_col < len(image_matrix[row]):
                            total += image_matrix[neighboring_row][neighboring_col][channel]
                            count += 1
                new_image[row][col][channel] = total // count

    new_file_name = "Blurred.png"
    common.write_file(new_file_name, new_image)

matrix_img = common.read_file("robot.png")
blur(matrix_img)

# import common
# import copy

# def blur(image_matrix):
#     new_image_matrix = copy.deepcopy(image_matrix)
#     channels = len(image_matrix[0][0])

#     for row in range(len(image_matrix)):
#         for col in range(len(image_matrix[row])):
#             for channel in range(channels):
#                 total = 0
#                 count = 0

#                 for r in range(-1, 4):
#                     for c in range(-1, 4):
#                         neighbor_row = row + r
#                         neighbor_col = col + c

#                         if 0 <= neighbor_row < len(image_matrix) and 0 <= neighbor_col < len(image_matrix[row]):
#                             total += image_matrix[neighbor_row][neighbor_col][0]
#                             count += 1

#                 new_image_matrix[row][col] = total // count

#     new_file_name = "Blurred.png"
#     common.write_file(new_file_name, new_image_matrix)

# matrix_img = common.read_file("robot.png")
# blur(matrix_img)



