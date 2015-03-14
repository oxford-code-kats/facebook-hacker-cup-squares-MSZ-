"""
tests for squares functions
"""
import pytest
from squares import parse_string, calc_sum, validate_square_area, get_first_point, get_last_point, \
get_height, get_width, cut_square, validate_square_filled, produce_output, parse_file

def test_parse_string():
    """
    if strings are converted properly to 0s,1s
    when 1 means #
    """

    input = """..##
..##
....
...."""

    expected = [[0,0,1,1],
               [0,0,1,1],
               [0,0,0,0],
               [0,0,0,0]]

    actual = parse_string(input)
    assert expected == actual

def test_sum_area():
    input = [[0,0,1,1],
               [0,0,1,1],
               [0,0,0,0],
               [0,0,0,0]]
    expected = 4
    actual = calc_sum(input)
    assert expected == actual



def test_valid_square_area():
    input = 4
    expected = True
    actual = validate_square_area(input)
    assert expected == actual

def test_invalid_square_area():
    input = 5
    expected = False
    actual = validate_square_area(input)
    assert expected == actual


def test_first_point():
    input = [[0,0,1,1],
               [0,0,1,1],
               [0,0,0,0],
               [0,0,0,0]]
    expected = (0,2)
    actual = get_first_point(input)
    assert expected == actual


def test_last_point():
    input = [[0,0,1,1],
               [0,0,1,1],
               [0,0,0,0],
               [0,0,0,0]]
    expected = (1,3)
    actual = get_last_point(input)
    assert expected == actual


def test_get_height():
    first_point = (0,2)
    last_point = (1,3)
    expected = 2
    actual = get_height(first_point, last_point)
    assert expected == actual


def test_get_width():
    first_point = (0, 2)
    last_point = (1, 3)
    expected = 2
    actual = get_width(first_point, last_point)
    assert expected == actual


def test_cut_square():
    values = [[0, 0, 1, 1],
              [0, 0, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    first_point = (0, 2)
    last_point = (1, 3)

    expected = [[1, 1], [1, 1]]
    actual = cut_square(values, first_point, last_point)
    assert expected == actual


def test_square_filled():
    height = 2
    width = 2
    sum_cut_square = 4

    expected = True
    actual = validate_square_filled(height, width, sum_cut_square)
    assert expected == actual


def test_square_not_filled():
    height = 3
    width = 3
    sum_cut_square = 4

    expected = False
    actual = validate_square_filled(height, width, sum_cut_square)
    assert expected == actual


def test_result_output_yes():
    values = [[0, 0, 1, 1],
              [0, 0, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    expected = "Case #1: YES"
    actual = produce_output(values)
    assert expected == actual


def test_result_output_no():
    values = [[0, 0, 0, 1],
              [0, 0, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    expected = "Case #1: NO"
    actual = produce_output(values)
    assert expected == actual


def test_parsing_file():

    expected = [[[0,0,1,1],
                [0,0,1,1],
                [0,0,0,0],
                [0,0,0,0]],
                [[1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1],
                [0,0,0,0,0]]]
    # print 'expected', expected
    actual = list(parse_file('example_input_file.txt'))
    # print 'actual', actual

    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])