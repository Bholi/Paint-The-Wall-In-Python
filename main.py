print('Paint The Wall Program')
h = float(input('Enter the height of the wall in m : '))
w = float(input('Enter the width of the wall in m :'))
coverage = 5


def paint_the_wall(height, width, coverage_area):
    number_of_cans = (height * width) / coverage_area

    print(f'The number of cans required is {round(number_of_cans)}')


paint_the_wall(height=h, width=w, coverage_area=coverage)
