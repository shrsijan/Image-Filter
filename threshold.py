import common

def threshold(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            rato, hariyo, nilo = image_matrix[row][col][0], image_matrix[row][col][1], image_matrix[row][col][2]
            if rato < red_min or rato > red_max:
                rato = 0
            if hariyo < green_min or hariyo > green_max:
                hariyo = 0
            if nilo < blue_min or nilo > blue_max:
                nilo = 0

            image_matrix[row][col] = [rato, hariyo, nilo]

    common.write_file("threshold.png", image_matrix)

matrix_img = common.read_file("cat.png")
threshold(matrix_img, int(input("Red min value:")),int(input("Red max value:")),int(input("Green min value:")),int(input("Green max value:")),int(input("Blue min value:")),int(input("Blue max value:")))