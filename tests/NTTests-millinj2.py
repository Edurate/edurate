import pytest
import graphing

def test_convertToInts():
    """Testing the convertToInts() function"""
    list = [["Some", "Something", "1", "2", "3"]]
    desired_output_string = [["Some", "Something", 1, 2, 3]]
    actual_output_string = graphing.convertToInts(list)
    assert len(list) == 5
    assert(desried_output_string == actual_output_string) is True
