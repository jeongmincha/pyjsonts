import unittest
from pyjsonts.time_series_json import TimeSeriesJSON


class TestTimeSeriesJSON(unittest.TestCase):

    def __init__(self):
        test_json = TimeSeriesJSON('./test_json.json')

if __name__ == '__main__':
    unittest.main()