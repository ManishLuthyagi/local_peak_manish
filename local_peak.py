import unittest


def local(array_list):
    peak = []
    if len(array_list) != 0:
        peak.append(array_list[-1])
    return peak


class LocalPeak(unittest.TestCase):
    def test_for_local_peak_in_empty_list(self):
        self.assertEqual(local([]), [])

    def test_for_first_local_peak_in_sorted_list_ascending_order(self):
        self.assertEqual(local([0, 1, 2, 3]), [3])


if __name__ == '__main__':
    unittest.main()
