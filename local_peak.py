import unittest


def local(array_list):
    return []


class LocalPeak(unittest.TestCase):
    def test_for_local_peak_in_empty_list(self):
        self.assertEqual(local([]), [])


if __name__ == '__main__':
    unittest.main()
