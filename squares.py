from itertools import islice


def parse_string(s):
    """
    parses individual blocks into arrays of 0s and 1s
    """
    rows = s.split('\n')
    return [parse_row(row) for row in rows]


def parse_row(row):
    return [parse_char(char) for char in row]


def parse_char(char):
    if char == '#':
        return 1
    elif char == '.':
        return 0
    raise ValueError('Invalid character: {}'.format(char))


def calc_sum(values):
    row_sums = [sum(row) for row in values]
    return sum(row_sums)


def validate_square_area(area):
    square = area ** 0.5
    return square.is_integer()


def get_first_point(values):
    """
    get coordinates of the first cell with 1
    """
    first_row = None
    first_column = None
    for i, row in enumerate(values):
            for k, v in enumerate(row):
                if first_row is None and v == 1:
                    first_row = i
                    first_column = k
    return (first_row, first_column)


def get_last_point(values):
    """
    get coordinates of the last cell with 1
    """
    last_row = None
    last_column = None
    for i, row in enumerate(values):
            for k, v in enumerate(row):
                if v == 1:
                    last_row = i
                    last_column = k
    return (last_row, last_column)


def get_height(first_point, last_point):
    height = last_point[0] - first_point[0] + 1
    return height


def get_width(first_point, last_point):
    width = last_point[1] - first_point[1] + 1
    return width


def cut_square(values, first_point, last_point):
    x1, y1, x2, y2 = first_point[1], first_point[0],last_point[1], last_point[0]
    new = [row[x1:x2+1] for row in values[y1:y2+1]]
    return new


def validate_square_filled(height, width, sum_new_square):
    """
    check if all cells are 1s by comparing calculated area
     with sum of the square lists
    """
    area_expected = height * width
    actual_area = sum_new_square
    return actual_area == area_expected


def produce_output(values, case=1):
    # quickly reject square if the area is not square
    if not validate_square_area(calc_sum(values)):
        return "Case #{}: NO".format(case)
    else:
        first_point = get_first_point(values)
        last_point = get_last_point(values)
        new_square = cut_square(values, first_point, last_point)
        sum_new_square = calc_sum(new_square)
        height = get_height(first_point, last_point)
        width = get_width(first_point, last_point)
        if not validate_square_filled(height, width, sum_new_square):
            return "Case #{}: NO".format(case)
        else:
            return "Case #{}: YES".format(case)

def parse_file(filename):
    with open(filename, 'r') as file:
        lines = iter(file)
        next(lines)  # Discard the number of test cases
        while lines:
            number_of_rows = int(next(lines)) 
            string = "".join(list(islice(lines, number_of_rows)))[:-1]  # removing end of line character
            yield list(parse_string(string))

if __name__ == '__main__':
    for index, s in enumerate(list(parse_file('square_detector.txt'))):
        print produce_output(s, index+1)
