import unittest
from pyjsonts.time_series_json import TimeSeriesJSON

test_json = TimeSeriesJSON(fn='test/test_json.json')


class TestTimeSeriesJSON(unittest.TestCase):

    def test_parse_json_items(self):
        self.assertTrue(True)
        items = test_json.parse_json_items(tag='item')
        self.assertEqual(len(items), 9)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeSeriesJSON)