from itertools import islice

def parse_string(s):
    """
    parses individual blocks into arrays of 0s and 1s
    """
    l = []
    sublist = []
    for c in s:
        if c != '\n':
            c = 1 if c == '#' else 0
            sublist.append(c)
        else:
            l.append(sublist)
            sublist = []
    l.append(sublist)  # in case line end is not enclosed in the string
    return l


def calc_sum(values):
    sum = 0
    for row in values:
            for v in row:
                sum += v
    return sum


def validate_square_area(area):
    square = area ** 0.5
    if square.is_integer():
        return True
    else:
        return False


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
    if actual_area == area_expected:
        return True
    else:
        return False


def produce_output(values, case=1):
    # values = parse_string(input)
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
        next(lines)  # Discard the number of test cases T
        while lines:
            number_of_rows = int(next(lines)) 
            string = "".join(list(islice(lines, number_of_rows)))[:-1]  # removing end of line character
            yield list(parse_string(string))

if __name__ == '__main__':
    for index, s in enumerate(list(parse_file('square_detector.txt'))):
        print produce_output(s, index+1)

