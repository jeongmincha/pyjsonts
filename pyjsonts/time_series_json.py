import json
import ijson
import numpy as np


class TimeSeriesJSON:

    def __init__(self, f=None, fn=None, tag='item'):
        """
        :param f: file object (_io.TextIOWrapper)
        :param fn: file name as a string
        :param tag: tag for dividing json items
            default value is 'item' because this value is default in ijson
        """
        if f is not None:
            self.__type = 'file'
            self.__file = f
        elif fn is not None:
            self.__type = 'file_name'
            self.__file_name = fn
            self.__file = open(fn)

        self.__items = self.parse_json_items(tag)

    def parse_json_items(self, tag, limit=0):
        self.__items = []
        self.__file.seek(0)
        cnt = 0

        objs = ijson.items(self.__file, tag)
        for obj in objs:
            item = json.dumps(obj,
                              sort_keys=True,
                              indent=4,
                              ensure_ascii=True)
            self.__items.append(item)
            cnt += 1
            if limit != 0 and cnt >= limit:
                break

        return self.__items

    def get_timestamp_list(self):
        return []

    def get_dict_time_freq(self):
        return {}

    def get_time_dist(self, base_timestamp, interval, num_bins):
        dist = np.array([[0, ]] * num_bins)
        timestamps = self.get_dict_time_freq()

        for idx in range(num_bins):
            if idx in timestamps:
                dist[idx] = timestamps[idx]

        return dist
