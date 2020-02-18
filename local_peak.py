import unittest


def local(array_list):
    peak = []
    if len(array_list) != 0:
        if array_list[0] > array_list[1]:
            peak.append(array_list[0])
        else:
            peak.append(array_list[1])

    return peak


class LocalPeak(unittest.TestCase):
    def test_for_local_peak_in_empty_list(self):
        self.assertEqual([], local([]))

    def test_for_first_local_peak_in_sorted_list_ascending_order(self):
        self.assertEqual([1], local([0, 1, 2, 3, 4]))

    def test_for_first_local_peak_in_sorted_list_descending_order(self):
        self.assertEqual([4], local([4, 3, 2, 1, 0]))

    def test_for_first_local_peak_in_for_repeated_element(self):
        self.assertEqual([4], local([4, 4, 2, 1, 0]))


if __name__ == '__main__':
    unittest.main()
