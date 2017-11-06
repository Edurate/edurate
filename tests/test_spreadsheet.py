"""Test functions in spreadsheey.py."""
import spreadsheet


def test_get_graph_data():
    """Check that spreadsheet data is processed correctly into graph data."""
    spreadsheet_list = [{'Question 5': 'Text answer to question 5'}]

    expected_graph_data = [['Question 5'], ['Text answer to question 5']]
    actual_graph_data = spreadsheet.get_graph_data(spreadsheet_list)

    assert actual_graph_data == expected_graph_data


def test_flip_responses():
    """Check if rows and columns have been switched."""
    list_to_flip = [['Row 1 Col 1', 'Row 1 Col 2', 'Row 1 Col 3'],
                    ['Row 2 Col 1', 'Row 2 Col 2', 'Row 2 Col 3'],
                    ['Row 3 Col 1', 'Row 3 Col 2', 'Row 3 Col 3']]

    expected_flipped_list = [['Row 1 Col 1', 'Row 2 Col 1', 'Row 3 Col 1'],
                             ['Row 1 Col 2', 'Row 2 Col 2', 'Row 3 Col 2'],
                             ['Row 1 Col 3', 'Row 2 Col 3', 'Row 3 Col 3']]

    actual_flipped_list = spreadsheet.flip_responses(list_to_flip)

    assert actual_flipped_list == expected_flipped_list


def test_filter_dates():
    """Check that only responses from most recent date are returned."""
    response_list = [['11/1/2017'], ['11/2/2017'], ['11/3/2017'], ['11/5/2017'], ['11/5/2017']]

    expected_latest_date_list = [['11/5/2017'], ['11/5/2017']]
    actual_latest_date_list = spreadsheet.filter_dates(response_list)

    assert actual_latest_date_list == expected_latest_date_list
