import unittest
from pyjsonts.time_series_json import TimeSeriesJSON

test_json = TimeSeriesJSON(fn='test/test_json.json')


class TestTimeSeriesJSON(unittest.TestCase):

    def test_parse_json_items(self):
        items = self.test_json.parse_json_items()
        self.assertTrue(len(items), 9)

if __name__ == '__main__':
    unittest.main()