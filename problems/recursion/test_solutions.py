from solutions import list_filter, count_runs, sequence_position

def test_list_filter():
    assert list_filter([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 3 == 0) == [3, 6]

    assert list_filter([1, 3, 2, 4, 0, 3, 6, -1, 8], lambda x: x >= 3) == [
        3,
        4,
        3,
        6,
        8,
    ]

    assert list_filter(
        ["ciaos", "pools", "nones", "mashed", "braes", "trip", "harry", "kooked", "mavens", "arrow"], 
        lambda word: "o" in word
    ) == ['ciaos', 'pools', 'nones', 'kooked', 'arrow']


def test_count_runs():
    assert count_runs([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]) == [2, 3, 1, 5, 2]


def test_sequence_position():
    assert sequence_position([1, 2, 2, 3, 1, 3, 5, 4, 2, 6, 7, 5, 3, 1, 3], [3,1,3]) == [3, 12]